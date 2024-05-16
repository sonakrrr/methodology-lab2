import re
import sys

class MarkdownConverter:
    def __init__(self, input_text_file):
        self.input_text_file = input_text_file
        self.markdown_content = self.read_markdown_content()

    def read_markdown_content(self):
        try:
            with open(self.input_text_file, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print(f"Error: File '{self.input_text_file}' not found.")
            sys.exit(1)
        except Exception as E:
            print(f"Error: {E}")
            sys.exit(1)

    def convert_to_html(self):
        self.apply_preformatted()
        self.apply_bold()
        self.apply_italic()
        self.apply_monospaced()
        self.apply_paragraphs()
        return f"<p>{self.markdown_content}</p>"

    def apply_bold(self):
        self.markdown_content = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', self.markdown_content)

    def apply_italic(self):
        self.markdown_content = re.sub(r'_([^_]+)_', r'<i>\1</i>', self.markdown_content)

    def apply_monospaced(self):
        self.markdown_content = re.sub(r'`([^`]+)`', r'<tt>\1</tt>', self.markdown_content)

    def apply_preformatted(self):
        self.markdown_content = re.sub(r'```(.*?)```', r'<pre>\1</pre>', self.markdown_content, flags=re.DOTALL)

    def apply_paragraphs(self):
        self.markdown_content = re.sub(r'(?<=\S)\n{2,}(?=\S)|\n\n(?=\S)', r'</p>\n<p>', self.markdown_content)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_markdown.py <input_file> [--out <output_file>]")
        sys.exit(1)

    input_text_file = sys.argv[1]
    output_text_file = None

    if len(sys.argv) > 2 and sys.argv[2] == "--out" and len(sys.argv) > 3:
        output_text_file = sys.argv[3]

    converter = MarkdownConverter(input_text_file)
    html_text = converter.convert_to_html()

    if output_text_file:
        with open(output_text_file, 'w', encoding='utf-8') as f:
            f.write(html_text)
    else:
        print(html_text)