s = f"([(])])"
dict = {")":"(","}":"{","]":"["}
list2 = []
for i in s:
    if i in dict.values():
        list2.append(i)
    elif i in dict.keys():
        if not list2 or list2[-1] != dict[i]:
            print(f"match of {i}, not found")
            break
        list2.pop()
if len(list2)==0:
    print("valid parenthesis")
else:
    print("invalid parenthesis")

