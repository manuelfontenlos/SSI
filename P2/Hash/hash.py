import hashlib
import argparse
import sys

# Funciones para obtener el hash de una cadena de texto
def func_hash_string(string, algoritmo):
    if algoritmo == 'md5':
        return hashlib.md5(string.encode()).hexdigest()
    elif algoritmo == 'sha1':
        return hashlib.sha1(string.encode()).hexdigest()
    elif algoritmo == 'sha256':
        return hashlib.sha256(string.encode()).hexdigest()

# Funciones para obtener el hash de un archivo
def func_hash_file(file, algoritmo):
    if algoritmo == 'md5':
        hash_obj = hashlib.md5()
    elif algoritmo == 'sha1':
        hash_obj = hashlib.sha1()
    elif algoritmo == 'sha256':
        hash_obj = hashlib.sha256()
    else:
        return None

    with open(file, 'rb') as f:
        # Leer el archivo en bloques de 1024 bytes
        while chunk := f.read(1024):
            hash_obj.update(chunk)

    return hash_obj.hexdigest()


def main():
    parser = argparse.ArgumentParser(
        description='Generador de hash. Utiliza esta herramienta para obtener el hash MD5, SHA-1 o SHA-256 de una cadena de texto o un archivo.',
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('-a', help='Algoritmo de hash a utilizar', choices=['md5', 'sha1', 'sha256'], default='md5')
    parser.add_argument('-s', metavar='texto', help='Cadena de texto para obtener el hash')
    parser.add_argument('-f', metavar='archivo', help='Ruta del archivo para obtener el hash')
    
    args = parser.parse_args()

    if args.s:  
        print(func_hash_string(args.s, args.a))
    elif args.f:  
        print(func_hash_file(args.f, args.a))
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == '__main__':
    main()