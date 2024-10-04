import argparse

def cifrar(mensaje, clave):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letras_unicas = []

    # Añado la clave a una lista de letras únicas
    for letra in clave.upper():
        if letra not in letras_unicas and letra in alfabeto:
            letras_unicas.append(letra)

    # Añado las letras del alfabeto que no estén en la clave
    for letra in alfabeto:
        if letra not in letras_unicas:
            letras_unicas.append(letra)

    # Desplazo las letras únicas según la longitud de la clave
    long_clave = len(clave)
    desplazamiento = long_clave % len(letras_unicas)
    letras_unicas = letras_unicas[-desplazamiento:] + letras_unicas[:-desplazamiento] 

    # Intercambio las letras en posiciones pares por las impares y viceversa
    for i in range(0, len(letras_unicas) - 1, 2):
        letras_unicas[i], letras_unicas[i + 1] = letras_unicas[i + 1], letras_unicas[i]

    # Cifro el mensaje
    mensaje_cifrado = ""
    for letra in mensaje:
        if letra in alfabeto:
            pos = alfabeto.index(letra)
            mensaje_cifrado += letras_unicas[pos]
        else:
            mensaje_cifrado += letra
            
    return mensaje_cifrado

def descifrar(mensaje_cifrado, clave):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letras_unicas = []

    for letra in clave.upper():
        if letra not in letras_unicas and letra in alfabeto:
            letras_unicas.append(letra)

    for letra in alfabeto:
        if letra not in letras_unicas:
            letras_unicas.append(letra)

    long_clave = len(clave)
    desplazamiento = long_clave % len(letras_unicas)
    letras_unicas = letras_unicas[-desplazamiento:] + letras_unicas[:-desplazamiento]

    for i in range(0, len(letras_unicas) - 1, 2):
        letras_unicas[i], letras_unicas[i + 1] = letras_unicas[i + 1], letras_unicas[i]

    mensaje_descifrado = ""
    for letra in mensaje_cifrado:
        if letra in letras_unicas:
            pos = letras_unicas.index(letra)
            mensaje_descifrado += alfabeto[pos]
        else:
            mensaje_descifrado += letra  # Si no está en el alfabeto, añadir la letra original

    return mensaje_descifrado

def main():
    parser = argparse.ArgumentParser(description='Cifrado y descifrado textos.')
    parser.add_argument('accion', choices=['cifrar', 'descifrar'], help='Acción a realizar: cifrar o descifrar')
    parser.add_argument('archivo', help='El archivo de texto que contiene el texto')
    parser.add_argument('clave', help='La clave para el cifrado o descifrado')

    args = parser.parse_args()

    # Leer el contenido del archivo
    with open(args.archivo, 'r', encoding='utf-8') as f:
        mensaje = f.read()

    if args.accion == 'cifrar':
        resultado = cifrar(mensaje, args.clave)
        # Escribir el resultado en un nuevo archivo
        with open('mensaje_cifrado.txt', 'w', encoding='utf-8') as f:
            f.write(resultado)
        print(f"Mensaje cifrado guardado en 'mensaje_cifrado.txt'")
    elif args.accion == 'descifrar':
        resultado = descifrar(mensaje, args.clave)
        # Escribir el resultado en un nuevo archivo
        with open('mensaje_descifrado.txt', 'w', encoding='utf-8') as f:
            f.write(resultado)
        print(f"Mensaje descifrado guardado en 'mensaje_descifrado.txt'")

if __name__ == "__main__":
    main()