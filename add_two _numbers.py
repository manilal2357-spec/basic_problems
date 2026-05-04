l1 = [9, 3, 4]
l2 = [5, 6, 7]

result = []
carry = 0

for i in range(len(l1)):
    total = l1[i] + l2[i] + carry

    if i == len(l1) - 1:
        result.append(total)
    else:
        result.append(total % 10)
        carry = total // 10

print(result)