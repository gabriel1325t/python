import time

def hi_everybody(lista):
    for name in lista:
        print("Oi", name)


hi_everybody(["Cha eun woo", "ama", "eu"])


def criar_lista(n):
    lista = []
    for i in range(n):
        lista.append(i)
    return lista

print(criar_lista(10))


time.sleep(3)
