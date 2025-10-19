
from markdown_blocks import markdown_to_html_node
import os


def extract_title(markdown: str) -> str:
    with open(markdown, "r") as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith("# "):
                return line.lstrip("# ").strip()
        raise Exception("no h1 header")

def generate_page(base_path: str, from_path: str, template_path: str, dest_path: str) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    dest_path = dest_path.rstrip("index.md")
    with open(from_path, "r") as md:
        md_file = md.read()

    with open(template_path, "r") as tp:
        tmpl_file = tp.read()

    parent_node = markdown_to_html_node(md_file)
    html = parent_node.to_html()

    title = extract_title(from_path)

    tmpl_file = tmpl_file.replace("{{ Title }}", title)
    tmpl_file = tmpl_file.replace("{{ Content }}", html)
    tmpl_file = tmpl_file.replace('href="/', f'href="{base_path}')
    tmpl_file = tmpl_file.replace('src="/', f'src="{base_path}')

    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

    dest_path = os.path.join(dest_path, "index.html")
    with open(dest_path, "w") as f:
        f.write(tmpl_file)

def generate_pages_recursive(base_path: str, dir_path_content: str, template_path: str, dest_dir_path: str) -> None:           

    if not os.path.isdir(dir_path_content):
        return

    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for directory in os.listdir(dir_path_content):
        full_path = os.path.join(dir_path_content, directory)
        full_dest_path = os.path.join(dest_dir_path, directory)

        if os.path.isdir(full_path):
            print(f"New path: {full_path}")
            generate_pages_recursive(base_path, full_path, template_path, full_dest_path)

        if os.path.isfile(full_path):
            print(f"generating file: {full_path}")
            generate_page(base_path, full_path, template_path, full_dest_path)



