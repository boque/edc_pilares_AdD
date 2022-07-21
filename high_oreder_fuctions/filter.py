# fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
# filter_object = list(filter(lambda s: s[0] == "A", fruit))
# print(filter_object)



lista = [1,23,4,4,7,4,7,9,4,6,8,9,2,56]

multiplos_de_3 = list(filter( lambda l: l % 3 == 0, lista ))

print(multiplos_de_3)


