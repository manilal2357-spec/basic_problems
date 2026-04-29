strs = ["ram", "rayam", "rani", "raja"]

prefix = ""
smallest_word = min(strs, key=len)

for i in range(len(smallest_word)):
    for j in range(len(strs)):
        if strs[j][i] != smallest_word[i]:
            print(prefix)
            exit()
    prefix += smallest_word[i]

print(prefix)