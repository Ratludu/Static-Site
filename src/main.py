from textnode import TextNode, TextType
from recursive import static_to_public, make_abs_dir
from webpage import generate_page, generate_pages_recursive
import sys

def main():

    base = "/"
    if len(sys.argv) == 0: 
        base = sys.argv[1]
    static_to_public(make_abs_dir("./static"), make_abs_dir("./docs"))
    generate_pages_recursive(base,"content/", "./template.html", "./docs/")


main()

