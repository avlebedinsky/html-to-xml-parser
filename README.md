# HTML to XML Parser

A Python tool for converting HTML files to XML format with specific tag extraction.

## Features
- Extracts paragraphs containing annotation tags
- Supports different encodings
- Pretty print XML output
- Auto-generated output filenames

## Installation

To get started, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd html-to-xml-parser
pip install -r requirements.txt
```

## Usage
```bash
python src/main.py <html_file> [output_file]
```

## Running Tests

To ensure everything is working correctly, you can run the unit tests included in the project:

```bash
python -m unittest discover -s tests
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.