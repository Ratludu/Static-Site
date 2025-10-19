
from markdown_blocks import markdown_to_html_node
import os


def extract_title(markdown: str) -> str:
    with open(markdown, "r") as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith("# "):
                return line.lstrip("# ").strip()
        raise Exception("no h1 header")

def generate_page(from_path: str, template_path: str, dest_path: str) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as md:
        md_file = md.read()

    with open(template_path, "r") as tp:
        tmpl_file = tp.read()

    parent_node = markdown_to_html_node(md_file)
    html = parent_node.to_html()

    title = extract_title(from_path)

    tmpl_file = tmpl_file.replace("{{ Title }}", title)
    tmpl_file = tmpl_file.replace("{{ Content }}", html)

    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

    dest_path = os.path.join(dest_path, "index.html")
    with open(dest_path, "w") as f:
        f.write(tmpl_file)
            


