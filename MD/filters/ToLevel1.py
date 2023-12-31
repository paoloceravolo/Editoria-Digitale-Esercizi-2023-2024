#!/usr/bin/env python3

"""
Set all headers to level 1
"""

from panflute import *

def action(elem, doc):
    if isinstance(elem, Header):
        elem.level = 1

def main(doc=None):
    return run_filter(action, doc=doc) 

if __name__ == '__main__':
    main()