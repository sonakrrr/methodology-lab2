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
        self.apply_preformatted('html')
        self.apply_bold('html')
        self.apply_italic('html')
        self.apply_monospaced('html')
        self.apply_paragraphs('html')
        return f"<p>{self.markdown_content}</p>"

    def convert_to_text(self, use_ansi):
        self.apply_preformatted('text', use_ansi)
        self.apply_bold('text', use_ansi)
        self.apply_italic('text', use_ansi)
        self.apply_monospaced('text', use_ansi)
        self.apply_paragraphs('text')
        return self.markdown_content

    def apply_bold(self, format_type, use_ansi=False):
        if format_type == 'html':
            self.markdown_content = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', self.markdown_content)
        elif format_type == 'text':
            if use_ansi:
                self.markdown_content = re.sub(r'\*\*(.*?)\*\*', r'\033[1m\1\033[22m', self.markdown_content)
            else:
                self.markdown_content = re.sub(r'\*\*(.*?)\*\*', r'\1', self.markdown_content)

    def apply_italic(self, format_type, use_ansi=False):
        if format_type == 'html':
            self.markdown_content = re.sub(r'_([^_]+)_', r'<i>\1</i>', self.markdown_content)
        elif format_type == 'text':
            if use_ansi:
                self.markdown_content = re.sub(r'_([^_]+)_', r'\033[3m\1\033[23m', self.markdown_content)
            else:
                self.markdown_content = re.sub(r'_([^_]+)_', r'\1', self.markdown_content)

    def apply_monospaced(self, format_type, use_ansi=False):
        if format_type == 'html':
            self.markdown_content = re.sub(r'`([^`]+)`', r'<tt>\1</tt>', self.markdown_content)
        elif format_type == 'text':
            if use_ansi:
                self.markdown_content = re.sub(r'`([^`]+)`', r'\033[7m\1\033[27m', self.markdown_content)
            else:
                self.markdown_content = re.sub(r'`([^`]+)`', r'\1', self.markdown_content)

    def apply_preformatted(self, format_type, use_ansi=False):
        if format_type == 'html':
            self.markdown_content = re.sub(r'```(.*?)```', r'<pre>\1</pre>', self.markdown_content, flags=re.DOTALL)
        elif format_type == 'text':
            if use_ansi:
                self.markdown_content = re.sub(r'```(.*?)```', r'\033[7m\1\033[27m', self.markdown_content, flags=re.DOTALL)
            else:
                self.markdown_content = re.sub(r'```(.*?)```', r'\1', self.markdown_content, flags=re.DOTALL)

    def apply_paragraphs(self, format_type):
        if format_type == 'html':
            self.markdown_content = re.sub(r'(?<=\S)\n{2,}(?=\S)|\n\n(?=\S)', r'</p>\n<p>', self.markdown_content)
        elif format_type == 'text':
            self.markdown_content = re.sub(r'(?<=\S)\n{2,}(?=\S)|\n\n(?=\S)', r'\n\n', self.markdown_content)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_markdown.py <input_file> [--out <output_file>] [--format <html|text>] [--ansi]")
        sys.exit(1)

    input_text_file = sys.argv[1]
    output_text_file = None
    format_type = 'html'  # Default format
    use_ansi = '--ansi' in sys.argv

    if '--out' in sys.argv:
        out_index = sys.argv.index('--out')
        if len(sys.argv) > out_index + 1:
            output_text_file = sys.argv[out_index + 1]

    if '--format' in sys.argv:
        format_index = sys.argv.index('--format')
        if len(sys.argv) > format_index + 1:
            format_type = sys.argv[format_index + 1]
            if format_type not in ['html', 'text']:
                print("Error: Unsupported format. Use 'html' or 'text'.")
                sys.exit(1)

    converter = MarkdownConverter(input_text_file)

    if format_type == 'html':
        output_content = converter.convert_to_html()
    else:
        output_content = converter.convert_to_text(use_ansi)

    if output_text_file:
        with open(output_text_file, 'w', encoding='utf-8') as f:
            f.write(output_content)
    else:
        print(output_content)
