import unittest
from src.parser.html_to_xml import HtmlToXmlParser

class TestHtmlToXmlParser(unittest.TestCase):

    def setUp(self):
        self.parser = HtmlToXmlParser()

    def test_parse_html(self):
        html_input = "<div><p>Hello, World!</p></div>"
        expected_output = "<div><p>Hello, World!</p></div>"  # Adjust based on actual expected output
        result = self.parser.parse_html(html_input)
        self.assertEqual(result, expected_output)

    def test_convert_to_xml(self):
        html_input = "<div><p>Hello, World!</p></div>"
        xml_output = self.parser.parse_html(html_input)
        expected_xml = "<root><div><p>Hello, World!</p></div></root>"  # Adjust based on actual expected output
        result = self.parser.convert_to_xml(xml_output)
        self.assertEqual(result, expected_xml)

if __name__ == '__main__':
    unittest.main()