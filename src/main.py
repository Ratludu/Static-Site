from textnode import TextNode, TextType
from recursive import static_to_public, make_abs_dir
from webpage import generate_page

def main():
    static_to_public(make_abs_dir("./static"), make_abs_dir("./public"))
    generate_page("./content/index.md", "./template.html", "./public/")


main()

