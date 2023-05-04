lista = []
x = 1
while x != '0':
    x = input("Digite:")
    if x != '0':
        lista.append(x)
for i in lista:
    for j in i:
        if j == 'm':
            k = 0
            break
        else:
            k = 1
    if k == 1:
        print(i)