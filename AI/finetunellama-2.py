# -*- coding: utf-8 -*-
"""FineTuneLLaMA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zabjlxbqTpMPvUM8kXeI4bj0l9klGzvE

Code following the example provided in https://www.datacamp.com/tutorial/fine-tuning-llama-2

We will start by installing the required libraries.


*  The %%capture magic command is used to suppress the output of the cell in Jupyter notebook.
*  The %pip magic command is used to install Python packages within a Jupyter notebook.


The code installs several Python packages, including transformers, which is a library developed by Hugging Face. Once you have installed the transformers package using the pip command, you can use it to interact with Hugging Face's model hub.

The datasets library provides a convenient interface for downloading, accessing, and working with a wide variety of Hugging Face datasets commonly used in natural language processing (NLP) and machine learning.

Parameter-Efficient Fine-Tuning (PEFT) methods enable efficient adaptation of pre-trained language models (PLMs) to various downstream applications without fine-tuning all the model's parameters. Fine-tuning large-scale PLMs is often prohibitively costly. In this regard, PEFT methods only fine-tune a small number of (extra) model parameters, thereby greatly decreasing the computational and storage costs.

TRL is a full stack library where we provide a set of tools to train transformer language models with Reinforcement Learning, from the Supervised Fine-tuning step (SFT), Reward Modeling step (RM) to the Proximal Policy Optimization (PPO) step.
"""

# Commented out IPython magic to ensure Python compatibility.
# %%capture
# %pip install accelerate peft bitsandbytes transformers trl

"""After that, we will load the necessary modules from these libraries."""



import os
import torch
from datasets import load_dataset
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    TrainingArguments,
    pipeline,
    logging,
)
from peft import LoraConfig
from trl import SFTTrainer

"""We now specify the names of the base model, the dataset for fine-tuning it and the resulting new model"""

# Model from Hugging Face hub
base_model = "NousResearch/Llama-2-7b-chat-hf"

# New instruction dataset
guanaco_dataset = "mlabonne/guanaco-llama2-1k"

# Fine-tuned model
new_model = "llama-2-7b-chat-guanaco"

"""
We now use the load_dataset function from the Hugging Face datasets library to load a specific split ("train") from the dataset named guanaco_dataset"""

dataset = load_dataset(guanaco_dataset, split="train")

"""Creating a configuration for quantization, specifically 4-bit quantization, using the bitsandbytes library in PyTorch

More bits in the context of quantization means using a larger number of bits to represent each value in your data. The number of bits used in quantization affects the precision with which values can be represented
"""

compute_dtype = getattr(torch, "float16")

quant_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=compute_dtype,
    bnb_4bit_use_double_quant=False,
)

"""The Hugging Face transformers library works with tokenizers, specifically an AutoTokenizer, for a pre-trained model.

A tokenizer is a fundamental component in natural language processing (NLP) that breaks down text into smaller units called tokens. Tokens can be words, subwords, or characters, depending on the granularity of the tokenization process. The primary purpose of a tokenizer is to facilitate the processing and analysis of textual data in NLP tasks
"""

tokenizer = AutoTokenizer.from_pretrained(base_model, trust_remote_code=True)
tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = "right"

"""We now define parameters for a model using the LoraConfig class, likely within the context of the peft library or a related library.

The parameter task_type is set to "CAUSAL_LM," because the model is configured for a causal language modeling task. Causal language models, such as autoregressive models, predict the next word in a sequence given the previous words.
"""

peft_params = LoraConfig(
    lora_alpha=16,
    lora_dropout=0.1,
    r=64,
    bias="none",
    task_type="CAUSAL_LM",
)

"""We now configure the training parameters using the TrainingArguments class"""

training_params = TrainingArguments(
    output_dir="./results",
    num_train_epochs=1,
    per_device_train_batch_size=4,
    gradient_accumulation_steps=1,
    optim="paged_adamw_32bit",
    save_steps=25,
    logging_steps=25,
    learning_rate=2e-4,
    weight_decay=0.001,
    fp16=False,
    bf16=False,
    max_grad_norm=0.3,
    max_steps=-1,
    warmup_ratio=0.03,
    group_by_length=True,
    lr_scheduler_type="constant",
    report_to="tensorboard"
)

"""Then we set up a trainer for training a machine learning model using the SFTTrainer class

Supervised fine-tuning (or SFT for short) allow to fine-tune a base model with a new dataset
"""

trainer = SFTTrainer(
    model=base_model,
    train_dataset=dataset,
    peft_config=peft_params,
    dataset_text_field="text",
    max_seq_length=None,
    tokenizer=tokenizer,
    args=training_params,
    packing=False,
)

"""
We can now use the pipeline function, from the transformers library, to generate text based on a prompt using a pre-trained language model"""

prompt = "Who is Leonardo Da Vinci?"
pipe = pipeline(task="text-generation", model=model, tokenizer=tokenizer, max_length=200)
result = pipe(f"<s>[INST] {prompt} [/INST]")
print(result[0]['generated_text'])

prompt = "What is Datacamp Career track?"
result = pipe(f"<s>[INST] {prompt} [/INST]")
print(result[0]['generated_text'])