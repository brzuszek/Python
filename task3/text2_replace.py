filepath='C:/Users/Szymon Mazurek/Desktop/Studia/rokIII/Pytong/task3'
f1="/tekst1.txt"
f2="/tekst2.txt"
f3="/tekst3.txt"
p1=filepath+f1
p2=filepath+f2
p3=filepath+f3
dictionary={'i':'oraz','oraz':'i','nigdy':'prawie nigdy','dlaczego':'czemu'}
words_2_replace=['i','oraz','nigdy','dlaczego']
k=len(words_2_replace)-1
txt_list=[p1,p2,p3]
n=len(txt_list)-1
while n>0:
    with open(txt_list[n], 'r') as file:
        data = file.read()
        while k>0:
            change = data.replace(words_2_replace[k],dictionary[words_2_replace[k]])
            k=k-1
    n=n-1
