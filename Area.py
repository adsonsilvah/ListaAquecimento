import math

Valores = input().split()

A,B,C = Valores

pi = 3.14159

AreaTri = float(A) * float(C)/2

AreaCir = pi * math.pow(float(C), 2)

AreaTrap = (float(A)+float(B)) * float(C) /2

AreaQuad = float(B)*float(B)

AreaRetan = float(A)*float(B)

print("TRIANGULO: %0.3f\nCIRCULO: %0.3f\nTRAPEZIO: %0.3f\nQUADRADO: %0.3f\nRETANGULO: %0.3f" %
(AreaTri,AreaCir,AreaTrap,AreaQuad,AreaRetan))