# def empieza_con_A(elemento):
#     return elemento[0] == 'A'

# frutas = ['Apple', 'Orange', 'Pear', 'Apricot']

# # lista = []

# # for i in frutas:
# #     lista.append(empieza_con_A(i))
# comienza_con_A = list((map(lambda frutas: frutas[0] == 'A' ,frutas)))


# print(comienza_con_A)
# def cuadrados(carro):
#     return carro ** 2

lista = [11, 22, 33 ,44,55]
lista2 = [2,3,4,5,6,7,8]
# lista3 =[]
# for i in range(len(lista)):
#     lista3.append(lista[i]+ lista2[i])
lista3 = list(map(lambda a, b: a + b, lista, lista2 ))
# cuadrados = list(map(lambda lista: lista ** 2, lista))


print(lista3) 

 
