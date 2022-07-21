'''generar una list-comprehension con los numeros del 1 al 100 elevados al cuadrado,
excepto los que sean multiplos de 3'''

def run():
    #lista = []
    #for i in range(1, 101):
    #    if i % 3 != 0:
    #       lista.append(i**2)

    lista = [i**2  for i in range(1, 101) if i % 3 != 0]
    print(lista)



if __name__ == '__main__':
    run()