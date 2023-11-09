#!/usr/bin/env python3

"""
Appling the filter to renumber the numbered lists with Roman numerals, and save the modified document 
"""

from panflute import *

def filter_renumber_roman(elem, doc):
    if isinstance(elem, OrderedList):
        # Create a new ordered list with Roman numerals
        roman_list = OrderedList()
        roman_list.style = 'UpperRoman'
        # Copy the contents of the original list
        roman_list.content = elem.content
        # Return the new list
        return roman_list


def main(doc=None):
    return run_filter(filter_renumber_roman, doc=doc)


if __name__ == '__main__':
    main()