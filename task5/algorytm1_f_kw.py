import math as m

a=float(input("Podaj wspolczynnik a funkcji: "))
b=float(input("Podaj wspolczynnik b funkcji: "))
c=float(input("Podaj wspolczynnik c funkcji: "))

delta=b*b-4*a*c

if delta<0:
    print("Brak miejsc zerowych funckji")
elif delta==0:
    x1=-b/(2*a)
    print("Jedno miejsce zerowe: "+ str(x1))
else:
    x1=(-b-m.sqrt(delta))/(2*a)
    x2=(-b+m.sqrt(delta))/(2*a)
    print("Dwa miejsca zerowe: "+str(x1)+", "+ str(x2))
