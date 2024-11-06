import argparse

# Creación del vector S necesario para la función PRGA
def KSA(key, Sini):
    
    T = [0] * 256
    
    keylen = len(key)
    for i in range(256):
        T[i] = key[i % keylen]  
    j = 0
    for i in range(256):
        j = (j + Sini[i] + T[i]) % 256
        Sini[i], Sini[j] = Sini[j], Sini[i]

    return Sini

# Generamos o keystream
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
        bytes_data = bytes.fromhex(hex_string)
        ascii_text = bytes_data.decode('utf-8', errors='replace')  
        return ascii_text
    except ValueError as e:
        print(f"Error al convertir hexadecimal a ASCII: {e}")
        return None

def cifrar_rc4(key_hex):

    key = hex_to_bytes(key_hex)
    S_ini = list(range(256))


    print(f"Valor inicial de S: {S_ini}")
    S = KSA(key,S_ini)
    
    print(f"Valor de S después de KSA: {S}")
    keystream = PRGA(S)  
    resultado_hex = ""
    
    # Cifrado carácter a carácter
    while True:
        caracter = input("Introduce un carácter (o presiona Enter para terminar): ")
        if caracter == "":
            break
        ascii_value = ord(caracter)
        print(f"ASCII de '{caracter}': {ascii_value} ({bin(ascii_value)[2:].zfill(8)} en binario)")
        keystream_value = next(keystream)
        print(f"Keystream: {keystream_value} ({bin(keystream_value)[2:].zfill(8)} en binario)")
        cifrado = ascii_value ^ keystream_value
        print(f"Cifrado (binario): {bin(cifrado)[2:].zfill(8)}")
        print(f"Cifrado (hexadecimal): {hex(cifrado)[2:]}")
        resultado_hex += hex(cifrado)[2:].zfill(2)

    print(f"Texto cifrado completo (hexadecimal): {resultado_hex}")

    #Pasar de hexadecimal a código ASCII
    
    resultado=hex_to_ascii(resultado_hex)

    print(f"Texto cifrado completo : {resultado}")

def descifrar_rc4(key_hex):
    key = hex_to_bytes(key_hex)
    S_ini = list(range(256))
    S = KSA(key, S_ini)
    keystream = PRGA(S)
    texto_cifrado_hex = input("Introduce el texto cifrado en hexadecimal: ").strip()
    texto_cifrado = hex_to_bytes(texto_cifrado_hex)
    texto_descifrado = bytearray()
    for byte_cifrado in texto_cifrado:
        keystream_value = next(keystream)
        descifrado = byte_cifrado ^ keystream_value  
        texto_descifrado.append(descifrado)
    
    # Mostrar el resultado en formato ASCII
    print(f"Texto descifrado (ASCII): {texto_descifrado.decode('utf-8', errors='replace')}")


def main():
    parser = argparse.ArgumentParser(description='RC4 Cifrado/Descifrado')
    parser.add_argument('clave', help='Clave de cifrado en formato hexadecimal')
    parser.add_argument('--cifrar', action='store_true', help='Realizar el proceso de cifrado')
    parser.add_argument('--descifrar', action='store_true', help='Realizar el proceso de descifrado')

    args = parser.parse_args()

    if args.cifrar:
        cifrar_rc4(args.clave)
    elif args.descifrar:
        descifrar_rc4(args.clave)
    else:
        print("Por favor, selecciona --cifrar o --descifrar")

if __name__ == "__main__":
    main()