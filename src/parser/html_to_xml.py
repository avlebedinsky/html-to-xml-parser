from bs4 import BeautifulSoup
import chardet

class HtmlToXmlParser:
    def __init__(self):
        self.pretty_print = True

    def set_pretty_print(self, enabled: bool):
        self.pretty_print = enabled

    def parse_html(self, html_file):
        try:
            # Определяем кодировку файла
            with open(html_file, 'rb') as f:
                raw_data = f.read()
            detected = chardet.detect(raw_data)
            encoding = detected['encoding'] or 'utf-8'

            # Читаем файл с определенной кодировкой
            content = raw_data.decode(encoding)
            
            # Используем html.parser
            soup = BeautifulSoup(content, 'html.parser')
            
            # Находим все теги p, содержащие span с словом "Аннотация"
            valid_p_tags = []
            for span in soup.find_all('span'):
                if span.string and 'Аннотация' in span.string:
                    p_parent = span.find_parent('p')
                    if p_parent:
                        valid_p_tags.append(p_parent)
            
            # Создаем результирующий XML
            result = ['<?xml version="1.0" encoding="UTF-8"?>']
            if valid_p_tags:
                result.append('<root>')
                for p_tag in valid_p_tags:
                    tag_str = str(p_tag)
                    if tag_str and tag_str.strip():
                        result.append(tag_str)
                result.append('</root>')
            else:
                result.append('<root/>')
            
            # Собираем финальную строку
            xml_str = '\n'.join(result)
            
            if self.pretty_print:
                try:
                    formatted_soup = BeautifulSoup(xml_str, 'xml')
                    pretty_xml = formatted_soup.prettify()
                    if pretty_xml:
                        return pretty_xml
                except:
                    pass
            return xml_str
            
        except Exception as e:
            raise Exception(f"Failed to parse HTML: {str(e)}")
