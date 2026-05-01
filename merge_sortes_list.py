list1 = [1,3,5,7]
list2 = [2,3,4,5,10] 
for i in list1:
    for j in range(len(list2)):
        if i<=list2[j]:
            list2.insert(j,i)
            break
print(list2)



