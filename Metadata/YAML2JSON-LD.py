import yaml
import json

def yaml_to_jsonld(yaml_data):
    # Create a base structure for JSON-LD with Schema.org context
    jsonld_data = {
        "@context": "http://schema.org/",
        "@type": "Book",  # You can change this based on your specific Schema.org type
    }

    # Update JSON-LD data with YAML content
    jsonld_data.update(yaml_data)

    return jsonld_data

def read_yaml_file(file_path):
    with open(file_path, 'r') as file:
        yaml_data = yaml.safe_load(file)
    return yaml_data

def write_jsonld_file(jsonld_data, output_path):
    with open(output_path, 'w') as file:
        json.dump(jsonld_data, file, indent=2)

if __name__ == "__main__":
    # Replace 'your_yaml_file.yaml' with the path to your YAML file
    input_yaml_path = 'metadata.yaml'

    # Replace 'output_jsonld_file.json' with the desired output path for JSON-LD
    output_jsonld_path = 'metadata.json'

    # Read YAML data from file
    yaml_data = read_yaml_file(input_yaml_path)
    print(yaml_data)

    # Convert YAML to JSON-LD
    jsonld_data = yaml_to_jsonld(yaml_data)

    # Write JSON-LD data to file
    write_jsonld_file(jsonld_data, output_jsonld_path)

    print(f"Conversion complete. JSON-LD data written to {output_jsonld_path}")
