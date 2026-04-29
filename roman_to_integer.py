d = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

roman_num = "XXVI"
total = 0

for i in range(len(roman_num)):
    if i < len(roman_num) - 1 and d[roman_num[i]] < d[roman_num[i+1]]:
        total -= d[roman_num[i]]
    else:
        total += d[roman_num[i]]

print(total)