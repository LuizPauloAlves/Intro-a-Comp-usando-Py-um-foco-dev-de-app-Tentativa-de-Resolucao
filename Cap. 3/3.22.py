lista = []
x = 1
while x != '0':
    x = input("Digite:")
    if x != '0':
        lista.append(x)
for i in lista:
    if i == 'segredo':
        continue
    print(i)