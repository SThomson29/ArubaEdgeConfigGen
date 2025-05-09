# Import required libraries
import os, yaml
from jinja2 import Environment, FileSystemLoader

# Function to render a Jinja2 template with provided seed data as a string
def render_template(template: os.PathLike, seed: dict) -> str:
    """Render a given template with seed data

    Args:
        template (os.PathLike): Path to template file
        seed (dict): Seed data

    Returns:
        str: Rendered output
    """
    # Get directory of provided template path
    template_directory = os.path.dirname(template)
    # Create a jinja env using the folder
    jinja_env = Environment(loader=FileSystemLoader(template_directory))

    # Render template with jinja
    this_template = jinja_env.get_template(os.path.basename(template))
    return this_template.render(seed)

# Function to list all files in a directory
def list_files(directory: os.PathLike) -> list:
    """List all files in a directory

    Args:
        directory (os.PathLike): Directory to list files from

    Returns:
        list: List of file paths
    """
    return [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

# List all files in the switches directory with correct format of .yaml
switch_list = []
for files in list_files('switches/'):
        if files.endswith('.yaml'):
            switch_list.append(files)

# Set the directory for the seed data
seed_loc=os.path.relpath('switches/','./')

# Loop through each file in the switch_list to process it and generate the config
for switches in switch_list:
    # Load the seed data from a YAML file  
    with open(switches) as f:
        seed = yaml.safe_load(f)

    # Set the directory for template generation 
    rel_directory=os.path.relpath('configs/','./')

    # Combine the template and seed data to generate the config
    config_return = render_template("config-template.j2",seed)

    # Dynamically name the output file based on the YAML file name
    base_name = os.path.splitext(os.path.basename(switches))[0]  # Extract base name without extension
    output_file = os.path.join(rel_directory, f"{base_name}.ios")  # Add .ios extension
    # Outputs file with format switchname.ios 
    with open(output_file, 'w') as f:
        f.write(config_return)
