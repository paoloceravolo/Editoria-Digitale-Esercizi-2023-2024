import json

# La tua struttura dati
data = {'schema.org': [{'\\@type': 'Book'}, {'additionalType': 'Product'}, {'name': 'titolo'}, {'author': 'Paolo Ceravolo'}, {'inLanguage': 'it'}, {'offers': [{'\\@type': 'Offer'}, {'availability': 'https://unimi.primo.exlibrisgroup.com/permalink/39UMI_INST/i9q3jt/alma991015614449706031'}, {'serialNumber': 991015614449706031}, {'offeredBy': [{'\\@type': 'Library'}, {'\\@id': 'https://sites.unimi.it/dcb/pub/opac/usm_a5_info.html'}, {'name': 'Biblioteca Biomedica di Città Studi'}]}]}], 'date': '03 novemebre 2023', 'bibliography': 'ref.bib', 'csl': 'IEEE.csl'}

# Rimuovi i caratteri di escape
json_data = json.dumps(data).replace('\\\\@', '@')

# Parsa la stringa JSON
parsed_data = json.loads(json_data)

# Stampa la struttura dati parsata
print(parsed_data)