# Esercizi con metadati


Diversi sistemi utilizzano diversi formati di metatati, avere a disposizioni degli strumenti di conversione diveta quindi fondamentale 

Il formato più comune per Pandoc è YAML 

## Esercizio 1

In Pandoc un file di metadati, in formato YAML o JSON, può essere utilizzato anche per parametrizzare una trasformazione utilizzando dei placeholder all’interno di un documento template 

``
pandoc --metadata-file=mymetadata.json --template=template.html -o output.html
``

## Esercizio 2

Una librerai che supporta trasforamzioni di YAML in altri formati è PyYAML 

``
pip install pyyaml
``

A questo punto possiamo convertire un file YAML attraverso uno script che legga il file YAML come un dictionary per poi trasformare i suoi elementi negli elementi del formato di destinazione. Ad esempio:

``
python3 YAML2JSON-LD.py 
``

## Esercizio 3

Non tutti i metadati inseriti in documento markdown possono essere di interesse per il sistema di destinazione. Prendendo in input ``input.yaml`` proviamo quindi ad estrarre i soli metadati relativi all'elemento ``scehma.org`` 

