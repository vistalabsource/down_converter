import markdown
import sys

def print_version():
    print("down_converter version 1.0.0")

def convert_markdown_to_html(markdown_file, html_output_file):
    try:
        with open(markdown_file, 'r', encoding='utf-8') as f:
            text = f.read()
            html = markdown.markdown(text)
        with open(html_output_file, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Markdownファイル '{markdown_file}' をHTMLファイル '{html_output_file}' に変換しました。")
        return html_output_file
    except FileNotFoundError:
        print("error: ファイルが存在しません。")
        sys.exit(1)


def main():
    if len(sys.argv) < 2:
        print("使い方: python main.py <markdownファイル> [options]")
        sys.exit(1)

    if '--version' in sys.argv:
        print_version()
        sys.exit(0)

    markdown_file = sys.argv[1]
    html_output_file = f"{markdown_file}.html"

    convert_markdown_to_html(markdown_file, html_output_file)

if __name__ == "__main__":
    main()