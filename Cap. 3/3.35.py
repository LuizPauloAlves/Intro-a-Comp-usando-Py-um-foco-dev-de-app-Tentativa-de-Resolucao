from math import *
def pontos(x1,y1,x2,y2):
    inc = float(x2 - x1)
    dis = sqrt((x2-x1)**2 + (y2-y1)**2)
    if inc == 0:
        print('A inclinação é infinita e a distancia é ',dis)
    else:
        print('A inclinação é ', inc, ' e a distancia é ', dis)
pontos(0,0,1,1)
pontos(0,0,0,1)