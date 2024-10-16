import argparse

# Creación del vector S necesario para la función PRGA
def KSA(key):
    # Inicialización
    S = list(range(256))
    T = [0] * 256
    
    keylen = len(key)
    for i in range(256):
        T[i] = key[i % keylen]  
    
    # Permutación inicial de S
    j = 0
    for i in range(256):
        j = (j + S[i] + T[i]) % 256
        S[i], S[j] = S[j], S[i]

    return S

# Generamos el keystream
def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # Intercambiamos posiciones del array S
        
        t = (S[i] + S[j]) % 256
        K = S[t]
        yield K  

def hex_to_bytes(hex_string):
    return [int(hex_string[i:i+2], 16) for i in range(0, len(hex_string), 2)]

def hex_to_ascii(hex_string):
    try:
        # Convierte la cadena hexadecimal a bytes
        bytes_data = bytes.fromhex(hex_string)
        # Decodifica los bytes a texto usando UTF-8
        ascii_text = bytes_data.decode('utf-8', errors='replace')  # 'replace' reemplaza caracteres no válidos
        return ascii_text
    except ValueError as e:
        print(f"Error al convertir hexadecimal a ASCII: {e}")
        return None

def cifrar_archivo(input_file, key_hex, output_file, output_file2):
    key = hex_to_bytes(key_hex)
    S = KSA(key)
    
    keystream = PRGA(S)  

    with open(input_file, 'rb') as f:
        texto = f.read()

    contenido = texto.decode('utf-8', errors='replace')

    print(f"El texto a descifrar es : {contenido}")
    
    resultado_hex = ""
    
    for byte in texto:
        ascii_value = byte
        caracter = chr(ascii_value)
        print(f"ASCII de '{caracter}': {ascii_value} ({bin(ascii_value)[2:].zfill(8)} en binario)")

        keystream_value = next(keystream)
        print(f"Keystream: {keystream_value} ({bin(keystream_value)[2:].zfill(8)} en binario)")

        cifrado = ascii_value ^ keystream_value
        print(f"Cifrado (binario): {bin(cifrado)[2:].zfill(8)}")
        resultado_hex += hex(cifrado)[2:].zfill(2)

    # Guardar el texto cifrado en el archivo de salida
    with open(output_file, 'w') as f:
        f.write(resultado_hex)

    print(f"Texto cifrado completo (hexadecimal): {resultado_hex}")
    
    resultado=hex_to_ascii(resultado_hex)

    with open(output_file2, 'w') as f:
        f.write(resultado)

    print(f"Texto cifrado completo : {resultado}")

def descifrar_archivo(input_file, key_hex, output_file):
    key = hex_to_bytes(key_hex)
    S = KSA(key)
    keystream = PRGA(S)

    with open(input_file, 'r') as f:
        texto_cifrado_hex = f.read().strip()
    
    texto_cifrado = hex_to_bytes(texto_cifrado_hex)
    
    texto_descifrado = bytearray()
    for byte_cifrado in texto_cifrado:
        keystream_value = next(keystream)
        descifrado = byte_cifrado ^ keystream_value  
        texto_descifrado.append(descifrado)

   
    with open(output_file, 'wb') as f:
        f.write(texto_descifrado)

    print(f"Texto descifrado (ASCII): {texto_descifrado.decode('utf-8', errors='replace')}")

# Función principal para procesar los argumentos y ejecutar el algoritmo
def main():
    parser = argparse.ArgumentParser(description='RC4 Cifrado/Descifrado de Archivos')
    parser.add_argument('clave', help='Clave de cifrado en formato hexadecimal')
    parser.add_argument('archivo', help='Nombre del archivo a cifrar o descifrar')
    parser.add_argument('--cifrar', action='store_true', help='Cifrar el archivo')
    parser.add_argument('--descifrar', action='store_true', help='Descifrar el archivo')

    args = parser.parse_args()

    if args.cifrar:
        output_file = args.archivo + 'hex.cifrado'
        output_file2 = args.archivo + 'ascii.cifrado'
        cifrar_archivo(args.archivo, args.clave, output_file, output_file2)
    elif args.descifrar:
        output_file = args.archivo + '.descifrado'
        descifrar_archivo(args.archivo, args.clave, output_file)
    else:
        print("Por favor, selecciona --cifrar o --descifrar")

if __name__ == "__main__":
    main()
