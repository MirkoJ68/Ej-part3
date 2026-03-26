def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)

print(contar_palabras("hola papi como andas"))