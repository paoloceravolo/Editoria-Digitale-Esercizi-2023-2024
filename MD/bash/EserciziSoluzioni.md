# Esercizi: automatizzare le trasformazioni Pandoc da Shell

A set of five exercises that progressively introduce to Bash scripting for automating Pandoc transformations. Each exercise builds on the previous one, gradually increasing in complexity.

## Exercise 1: Basic Conversion

### Assignment:
Write a Bash script named *convert_to_html.sh* that converts a single Markdown file to HTML using Pandoc. Ensure that the output HTML file is named output.html.

### Hints:

- Use a variable to store the Pandoc command with appropriate options.
- Specify the input and output file paths in the script.

### Solution:

```
#!/bin/bash

# Set the Pandoc command with your desired options
PANDOC_CMD="pandoc --from markdown --to html5 --mathjax --bibliography=ref.bib"

# Input and output file paths
INPUT_FILE="example.md"
OUTPUT_FILE="output.html"

# Execute the Pandoc command for the single file
$PANDOC_CMD -o "$OUTPUT_FILE" "$INPUT_FILE"

```

## Exercise 2: Batch Conversion

### Assignment:
Extend the script from Exercise 1 to perform batch conversion for all Markdown files in the markdown_files directory. Output the HTML files to a new directory named html_output.

### Hints:

- Use a for loop to iterate over all Markdown files in the directory.
- Create the ``html_output`` directory if it doesn't exist.

### Solution:

```
#!/bin/bash

# Set the Pandoc command with your desired options
PANDOC_CMD="pandoc --from markdown --to html5 --mathjax --bibliography=ref.bib"

# Input and output directories
INPUT_DIR="markdown_files"
OUTPUT_DIR="html_output"

# Create the output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Iterate over all Markdown files in the input directory
for file in "$INPUT_DIR"/*.md; do
    # Extract the filename without the extension
    filename=$(basename -- "$file")
    filename_noext="${filename%.*}"

    # Execute the Pandoc command for each file
    $PANDOC_CMD -o "$OUTPUT_DIR/$filename_noext.html" "$file"
done
```

## Exercise 3: Customizing Conversion Options

### Assignment:
Modify the script from Exercise 2 to allow users to customize the Pandoc options. Prompt the user to input the desired options (e.g., ``--toc`` for table of contents).

### Hints:

- Use the read command to get user input.
- Include the user-specified options in the Pandoc command.

```
#!/bin/bash

# Prompt the user to input Pandoc options
echo "Enter Pandoc options (e.g., --toc):"
read pandoc_options

# Set the Pandoc command with user-specified options
PANDOC_CMD="pandoc $pandoc_options --from markdown --to html5 --mathjax --bibliography=ref.bib"

# Input and output directories
INPUT_DIR="markdown_files"
OUTPUT_DIR="html_output"

# Create the output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Iterate over all Markdown files in the input directory
for file in "$INPUT_DIR"/*.md; do
    # Extract the filename without the extension
    filename=$(basename -- "$file")
    filename_noext="${filename%.*}"

    # Execute the Pandoc command for each file
    $PANDOC_CMD -o "$OUTPUT_DIR/$filename_noext.html" "$file"
done
```

## Exercise 4: Handling Input Directories

### Assignment:
Enhance the script from Exercise 3 to accept the input directory as a command-line argument. If no argument is provided, default to the current directory.

### Hints:

- Use ``$1`` to access the first command-line argument.
- Use a default value if no argument is provided.

### Solution:

```
#!/bin/bash

# Set the Pandoc command with your desired options
PANDOC_CMD="pandoc --from markdown --to html5 --mathjax --bibliography=ref.bib"

# Input directory (default to current directory if not provided)
INPUT_DIR="${1:-.}"
OUTPUT_DIR="html_output"

# Create the output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Iterate over all Markdown files in the input directory
for file in "$INPUT_DIR"/*.md; do
    # Extract the filename without the extension
    filename=$(basename -- "$file")
    filename_noext="${filename%.*}"

    # Execute the Pandoc command for each file
    $PANDOC_CMD -o "$OUTPUT_DIR/$filename_noext.html" "$file"
done
```

## Exercise 5: Advanced Conversion

### Assignment:
Create a script named *advanced_converter.sh* that performs the following:

Converts all Markdown files in the content directory to HTML with Pandoc.
Inserts a custom CSS file (styles.css) for styling.
Uses a template file (template.html) for the HTML output.

### Hints:

- Consider using the ``--css`` and ``--template`` options in the Pandoc command.
- Make sure to handle the existence of the CSS and template files.

### Solution:

```
#!/bin/bash

# Set the Pandoc command with your desired options
PANDOC_CMD="pandoc --from markdown --to html5 --mathjax --bibliography=ref.bib"

# Input and output directories
INPUT_DIR="content"
OUTPUT_DIR="html_output"

# Custom CSS and template files
CSS_FILE="styles.css"
TEMPLATE_FILE="template.html"

# Create the output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Iterate over all Markdown files in the input directory
for file in "$INPUT_DIR"/*.md; do
    # Extract the filename without the extension
    filename=$(basename -- "$file")
    filename_noext="${filename%.*}"

    # Execute the Pandoc command for each file with custom CSS and template
    $PANDOC_CMD --css "$CSS_FILE" --template "$TEMPLATE_FILE" -o "$OUTPUT_DIR/$filename_noext.html" "$file"
done
```

You can extend these scripts, exploring additional Pandoc options and Bash scripting techniques.

