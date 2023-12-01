#!/bin/bash

pandoc "$1" \
-f gfm \
--include-in-header header.tex \
--highlight-style kate \
--metadata title=\'Prova\' \
-V linkcolor:blue \
-V geometry:a4paper \
-V geometry:margin=2cm \
-V mainfont="Palatino" \
-V monofont="Courier" \
-V fontsize=12pt \
--pdf-engine=xelatex \
--toc \
--toc-depth 2 \
--epub-cover-image cover.jpg \
-o "$2"