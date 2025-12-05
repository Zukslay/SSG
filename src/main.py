import os
from functions_directory import copy_static_to_public, generate_page


def main():
    copy_static_to_public()
    current_dir = os.path.dirname(os.path.abspath("SSG"))
    contents = ["content/index.md",
                 "content/blog/glorfindel/index.md",
                 "content/blog/majesty/index.md",
                 "content/blog/tom/index.md",
                 "content/contact/index.md"]
    paths = []
    html_template = os.path.join(current_dir, "template.html")
    for content in contents:
        cont = os.path.join(current_dir, content)
        paths.append([cont, html_template, cont.replace("content", "public").replace(".md", ".html")])
    
    for path in paths:
        generate_page(path[0], path[1], path[2])






if __name__ == "__main__":
    main()