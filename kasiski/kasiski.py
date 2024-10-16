import argparse
import itertools

#listas para guardar la distancia entre cada subcriptograma
cuatrihashmapdiff = {}
trihashmapdiff = {}

# Inicializa el diccionario para contar los múltiplos
mcdhashmap = {i: 0 for i in range(2, 8)}

fragmentos = []

frecuencias = []

maxletter = {}
maxletter2 = {}
maxletter3 = {}

def buscar_cuatrigramas(text):
    for index in range(0,len(text)-4):
        count = 0
        cuatrigram = text[index:index+4]
        for auxindex in range(index+4, len(text)-4):
            if auxindex != 0:
                auxcuatrigram = text[auxindex:auxindex+4]
                if cuatrigram == auxcuatrigram:
                    count+=1
                    cuatrihashmapdiff[cuatrigram] = auxindex - index
                    #print(f"Cuatrigrama {cuatrigram} repetido {count} veces, diferencia {auxindex-index}")


def buscar_trigramas(text):
    for index in range(0,len(text)-3):
        count = 0
        trigram = text[index:index+3]
        for auxindex in range(index+3, len(text)-3):
            if auxindex != 0:
                auxtrigram = text[auxindex:auxindex+3]
                if trigram == auxtrigram:
                    count+=1
                    trihashmapdiff[trigram] = auxindex - index
                    #print(f"Trigrama {trigram} repetido {count} veces, diferencia {auxindex-index}")


def calcular_mcd():
    for i in range(2,8):
        for cuatrigram in cuatrihashmapdiff:
            if(cuatrihashmapdiff[cuatrigram] % i == 0):
                mcdhashmap[i] += 1
        for trigram in trihashmapdiff:
            if(trihashmapdiff[trigram] % i == 0):
                mcdhashmap[i] += 1

    #print("La longitud de la clave es el máximo común divisor más repetido:")    
    #for i in range(2,8):
        #print(f"{i}: {mcdhashmap[i]}")

    max=0
    max_mcd=0
    for i in range(2,8):
        if mcdhashmap[i]>max:
            max=mcdhashmap[i]
            max_mcd=i
    
    return max_mcd


#División del texto en fragmentos cifrados con la misma letra
def dividir_fragmentos(text,mcd):
    l = len(text)
    for i in range(mcd):
        fragmentos.append([])

    for i in range(mcd):
        for j in range(i,l,mcd):
            if j < l:
                fragmentos[i].append(text[j])


#Comprobamos las letras más repetidas en cada fragmento
def analisis_fragmentos(mcd):

    for i in range(mcd):
        frecuencias.append({'A': 0.0, 'B': 0.0, 'C': 0.0, 'D': 0.0, 
            'E': 0.0, 'F': 0.0, 'G': 0.0, 'H': 0.0, 'I': 0.0, 'J': 0.0, 
            'K': 0.0, 'L': 0.0, 'M': 0.0, 'N': 0.0, 'O': 0.0, 'P': 0.0, 
            'Q': 0.0, 'R': 0.0, 'S': 0.0, 'T': 0.0, 'U': 0.0, 'V': 0.0, 
            'W': 0.0, 'X': 0.0, 'Y': 0.0, 'Z': 0.0}) 
    
    for i in range(mcd):
        for key in frecuencias[i].keys(): # Coge de la A-Z
            for letter in fragmentos[i]: # Coge las letras del subcriptograma
                if letter == key: # Si coinciden se suma 1
                    frecuencias[i][key] += 1
    
    for i in range(mcd):
        for j in frecuencias[i].keys():
            frecuencias[i][j] = (frecuencias[i][j] / 26)

    #Calculamos la letra más repetida en el fragmento
    for i in range(mcd):
        maxfrec=0
        for j in frecuencias[i].keys():
            if frecuencias[i][j] > maxfrec:
                maxletter[i] = str(j)
                maxfrec = frecuencias[i][j]
    
    for i in range(mcd):
        maxfrec=0
        for j in frecuencias[i].keys():
            if str(j) != maxletter[i]  :
                if frecuencias[i][j] > maxfrec:
                    maxletter2[i] = str(j)
                    maxfrec = frecuencias[i][j]
    
    for i in range(mcd):
        maxfrec=0
        for j in frecuencias[i].keys():
            if str(j) != maxletter[i] and str(j) != maxletter2[i]:
                if frecuencias[i][j] > maxfrec:
                    maxletter3[i] = str(j)
                    maxfrec = frecuencias[i][j]

def main():
    alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
    'Q','R','S','T','U','V','W','X','Y','Z']

    parser = argparse.ArgumentParser(description='Análisis de cifrado vigenere con kasiski')
    parser.add_argument('archivo', help='El archivo de texto que contiene el texto cifrado')

    args = parser.parse_args()

    # Leer el contenido del archivo
    with open(args.archivo, 'r', encoding='utf-8') as f:
        mensaje = f.read()

    buscar_cuatrigramas(mensaje)
    buscar_trigramas(mensaje)
    
    mcd = calcular_mcd()

    dividir_fragmentos(mensaje,mcd)
    analisis_fragmentos(mcd)

    print(f"La clave usada para cifrar el texto es de {mcd} cifras")

    for i in range(mcd):
        print(f"Las letras más repetidas en el fragmento {i+1} son las letras: {maxletter[i]}, {maxletter2[i]}, {maxletter3[i]}")

    for i in range(mcd):
        print(f"Las frecuencias de las letras del fragmento {i+1}:")
        for j in frecuencias[i].keys():
            print(f"{j}:{frecuencias[i][j]:.2f}")

if __name__ == "__main__":
    main()
