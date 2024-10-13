import argparse

#listas para guardar las apariciones de cada subcriptograma
cuatrihashmapcount = {}
trihashmapcount = {}

#listas para guardar la distancia entre cada subcriptograma
cuatrihashmapdiff = {}
trihashmapdiff = {}


def buscar_cuatrigramas(text):
    for index in range(len(text)-3):
    
        count = 0
        cuatrigram = text[index:index+3]
        poscuatrigram = index+3
        for auxindex in range(len(text)-3):
            if auxindex != 0:
                auxcuatrigram = text[auxindex:auxindex+3]
                if cuatrigram == auxcuatrigram:
                    count+=1
                    cuatrihashmapdiff.add(cuatrigram)
                    cuatrihashmapcount.add(cuatrigram)
                    cuatrihashmapcount[cuatrihashmapcount] = count
                    cuatrihashmapdiff[cuatrigram] = auxindex - poscuatrigram
                    print(f"Cuatrigrama {cuatrigram} repetido {count} veces, diferencia {auxindex-poscuatrigram}")


def buscar_trigramas(text):
    for index in range(len(text)-2):
    
        count = 0
        trigram = text[index:index+2]
        postrigram = index+2
        for auxindex in range(len(text)-2):
            if auxindex != 0:
                auxtrigram = text[auxindex:auxindex+2]
                if trigram == auxtrigram:
                    count+=1
                    trihashmapdiff.add(trigram)
                    trihashmapcount.add(trigram)
                    trihashmapcount[trihashmapcount] = count
                    trihashmapdiff[trigram] = auxindex - postrigram
                    print(f"Trigrama {trigram} repetido {count} veces, diferencia {auxindex-postrigram}")


def main():
    parser = argparse.ArgumentParser(description='Análisis de cifrado vigenere con kasiski')
    parser.add_argument('archivo', help='El archivo de texto que contiene el texto')

    args = parser.parse_args()

    # Leer el contenido del archivo
    with open(args.archivo, 'r', encoding='utf-8') as f:
        mensaje = f.read()         

    buscar_cuatrigramas(mensaje)
    buscar_trigramas(mensaje)
