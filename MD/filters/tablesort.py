#!/usr/bin/env python3

"""
"""

from panflute import *

def table_sort(elem, doc):
    if isinstance(elem, Table):
        # Specify the column number to sort by (zero-based index)
        column_to_sort = 2  # Change this to the desired column
        # Specify the sort order ('asc' for ascending, 'desc' for descending)
        sort_order = 'asc'  # Change this as needed

        # Get the table's header row
        header_row = elem.content[0]

        # Get the data rows to sort (skip the header row)
        data_rows = elem.content[1:]

         # Convert data_rows from list to TableBody
        table_body = TableBody(*data_rows)

        # Sort the data rows based on the selected column
        sorted_rows = sorted(table_body.content, key=lambda row: row.content[column_to_sort].text)

        if sort_order == 'desc':
            sorted_rows = list(reversed(sorted_rows))


        # Reconstruct the table with the sorted data rows
        #sorted_table = [header_row] + data_rows

        #head = TableHead(header_row)
        #rows = TableRow(data_rows)
        #body = TableBody(rows)
        caption = 'sorted table'
        #sorted_table = Table(data_rows, head=header_row, caption=caption)
        # Reconstruct the table with the sorted data rows
        sorted_table = Table(*[header_row, TableBody(*sorted_rows)])
        # Return the sorted table
        return sorted_table

        #div = Div(*sorted_table)
        #div = div.append(*sorted_table)
        #return div

def main(doc=None):
    return run_filter(table_sort, doc=doc)


if __name__ == '__main__':
    main()