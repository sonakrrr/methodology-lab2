# Methodology-lab2
Lab2 for methodologies and technologies of software development
## Functionality
This program is designed to convert text written in Markdown format into corresponding HTML code. Upon execution, the program takes a path to a Markdown file as input. The `MarkdownConverter` class is initialized with this file and stores its content in an internal variable. The `convert_to_html` method calls a series of sub-methods to process various Markdown elements such as:
- Bold Text: `**text**` becomes `<b>text</b>`.
- Italic Text: `_text_` becomes `<i>text</i>`.
- Monospaced Text: `` `text` `` becomes `<tt>text</tt>`.
- Preformatted Text: ``` ```text``` ``` becomes `<pre>text</pre>`.

After processing the text, the program returns it in HTML format wrapped in `<p>` tags. The main part of the program checks the correctness of the command-line arguments. If they are correct, an instance of the `MarkdownConverter` class is created, the text is converted to HTML, and if an output file is specified, the result is written to the file; if no output file is specified, the HTML is printed to the screen.

## How to start
To start using the program, you need to have Python downloaded on your computer.
Then all you need to do is copy this repository to your machine. You can do this using this command:
```shell
git clone https://github.com/sonakrrr/methodology-lab1
```

## How to use
This program was developed exclusively for console use. To run it, you need to pass arguments (input and output) using the following command:
```shell
python convert_markdown.py <input_file_path> [-o, --out <output_file_path>] [-f, --format <format>]
```
`<input_file_path>` - path to your markdown file.

`<output_file_path>` - path to your output file: either `.html` or `.txt`.

`<format>` - output format: `html` `text` or `text --ansi`.

If used without the `--out` key, the text will be output to the console
```shell
python convert_markdown.py <input_file_path> --format <format> 
```
If you use without the `--format` key, the result will be automatically displayed as html
```shell
python convert_markdown.py <input_file_path> 
```
## Running tests
Run the tests using this command:
```shell
python -m unittest test_markdown_converter.py
```
## Conclusion after implementing tests
Utilizing unit tests for this project proved to be immensely beneficial. Leveraging my prior experience with them, I effortlessly crafted a suite of tests that scrutinized every aspect of the program's functionality. This practice not only instilled confidence in the correctness of my code but also preemptively averted potential errors in the future. 

## Revert commit
[Here is the link](https://github.com/sonakrrr/methodology-lab2/commit/284d4a36fcf52fa582fade9499035cb0b3904628)

## Failed tests
[Here is the link](https://github.com/sonakrrr/methodology-lab2/commit/1ffca91e4f124500d383534dabb4f2ea212479aa)
