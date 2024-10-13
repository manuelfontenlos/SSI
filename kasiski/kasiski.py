import argparse

#listas para guardar las apariciones de cada subcriptograma
cuatrihashmapcount = {}
trihashmapcount = {}

#listas para guardar la distancia entre cada subcriptograma
cuatrihashmapdiff = {}
trihashmapdiff = {}

# Inicializa el diccionario para contar los múltiplos
mcdhashmap = {i: 0 for i in range(2, 7)}

def buscar_cuatrigramas(text):
    for index in range(0,len(text)-4):
        count = 0
        cuatrigram = text[index:index+4]
        for auxindex in range(index+4, len(text)-4):
            if auxindex != 0:
                auxcuatrigram = text[auxindex:auxindex+4]
                if cuatrigram == auxcuatrigram:
                    count+=1
                    cuatrihashmapcount[cuatrigram] = count
                    cuatrihashmapdiff[cuatrigram] = auxindex - index
                    print(f"Cuatrigrama {cuatrigram} repetido {count} veces, diferencia {auxindex-index}")


def buscar_trigramas(text):
    for index in range(0,len(text)-3):
        count = 0
        trigram = text[index:index+3]
        for auxindex in range(index+3, len(text)-3):
            if auxindex != 0:
                auxtrigram = text[auxindex:auxindex+3]
                if trigram == auxtrigram:
                    count+=1
                    trihashmapcount[trigram] = count
                    trihashmapdiff[trigram] = auxindex - index
                    print(f"Trigrama {trigram} repetido {count} veces, diferencia {auxindex-index}")


def calcular_mcd():
    for i in range(2,7):
        for cuatrigram in cuatrihashmapdiff:
            if(cuatrihashmapdiff[cuatrigram] % i == 0):
                mcdhashmap[i] += 1
    for i in range(2,7):
        for trigram in trihashmapdiff:
            if(trihashmapdiff[trigram] % i == 0):
                mcdhashmap[i] += 1
            

def main():
    parser = argparse.ArgumentParser(description='Análisis de cifrado vigenere con kasiski')
    parser.add_argument('archivo', help='El archivo de texto que contiene el texto')

    args = parser.parse_args()

    # Leer el contenido del archivo
    with open(args.archivo, 'r', encoding='utf-8') as f:
        mensaje = f.read()

    buscar_cuatrigramas(mensaje)
    buscar_trigramas(mensaje)
    calcular_mcd()

    for i in range(2,7):
        print(f"{i}: {mcdhashmap[i]}")

if __name__ == "__main__":
    main()
