# Aruba CX Config Generator

## Overview
The ArubaEdge Config Generator is a tool designed to simplify the creation of Aruba CX configurations using Jinja2 templates. It allows users to generate consistent and reusable configurations for Aruba CX devices, with a focus on access switching.

## Features
- **Template-based Configuration**: Use Jinja2 template to define reusable configuration patterns.
- **Dynamic Variables**: Populate templates with dynamic data for customized configurations.
- **Automation Ready**: Easily integrate with automation workflows.

## Requirements
- Python 3.7 or higher
- Jinja2 library
- Pyyaml library
  
## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/SThomson29/ArubaEdgeConfigGen
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Use the provided template `config-template.j2` and modify as required. If you are more experienced feel free to create your own. You can look at the existing template for guidance. 
2. Provide input data in YAML format in the directory called switches. There are some yaml examples within the main folder. You can check your yaml is correctly formatted using https://www.yamllint.com/
3. Run the generator:
    ```bash
    python config-gen.py 
    ```
4. The generated configuration will be saved in the `Configs/` directory formated as a .ios type file. 

## Example
```bash
python config-gen.py
```

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any bugs or feature requests.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
For questions or support, please contact sam.thomson.1991@gmail.com
