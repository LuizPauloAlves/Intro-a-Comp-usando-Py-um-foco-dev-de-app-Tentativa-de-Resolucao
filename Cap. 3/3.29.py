x = 0
while True:
    x = eval(input('digite o valor de x:'))
    if x < -10 or x > 10:
        continue
    y = eval(input('digite o valor de y:'))
    if y >= -10 and y <= 10:
        break
if x**2 + y**2 <= 8**2:
    print("está dentro")
else:
    print('Errou!!!')