x = int(input("enter a number :- "))
x2 = str(x)
x3 = -(x)
reverse_number = []
if x2[0]=="-":
    for i in range(1,len(x2)):
        reverse_number.append(x3%10)
        x3 = x3//10
else:
    for i in range(len(x2)):
        reverse_number.append(x%10)
        x = x//10

reverse1 = 0
reverse_number.reverse()

for i in range(len(reverse_number)):
    num = reverse_number[i]*(10**i)
    reverse1 = reverse1 + num


if x2[0]=="-":
    print("-",reverse1, sep = "")
else:
    print(reverse1)
