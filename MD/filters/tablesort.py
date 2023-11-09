#!/usr/bin/env python3

"""
Appling the filter to renumber the numbered lists with Roman numerals, and save the modified document 
"""

from panflute import *

def table_sort(elem, doc):
    if isinstance(elem, Table):
        # Specify the column number to sort by (zero-based index)
        column_to_sort = 1  # Change this to the desired column
        # Specify the sort order ('asc' for ascending, 'desc' for descending)
        sort_order = 'asc'  # Change this as needed

        # Get the table's header row
        header_row = elem.content[0]

        # Get the data rows to sort (skip the header row)
        data_rows = elem.content[1:]

        # Sort the data rows based on the selected column
        data_rows.sort(key=lambda row: row.content[column_to_sort].text)

        if sort_order == 'desc':
            data_rows = list(reversed(data_rows))

        # Reconstruct the table with the sorted data rows
        sorted_table = [header_row] + data_rows

        # Return the sorted table
        return Div(*sorted_table)

def main(doc=None):
    return run_filter(table_sort, doc=doc)


if __name__ == '__main__':
    main()