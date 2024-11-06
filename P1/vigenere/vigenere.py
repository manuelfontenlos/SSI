import argparse


def obtener_array_caracter(caracter):
    alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
    'Q','R','S','T','U','V','W','X','Y','Z']
    
    # Encontrar el índice del carácter en el alfabeto
    indice_caracter = alfabeto.index(caracter)

    # Crear una lista circular: desde el carácter dado hasta el final, luego desde el principio
    array = alfabeto[indice_caracter:] + alfabeto[:indice_caracter]

    return array

def cifrar(mensaje,clave):
    alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
    'Q','R','S','T','U','V','W','X','Y','Z']

    mensaje = mensaje.upper()
    clave = clave.upper()

    mensaje_cifrado=""
    
    # Cifrado de cada letra del mensaje
    ind_clave=0
    for c_mens in mensaje:
        if (c_mens in alfabeto):
            ind = alfabeto.index(c_mens)
            # Pasamos la letra correspondiente de la clave a la función auxiliar
            mensaje_cifrado+=(obtener_array_caracter(clave[ind_clave%len(clave)])[ind]) 
            ind_clave+=1

    return mensaje_cifrado



def descifrar (mensaje,clave):
    alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
    'Q','R','S','T','U','V','W','X','Y','Z']

    mensaje = mensaje.upper()
    clave = clave.upper()

    mensaje_descifrado = ""
    
    # Descifrado de cada letra da mensaxe
    ind_clave = 0
    for c_mens in mensaje:
        if c_mens in alfabeto:
            #Obtén a posición que ten o caracter no array de caracteres que lle pertenece según a clave  
            ind_clave_letra = obtener_array_caracter(clave[ind_clave%len(clave)]).index(c_mens)
            #Segun esa posición fai o descifrado no alfabeto orixinal
            mensaje_descifrado += alfabeto[ind_clave_letra]
            #Incrementa o valor da clave
            ind_clave += 1

    return mensaje_descifrado



def main():
    parser = argparse.ArgumentParser(description='Cifrado vigenere')
    parser.add_argument('archivo', help='Archivo a cifrar')
    parser.add_argument('clave', help='La clave para el cifrado')
    parser.add_argument('--descifrar', action='store_true', help='Si se indica, descifra el archivo')

    args = parser.parse_args()

    if (len(args.clave)) > 7:
        print("La clave debe tener menos de 7 caracteres")
        exit()

    with open(args.archivo, 'r', encoding='utf-8') as f:
        mensaje = f.read()    

    if args.descifrar:
        resultado = descifrar(mensaje, args.clave)
        archivo_salida = 'mensaje_descifrado.txt'
        with open('mensaje_descifrado.txt', 'w', encoding='utf-8') as f:
            f.write(resultado)
        print(f"Mensaje descifrado guardado en 'mensaje_descifrado.txt'")
    else:
        resultado = cifrar(mensaje, args.clave)
        archivo_salida = 'mensaje_cifrado.txt'
        with open('mensaje_cifrado.txt', 'w', encoding='utf-8') as f:
            f.write(resultado)
        print(f"Mensaje cifrado guardado en 'mensaje_cifrado.txt'")    
    # Escribir el resultado en un nuevo archivo
    


if __name__ == "__main__":
    main()
