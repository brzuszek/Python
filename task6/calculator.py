from complex import Complex as cp

compare=cp(0,0)
compare1=float(1)

while (1):
    print("Wybierz typ liczby: ")
    print("1. Liczba rzeczywista")
    print("2. Liczba urojona")
    choice=(input())

    if not choice.isdigit() or int(choice)!=1 or int(choice)!=2 :
        print("Podaj prawidlowa wartosc!")
    elif int(choice)==1:
        num1=float(input("Podaj pierwszą liczbę: "))
        break
    elif int(choice)==2:
        num1_re=float(input("Podaj czest rzeczywista: "))
        num1_im=float(input("Podaj czest urojona: "))
        num1=cp(num1_re,num1_im)
        break

while(1):
    print("Wybierz typ liczby: ")
    print("1. Liczba rzeczywista")
    print("2. Liczba urojona")
    choice=(input())
    if not choice.isdigit() or int(choice)!=1 or int(choice)!=2 :
        print("Podaj prawidlowa wartosc!")
    elif int(choice)==1:
        num2=float(input("Podaj pierwszą liczbę: "))
        break
    elif int(choice)==2:
        num2_re=float(input("Podaj czest rzeczywista: "))
        num2_im=float(input("Podaj czest urojona: "))
        num2=cp(num2_re,num2_im)
        print(type(num2))
        break


while(1):

    print("1.Dodawanie")
    print("2.Odejmowanie")
    print("3.Mnozenie")
    print("4.Dzielenie")
    op=(input())
    if not op.isdigit() or int(op)!=1 or int(op)!=2 or int(op)!=3 or int(op)!=4:
        print("Podaj prawidlowa wartosc!")
    else:
        break
while(1):
    if op==1:
        if type(num1)==type(num2):
            res=num1+num2
            break
        elif (type(num1)==type(compare))&(type(num2)!=type(compare)):
            res=num1
            res.re=res.re+num2
            break
        elif (type(num2)==type(compare))&(type(num1)!=type(compare)):
            res=num2
            res.re=res.re+num1
            break

    elif op==2:
        if type(num1)==type(num2):
            res=num1-num2
            break
        elif (type(num1)==type(compare))&(type(num2)!=type(compare)):
            res=num1
            res.re=res.re-num2
            break
        elif (type(num2)==type(compare))&(type(num1)!=type(compare)):
            res=num2
            res.re=res.re-num1
            break



    elif op==3:
        if type(num1)==type(num2):
            res=num1*num2
            break
        elif (type(num1)==type(compare))&(type(num2)!=type(compare)):
            res=num1
            res.re=res.re*num2
            res.im=res.im*num2
            break
        elif (type(num2)==type(compare))&(type(num1)!=type(compare)):
            res=num2
            res.re=res.re*num1
            res.im=res.im*num1
            break

    elif op==4:
        if type(num1)==type(num2):
            res=num1/num2
            break
        elif (type(num1)==type(compare))&(type(num2)!=type(compare)):
            res=num1
            res.re=res.re/num2
            res.im=res.im/num2
            break
        elif (type(num2)==type(compare))&(type(num1)!=type(compare)):
            res=num2
            res.re=res.re/num1
            res.im=res.im/num1
            break



print("Wynik to: "+str(res))

