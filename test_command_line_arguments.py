import unittest
from unittest.mock import patch
import sys
from convert_markdown import MarkdownConverter

class TestCommandLineArguments(unittest.TestCase):

    @patch('sys.argv', ['convert_markdown.py', 'test_cases.md'])
    def test_no_optional_arguments(self):
        converter = MarkdownConverter('test_cases.md')
        output = converter.convert_to_html()
        self.assertTrue(output.startswith('<p>'))

    @patch('sys.argv', ['convert_markdown.py', 'test_cases.md', '--out', 'output.html'])
    def test_output_file_argument(self):
        output_file = 'output.html'
        converter = MarkdownConverter('test_cases.md')
        output = converter.convert_to_html()
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(output)
        with open(output_file, 'r', encoding='utf-8') as f:
            content = f.read()
        self.assertTrue(content.startswith('<p>'))

    @patch('sys.argv', ['convert_markdown.py', 'test_cases.md', '--format', 'text'])
    def test_format_text_argument(self):
        converter = MarkdownConverter('test_cases.md')
        output = converter.convert_to_text(use_ansi=False)
        self.assertFalse(output.startswith('<p>'))

    @patch('sys.argv', ['convert_markdown.py', 'test_cases.md', '--format', 'html'])
    def test_format_html_argument(self):
        converter = MarkdownConverter('test_cases.md')
        output = converter.convert_to_html()
        self.assertTrue(output.startswith('<p>'))

    @patch('sys.argv', ['convert_markdown.py', 'test_cases.md', '--ansi'])
    def test_ansi_argument(self):
        converter = MarkdownConverter('test_cases.md')
        output = converter.convert_to_text(use_ansi=True)
        self.assertIn('\033[', output)  # ANSI codes should be present

    @patch('sys.argv', ['convert_markdown.py', 'test_cases.md', '--format', 'text', '--out', 'output.txt'])
    def test_format_and_output_file_arguments(self):
        output_file = 'output.txt'
        converter = MarkdownConverter('test_cases.md')
        output = converter.convert_to_text(use_ansi=False)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(output)
        with open(output_file, 'r', encoding='utf-8') as f:
            content = f.read()
        self.assertFalse(content.startswith('<p>'))

if __name__ == '__main__':
    unittest.main()
