import os
import shutil
import re
from functions_block import converter

def recursive_path(path, copy_path):
    for dir_or_file in os.listdir(path):
        sub_path = os.path.join(path, dir_or_file)
        
        if os.path.isfile(sub_path):
            sub_path_copy = os.path.join(copy_path, dir_or_file)
            shutil.copy(sub_path, sub_path_copy)

        else:
            sub_path_copy = os.path.join(copy_path, dir_or_file)
            os.mkdir(sub_path_copy)
            recursive_path(sub_path, sub_path_copy)

def copy_static_to_public():
    current_dir = os.path.dirname(os.path.abspath("SSG"))
    static_path = os.path.join(current_dir, "static")
    public_path = os.path.join(current_dir, "public")
    

    if not os.path.exists(static_path):
        raise Exception("static directory doesn't exists")
    
    if os.path.exists(public_path):
        shutil.rmtree(public_path)
        os.mkdir(public_path)
    else:
        os.mkdir(public_path)
    
    recursive_path(static_path, public_path)
        

    return public_path

def extract_title(md):
    h1_header = md.split("\n\n")[0]
    if bool(re.match(r"^# ", h1_header)):
        return re.sub(r"^# ", "", h1_header)
    else:
        raise Exception("no header <h1>")
    
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    md_content = None
    temp_content = None
    
    with open(from_path) as path:
        md_content = path.read()
    
    with open(template_path) as temp_path:
        temp_content = temp_path.read()
    
    md_title = extract_title(md_content)
    md_to_html = converter(md_content)
    
    

    temp_content = temp_content.replace("{{ Title }}", md_title)
    temp_content = temp_content.replace("{{ Content }}", md_to_html)
    
    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(temp_content)
