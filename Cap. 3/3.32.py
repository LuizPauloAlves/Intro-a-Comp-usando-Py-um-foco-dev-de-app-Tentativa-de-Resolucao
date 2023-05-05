def pagar(sal, hora):
    if hora <= 40:
        print(sal*hora)
    else:
        print(int(sal*40 + 1.5*sal*(hora-40)))
pagar(10,10)
pagar(10,35)
pagar(10,45)