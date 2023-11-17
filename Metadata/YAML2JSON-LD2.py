import yaml
import json

def flatten(metadata_list):
    flattened_metadata = {}
    for item in metadata_list:
        if isinstance(item, dict):
            flattened_metadata.update(item)
    return flattened_metadata

def read_yaml_file(file_path):
    with open(file_path, 'r') as file:
        yaml_data = yaml.safe_load(file)
    return yaml_data

def yaml_to_jsonld(input_file, output_file):    
    metadata =  read_yaml_file(input_file)
    print(metadata)
    metadata_schema = {}

    # Assuming metadata is inside a list called 'metadata'
    if 'schema.org' in metadata and isinstance(metadata['schema.org'], list):
        metadata_schema = metadata['schema.org']
        #print(metadata_schema)
        # Insert the values of the element schema.org in a dictionary
        flattened_metadata = flatten(metadata_schema)
        print(flattened_metadata)


    # Create a base structure for JSON-LD with Schema.org context
    # **json_fragment_valid sta effettuando l'unpacking della lista metadata_list all'interno del dizionario jsonld_data. Questo significa che i valori della lista metadata_list verranno aggiunti come coppie chiave-valore al dizionario jsonld_data.
    jsonld_data = {
        "@context": "http://schema.org/", **flattened_metadata
    }

    # Generate output file
    with open(output_file, 'w') as jsonld_file:
        json.dump(jsonld_data, jsonld_file, indent=2)

if __name__ == "__main__":
    input_yaml_file = 'input.yaml'  # Replace with the path to your input YAML file
    output_jsonld_file = 'output.jsonld'  # Replace with the desired output JSON-LD file path

    yaml_to_jsonld(input_yaml_file, output_jsonld_file)