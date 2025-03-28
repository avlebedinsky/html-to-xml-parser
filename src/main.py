import sys
import os
from parser.html_to_xml import HtmlToXmlParser
from datetime import datetime

def generate_output_filename(html_file):
    base_name = os.path.splitext(os.path.basename(html_file))[0]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{base_name}_{timestamp}.xml"

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <html_file> [output_file]")
        print("Example: python main.py test.html output.xml")
        print("\nIf output_file is not specified, XML will be saved with auto-generated name")
        sys.exit(1)

    html_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else generate_output_filename(html_file)
    parser = HtmlToXmlParser()

    if not os.path.exists(html_file):
        print(f"Error: HTML file '{html_file}' not found")
        sys.exit(1)

    try:
        xml_output = parser.parse_html(html_file)
        try:
            output_dir = os.path.dirname(output_file)
            if output_dir and not os.path.exists(output_dir):
                os.makedirs(output_dir)
                
            with open(output_file, 'w', encoding='utf-8', newline='') as f:
                f.write(xml_output)
            print(f"XML saved to {output_file}")
        except (IOError, PermissionError) as e:
            print(f"Error saving XML file: {e}")
            sys.exit(1)
    except TypeError as e:
        if "pretty_print" in str(e):
            try:
                parser.set_pretty_print(False)
                xml_output = parser.parse_html(html_file)
                with open(output_file, 'w', encoding='utf-8', newline='') as f:
                    f.write(xml_output)
                print(f"XML saved to {output_file} (without pretty print)")
            except Exception as inner_e:
                print(f"Error parsing HTML: {str(inner_e)}")
                sys.exit(1)
        else:
            print(f"Error parsing HTML: {str(e)}")
            sys.exit(1)
    except Exception as e:
        print(f"Error parsing HTML: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()