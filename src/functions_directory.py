import os
import shutil

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
    print(static_path)

    if not os.path.exists(static_path):
        raise Exception("static directory doesn't exists")
    
    if os.path.exists(public_path):
        shutil.rmtree(public_path)
        os.mkdir(public_path)
    else:
        os.mkdir(public_path)
    
    recursive_path(static_path, public_path)
        

    return public_path