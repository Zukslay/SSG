import os
import sys
from functions_directory import generate_page_recursive, copy_static_to_docs


def main():
    basepath = sys.argv[1]
    if not basepath:
        basepath = "/"

    copy_static_to_docs()
    current_dir = os.path.dirname(os.path.abspath("SSG"))
    content_dir = os.path.join(current_dir, "content")
    docs_dir = os.path.join(current_dir, "docs")
    
    generate_page_recursive(content_dir, docs_dir, basepath)






if __name__ == "__main__":
    main()