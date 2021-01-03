
filepath='C:/Users/Szymon Mazurek/Desktop/Studia/rokIII/Pytong/task3'
f1="/tekst1.txt"
f2="/tekst2.txt"
f3="/tekst3.txt"
p1=filepath+f1
p2=filepath+f2
p3=filepath+f3

txt_list=[p1,p2,p3]
n=len(txt_list)-1
while n>0:
    with open(txt_list[n], 'r') as file:
        data = file.read()
        change = data.replace("się", "").replace("i", "").replace(
            "oraz", "").replace("nigdy", "").replace("dlaczego", "")
    n=n-1
