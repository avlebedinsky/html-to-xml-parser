# HTML to XML Parser

This project provides a simple parser that converts HTML documents into well-formed XML. It utilizes the BeautifulSoup library for parsing HTML and lxml for generating XML.

## Features

- Parses HTML content and converts it to XML format.
- Handles various HTML structures and ensures valid XML output.

## Installation

To get started, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd html-to-xml-parser
pip install -r requirements.txt
```

## Usage

To run the parser, execute the following command:

```bash
python src/main.py
```

You will be prompted to enter the HTML content you wish to convert to XML.

## Running Tests

To ensure everything is working correctly, you can run the unit tests included in the project:

```bash
python -m unittest discover -s tests
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.