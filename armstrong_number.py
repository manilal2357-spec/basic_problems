x = 153
a = x 
l1 = []

while x>0:
    r = x%10
    l1.append(r)
    x = x//10
sum = 0
for i in l1:
    sum = sum + i**len(l1) 
if sum == a:
    print("given number is a armstrong number.") 
else:
    print("given number is not a armstrong number.") 