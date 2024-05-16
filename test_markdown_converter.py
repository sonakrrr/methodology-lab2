import unittest
import os
from convert_markdown import MarkdownConverter

class TestMarkdownConverter(unittest.TestCase):

    def setUp(self):
        self.input_file = 'input_text.md'
        self.html_output = '''<p>Lab1 "Git Basics"</p>
<p><tt>Convert</tt> <b>markdown</b> 
to <i>html</i></p>
<p><pre>
Made by 
        Sofiia Krytska 
                       group IM-21
</pre></p>'''
        self.text_output = '''Lab1 "Git Basics"\n\nConvert markdown \nto html\n\nMade by \n        Sofiia Krytska \n                       group IM-21\n'''

    def test_convert_to_html(self):
        converter = MarkdownConverter(self.input_file)
        html_output = converter.convert_to_html()
        self.assertMultiLineEqual(html_output, self.html_output)

    def test_convert_to_text_without_ansi(self):
        converter = MarkdownConverter(self.input_file)
        text_output = converter.convert_to_text(use_ansi=True)
        self.assertMultiLineEqual(text_output, self.text_output)

if __name__ == '__main__':
    unittest.main()
