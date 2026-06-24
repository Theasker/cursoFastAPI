from pathlib import Path

p = Path(r"c:\Users\mseguraa\Documents\Python\cursoFastAPI\rutas\01_path.py")
print(p.absolute())

# Obtener el nombre de archivo
print(p.name)

# Obtener la extension del archivo
print(p.suffix)

# Obtener solo el nombre del archivo sin extension
print(p.stem)

# Obtener el directorio padre
print(p.parent)

# Crear un path relativo
p_relativo = Path("documentos/archivo.txt")
print(p_relativo)

print(Path()) # Obtiene la ruta actual
print(Path.home()) # Obtiene la ruta del usuario
print(Path.cwd()) # Obtiene el directorio actual
####
path = Path("hola-mundo/mi-archivo.py")
print(f"path.is_file(): {path.is_file()}")
print(f"path.is_dir(): {path.is_dir()}")
print(f"path.exists(): {path.exists()}")
print(f"path.is_absolute(): {path.is_absolute()}")
print(f"path.stem: {path.stem}")
print(f"path.suffix: {path.suffix}")
print(f"path.parent: {path.parent}")
print(f"path.name: {path.name}")
print(f"path.absolute: {path.absolute()}")
print(f"path.home: {path.home()}")
print(f"path.cwd: {path.cwd()}")

