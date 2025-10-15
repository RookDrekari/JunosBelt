import yaml

def parse_yaml(file_path):
    with open(file_path, 'r') as f:
        data = yaml.safe_load(f)
    return data

if __name__ == "__main__":
    file_path = "./data/mechanics/recipes.yaml"
    try:
        parsed = parse_yaml(file_path)
        print(parsed)
    except Exception as e:
        print(f"Error parsing YAML: {e}")
