def isPalindrome():
    x = 12345
    l1 = []
    original = x
    while x > 0:
        r = x % 10
        l1.append(r)
        x = x // 10   

    num = 0
    for i in range(len(l1)):
        num = num + l1[i] * (10 ** (len(l1) - i - 1))

    
    # print(x,num)
    if num == original:
        return True
    else:
        return False
isPalindrome()

        