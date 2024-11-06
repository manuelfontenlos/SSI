import argparse

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def construir_alfabeto(clave):
    letras_unicas = []

    # Añado la clave a una lista de letras únicas
    for letra in clave.upper():
        if letra not in letras_unicas:
            letras_unicas.append(letra)

    # Añado las letras del alfabeto que no estén en la clave
    for letra in alfabeto:
        if letra not in letras_unicas:
            letras_unicas.append(letra)

    # Intercambio de letras basado en la clave
    for i in range(len(letras_unicas)):
        # Usamos el código ASCII de la letra correspondiente de la clave para determinar la posición de intercambio
        swap_index = ord(clave[i % len(clave)]) % len(letras_unicas)
        letras_unicas[i], letras_unicas[swap_index] = letras_unicas[swap_index], letras_unicas[i]

    return letras_unicas



def cifrar(texto, clave):

    nuestroalfabeto = construir_alfabeto(clave)

    texto_cifrado = ""
    for letra in texto:
            pos = alfabeto.index(letra)
            texto_cifrado += nuestroalfabeto[pos]
            
    return texto_cifrado


def descifrar(texto, clave):

    nuestroalfabeto = construir_alfabeto(clave)
    
    texto_descifrado = ""
    for letra in texto:
        pos = nuestroalfabeto.index(letra)
        texto_descifrado += alfabeto[pos]

    return texto_descifrado



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
        with open('texto_cifrado.txt', 'w', encoding='utf-8') as f:
            f.write(resultado)
        print(f"Texto cifrado guardado en 'texto_cifrado.txt'")
    elif args.accion == 'descifrar':
        resultado = descifrar(mensaje, args.clave)
        # Escribir el resultado en un nuevo archivo
        with open('texto_descifrado.txt', 'w', encoding='utf-8') as f:
            f.write(resultado)
        print(f"Texto descifrado guardado en 'texto_descifrado.txt'")

if __name__ == "__main__":
    main()
