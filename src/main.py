from textnode import TextNode, TextType
from recursive import static_to_public, make_abs_dir
from webpage import generate_page, generate_pages_recursive

def main():
    static_to_public(make_abs_dir("./static"), make_abs_dir("./public"))
    generate_pages_recursive("./content/", "./template.html", "./public/")


main()

