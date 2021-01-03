import random
n=50
numbers=[]
while n>0:
    numbers.append(random.randint(1,100))
    n=n-1

for i in range (0, len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i]<numbers[j]:
            copy1 = numbers[i]
            copy2 = numbers[j]
            numbers[i]=copy2
            numbers[j]=copy1


print(numbers)
