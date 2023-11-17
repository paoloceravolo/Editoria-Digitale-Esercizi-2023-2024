import yaml
import csv

def read_yaml_file(file_path):
    with open(file_path, 'r') as file:
        yaml_data = yaml.safe_load(file)
    return yaml_data

def yaml_to_csv(yaml_data, output_csv_path):
    # Extract header from the first item in the YAML data
    #print(yaml_data.keys())
    header = list(yaml_data.keys())
    #yaml_data_values = list(yaml_data.values())
    #print(yaml_data)

    with open(output_csv_path, 'w', newline='') as csvfile:
        # Create a CSV writer and write the header
        csv_writer = csv.DictWriter(csvfile, fieldnames=header)
        csv_writer.writeheader()

        # Write the dictioanry of YAML data into CSV rows
        csv_writer.writerow(yaml_data)


if __name__ == "__main__":
    # Replace 'your_yaml_file.yaml' with the path to your YAML file
    input_yaml_path = 'metadata.yaml'

    # Replace 'output_csv_file.csv' with the desired output path for CSV
    output_csv_path = 'metadata.csv'

    # Read YAML data from file
    yaml_data = read_yaml_file(input_yaml_path)

    # Convert YAML to CSV
    yaml_to_csv(yaml_data, output_csv_path)

    print(f"Conversion complete. CSV data written to {output_csv_path}")
