from functools import reduce
# 
lista = [1,2,3,4,5,6,7,8,9]
# 
# suma = 0
# 
# for i in lista:
#     suma+=i
# 
# print(suma)

suma = reduce(lambda x,y: x+y, lista)

print(suma)