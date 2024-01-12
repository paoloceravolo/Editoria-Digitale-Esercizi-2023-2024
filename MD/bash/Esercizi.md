# Esercizi: automatizzare le trasformazioni Pandoc da Shell

A set of five exercises that progressively introduce to Bash scripting for automating Pandoc transformations. Each exercise builds on the previous one, gradually increasing in complexity.

## Exercise 1: Basic Conversion

### Assignment:
Write a Bash script named *convert_to_html.sh* that converts a single Markdown file to HTML using Pandoc. Ensure that the output HTML file is named output.html.

### Hints:

- Use a variable to store the Pandoc command with appropriate options.
- Specify the input and output file paths in the script.

## Exercise 2: Batch Conversion

### Assignment:
Extend the script from Exercise 1 to perform batch conversion for all Markdown files in the markdown_files directory. Output the HTML files to a new directory named html_output.

### Hints:

- Use a for loop to iterate over all Markdown files in the directory.
- Create the ``html_output`` directory if it doesn't exist.

## Exercise 3: Customizing Conversion Options

### Assignment:
Modify the script from Exercise 2 to allow users to customize the Pandoc options. Prompt the user to input the desired options (e.g., ``--toc`` for table of contents).

### Hints:

- Use the read command to get user input.
- Include the user-specified options in the Pandoc command.

## Exercise 4: Handling Input Directories

### Assignment:
Enhance the script from Exercise 3 to accept the input directory as a command-line argument. If no argument is provided, default to the current directory.

### Hints:

- Use ``$1`` to access the first command-line argument.
- Use a default value if no argument is provided.

## Exercise 5: Advanced Conversion

### Assignment:
Create a script named *advanced_converter.sh* that performs the following:

Converts all Markdown files in the content directory to HTML with Pandoc.
Inserts a custom CSS file (styles.css) for styling.
Uses a template file (template.html) for the HTML output.

### Hints:

- Consider using the ``--css`` and ``--template`` options in the Pandoc command.
- Make sure to handle the existence of the CSS and template files.

You can extend these scripts, exploring additional Pandoc options and Bash scripting techniques.

