#!/usr/bin/env python3

"""
Remove all horizontal rules from a markdown document.  
"""

from panflute import *


def filter_horizontal_rules(elem, doc):
    if isinstance(elem, HorizontalRule):
        # Return None to remove the horizontal rule element
        return []


def main(doc=None):
    return run_filter(filter_horizontal_rules, doc=doc)


if __name__ == '__main__':
    main()