#3.0.3

def cuenta(palabra,letra):
    contador = 0
    for ltra in palabra:
        if ltra == letra:
            contador = contador + 1
    return contador

if __name__ == "__main__":

    #entrada
    palabra = str(input("Introduzca una palabra: "))
    letra = str(input("Introduzca la letra a contar: "))

    #proceso
    contar_a = cuenta(palabra,letra)

    #salida
    print(contar_a)