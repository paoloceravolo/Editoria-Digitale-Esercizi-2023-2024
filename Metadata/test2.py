def flatten_structure(data):
    if isinstance(data, dict):
        # Se il dizionario ha una sola chiave e il valore è una lista, estrai gli elementi della lista
        if len(data) == 1 and isinstance(list(data.values())[0], list):
            return flatten_structure(list(data.values())[0])
        # Altrimenti, applica la funzione ricorsivamente ai valori del dizionario
        else:
            return {key: flatten_structure(value) for key, value in data.items()}
    elif isinstance(data, list):
        # Se la lista contiene un solo elemento di tipo dizionario, estrai quel dizionario
        if len(data) == 1 and isinstance(data[0], dict):
            return flatten_structure(data[0])
        # Altrimenti, applica la funzione ricorsivamente a ciascun elemento della lista
        else:
            return [flatten_structure(item) for item in data]
    else:
        return data

# La tua struttura dati
data = {'schema.org': [{'@type': 'Book'}, {'additionalType': 'Product'}, {'name': 'titolo'}, {'author': 'Paolo Ceravolo'}, {'inLanguage': 'it'}, {'offers': [{'@type': 'Offer'}, {'availability': 'https://unimi.primo.exlibrisgroup.com/permalink/39UMI_INST/i9q3jt/alma991015614449706031'}, {'serialNumber': 991015614449706031}, {'offeredBy': [{'@type': 'Library'}, {'@id': 'https://sites.unimi.it/dcb/pub/opac/usm_a5_info.html'}, {'name': 'Biblioteca Biomedica di Città Studi'}]}]}], 'date': '03 novembre 2023', 'bibliography': 'ref.bib', 'csl': 'IEEE.csl'}

# Applica la funzione per semplificare la struttura
flattened_data = flatten_structure(data)

# Stampa la struttura semplificata
print(flattened_data)
