import yaml

def yaml_to_html_microdata(yaml_data):
    html = "<!DOCTYPE html>\n<html>\n<head>\n</head>\n<body>\n"

    #for item in yaml_data.items():    
    for key, value in yaml_data.items():
        html += "<div itemscope itemtype='http://schema.org/Product'>\n"
        html += f"  <span itemprop='{key}'>{value}</span><br>\n"
    html += "</div>\n"

    html += "</body>\n</html>"

    return html

if __name__ == "__main__":
    # Replace 'your_yaml_file.yaml' with the path to your YAML file
    input_yaml_path = 'metadata.yaml'

    # Replace 'output_html_file.html' with the desired output path for HTML
    output_html_path = 'metadata.html'

    # Read YAML data from file
    with open(input_yaml_path, 'r') as file:
        yaml_data = yaml.safe_load(file)
        print(yaml_data.items())

    # Convert YAML to HTML with Microdata
    html_content = yaml_to_html_microdata(yaml_data)

    # Write HTML content to file
    with open(output_html_path, 'w') as file:
        file.write(html_content)

    print(f"Conversion complete. HTML with Microdata written to {output_html_path}")