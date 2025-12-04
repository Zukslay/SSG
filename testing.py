import os


current_dir = os.path.dirname(os.path.abspath("SSG"))
static_path = os.path.join(current_dir, "static")
public_path = os.path.join(current_dir, "public")
archivos = os.listdir(current_dir)

for archivo in archivos:
    print(archivo)

print(current_dir)
print(static_path)