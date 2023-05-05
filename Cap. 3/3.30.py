while True:
    valor = eval(input("Valor:"))
    if valor >= 1000 and valor <= 9999:
        break
for i in range(4,0,-1):
    print(valor // 10 ** (i-1))
    valor = valor % 10**(i-1)