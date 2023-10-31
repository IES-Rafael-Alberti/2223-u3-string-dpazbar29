#3.0.1

def obtenerCadena(cadena:str) -> list:
    '''voltea la cadena y la devuelve letra a letra en diferentes lineas'''
    resultado = []
    cont = 0
    cadena = cadena[::-1]

    while cont < len(cadena):
        letra = cadena[cont]
        resultado.append(letra)
        strResultado = "\n".join(resultado)
        cont = cont + 1
    return strResultado



 

if __name__ == "__main__":

    #leer
    cadena = str(input("Intrduzca una palabra: "))

    #proceso
    letras = obtenerCadena(cadena)
    
    #devolución
    print(letras)
    