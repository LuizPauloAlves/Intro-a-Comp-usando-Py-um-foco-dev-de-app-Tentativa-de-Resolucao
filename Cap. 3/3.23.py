lista = []
abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M']
x = 1
while x != '0':
    x = input("Digite:")
    if x != '0':
        lista.append(x)
for i in lista:
    if i[0] in abc:
        print(i)