#!/bin/bash

if [ $# -lt 1 ]
	then
	echo "No arguments supplied. Please provide the path to a markdown file"
		exit 1
fi

input_file=$1
	output_file="${input_file%.*}.epub"

# Default values for options
epub_version="3.0"
toc_level=2

# Parse command-line options
while [[ $# -gt 1 ]]
do
key="$1"

case $key in
    -e|--epub-version)
    epub_version="$2"
    shift # past argument
    ;;
    -t|--toc-level)
    toc_level="$2"
    shift # past argument
    ;;
    *)
          # unknown option
    ;;
esac
shift # past argument or value
done

pandoc $input_file -o $output_file --epub-version=$epub_version --toc --toc-depth=$toc_level --include-in-header header.tex --epub-metadata=metadata.xml --epub-cover-image=cover.jpg

echo "EPUB file created successfully: $output_file"