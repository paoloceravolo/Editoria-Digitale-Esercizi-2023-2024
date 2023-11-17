import sys
import yaml

def yaml_to_html_microdata(yaml_data):
    # Create a string for the Microdata in the head section
    head_microdata = ""
    for key, value in yaml_data.items():
        head_microdata += f'<meta itemprop="{key}" content="{value}">\n'

    # Create the HTML body content
    body_content = "<div itemscope itemtype='http://schema.org/Product'>\n"
    for key, value in yaml_data.items():
        body_content += f"  <span itemprop='{key}'>{value}</span><br>\n"
    body_content += "</div>"

    # Combine the head and body content into a complete HTML document
    html = f"<!DOCTYPE html>\n<html>\n<head>\n{head_microdata}</head>\n<body>\n{body_content}\n</body>\n</html>"

    return html

if __name__ == "__main__":
    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python script.py input_yaml_path output_html_path")
        sys.exit(1)

    # Input and output paths from command line arguments
    input_yaml_path = sys.argv[1]
    output_html_path = sys.argv[2]

    # Read YAML data from file
    with open(input_yaml_path, 'r') as file:
        yaml_data = yaml.safe_load(file)

    # Convert YAML to HTML with Microdata
    html_content = yaml_to_html_microdata(yaml_data)

    # Write HTML content to file
    with open(output_html_path, 'w') as file:
        file.write(html_content)

    print(f"Conversion complete. HTML with Microdata in head written to {output_html_path}")
