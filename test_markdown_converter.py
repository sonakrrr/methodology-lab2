import unittest
from convert_markdown import MarkdownConverter

class TestMarkdownConverter(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_file = 'test_cases.md'
        cls.converter = MarkdownConverter(cls.test_file)

    def test_bold_html(self):
        self.converter.markdown_content = "**bold text**"
        self.converter.apply_bold('html')
        self.assertEqual(self.converter.markdown_content, "<b>bold text</b>")

    def test_bold_text(self):
        self.converter.markdown_content = "**bold text**"
        self.converter.apply_bold('text', use_ansi=False)
        self.assertEqual(self.converter.markdown_content, "bold text")

    def test_bold_text_ansi(self):
        self.converter.markdown_content = "**bold text**"
        self.converter.apply_bold('text', use_ansi=True)
        self.assertEqual(self.converter.markdown_content, "\033[1m" + "bold text" + "\033[22m")

    def test_italic_html(self):
        self.converter.markdown_content = "_italic text_"
        self.converter.apply_italic('html')
        self.assertEqual(self.converter.markdown_content, "<i>italic text</i>")

    def test_italic_text(self):
        self.converter.markdown_content = "_italic text_"
        self.converter.apply_italic('text', use_ansi=False)
        self.assertEqual(self.converter.markdown_content, "italic text")

    def test_italic_text_ansi(self):
        self.converter.markdown_content = "_italic text_"
        self.converter.apply_italic('text', use_ansi=True)
        self.assertEqual(self.converter.markdown_content, "\033[3m" + "italic text" + "\033[23m")

    def test_monospaced_html(self):
        self.converter.markdown_content = "`monospaced text`"
        self.converter.apply_monospaced('html')
        self.assertEqual(self.converter.markdown_content, "<tt>monospaced text</tt>")

    def test_monospaced_text(self):
        self.converter.markdown_content = "`monospaced text`"
        self.converter.apply_monospaced('text', use_ansi=False)
        self.assertEqual(self.converter.markdown_content, "monospaced text")

    def test_monospaced_text_ansi(self):
        self.converter.markdown_content = "`monospaced text`"
        self.converter.apply_monospaced('text', use_ansi=True)
        self.assertEqual(self.converter.markdown_content, "\033[7m" + "monospaced text" + "\033[27m")

    def test_preformatted_html(self):
        self.converter.markdown_content = "```preformatted text```"
        self.converter.apply_preformatted('html')
        self.assertEqual(self.converter.markdown_content, "<pre>preformatted text</pre>")

    def test_preformatted_text(self):
        self.converter.markdown_content = "```preformatted text```"
        self.converter.apply_preformatted('text', use_ansi=False)
        self.assertEqual(self.converter.markdown_content, "preformatted text")

    def test_preformatted_text_ansi(self):
        self.converter.markdown_content = "```preformatted text```"
        self.converter.apply_preformatted('text', use_ansi=True)
        self.assertEqual(self.converter.markdown_content, "\033[7m" + "preformatted text" + "\033[27m")

    def test_paragraphs_html(self):
        self.converter.markdown_content = "Paragraph one.\n\nParagraph two."
        self.converter.apply_paragraphs('html')
        self.assertEqual(self.converter.markdown_content, "Paragraph one.</p>\n<p>Paragraph two.")

    def test_paragraphs_text(self):
        self.converter.markdown_content = "Paragraph one.\n\nParagraph two."
        self.converter.apply_paragraphs('text')
        self.assertEqual(self.converter.markdown_content, "Paragraph one.\n\nParagraph two.")

    def test_full_conversion_html(self):
        self.converter.markdown_content = "**bold** _italic_ `monospaced` ```preformatted``` Paragraph."
        result = self.converter.convert_to_html()
        self.assertEqual(result, "<p><b>bold</b> <i>italic</i> <tt>monospaced</tt> <pre>preformatted</pre> Paragraph.</p>")

    def test_full_conversion_text(self):
        self.converter.markdown_content = "**bold** _italic_ `monospaced` ```preformatted``` Paragraph."
        result = self.converter.convert_to_text(use_ansi=False)
        self.assertEqual(result, "bold italic monospaced preformatted Paragraph.")

    def test_full_conversion_text_ansi(self):
        self.converter.markdown_content = "**bold** _italic_ `monospaced` ```preformatted``` Paragraph."
        result = self.converter.convert_to_text(use_ansi=True)
        self.assertEqual(result, "\033[1mbold\033[22m \033[3mitalic\033[23m \033[7mmonospaced\033[27m \033[7mpreformatted\033[27m Paragraph.")

if __name__ == '__main__':
    unittest.main()
