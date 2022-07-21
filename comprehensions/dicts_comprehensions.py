'''generamos  un diccionario-comprehensions donde los valores de las llaves seran los 
numero del 1 al 100 excepto los multiplos de 3, donde el valor de la llave serà la llave 
elevada al cubo'''


def run():
    my_dict = {}
    for i in range(1,101):
        if i % 3 != 0:
            my_dict[i] = i**3
     
    print(my_dict)

if __name__ ==  '__main__':
    run()