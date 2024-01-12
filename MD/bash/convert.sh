#!/bin/bash

# Set the Pandoc command with your desired options
PANDOC_CMD="pandoc -s --from markdown --to html5 --mathjax --bibliography=ref.bib --metadata title=Prova"

# Input and output directories
INPUT_DIR="test"
OUTPUT_DIR="actual"

# Iterate over all Markdown files in the input directory
for file in "$INPUT_DIR"/*.md; do
    # Extract the filename without the extension
    filename=$(basename -- "$file")
    filename_noext="${filename%.*}"

    # Execute the Pandoc command for each file
    $PANDOC_CMD -o "$OUTPUT_DIR/$filename_noext.html" "$file"
done