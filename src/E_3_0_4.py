def contarLetras(palabra,letra_a,letra_n,letra_b):
    numeros = []
    numeros.append(palabra.count(letra_a,0,len(palabra)))
    numeros.append(palabra.count(letra_n,0,len(palabra)))
    numeros.append(palabra.count(letra_b,0,len(palabra)))

    return numeros

def MensajeSalida(letra_a,letra_n,letra_b,contar_letras):
    return "La letra " + str(letra_a) + " aparece: " + str(contar_letras[0]) + " veces\nLa letra "  + str(letra_n) + " aparece: " + str(contar_letras[1]) + " veces\nLa letra "  + str(letra_b) + " aparece: " + str(contar_letras[2]) + " vez"
if __name__ == "__main__":

    #entrada
    palabra = "banana"
    letra_a = "a"
    letra_n = "n"
    letra_b = "b"

    #proceso
    contar_letras = contarLetras(palabra,letra_a,letra_n,letra_b)
    mensaje = MensajeSalida(letra_a,letra_n,letra_b,contar_letras)

    #salida
    print(mensaje)
