def inverte_int(N):
    N = str(N)
    print(int(N[::-1]))

inverte_int(123)
inverte_int(908)

def inverte_int2(n):
    new = 0
    while n !=0:
        new = new * 10 + n % 10
        n = n // 10
    print(new)

inverte_int2(123)
inverte_int2(908)
