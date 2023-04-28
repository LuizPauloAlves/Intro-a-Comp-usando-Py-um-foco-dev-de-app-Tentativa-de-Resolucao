##
#
lista = [3,7,-2,12]
print(lista[len(lista)//2])
#
##
#
print(lista[len(lista)//2-1])
#
##
#
lista.sort()
print(lista)
#
##
#
a = lista[0]
lista.remove(a)
lista.append(a)
print(lista)
#
