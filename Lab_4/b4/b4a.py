#Câu a:
n = int(input("Nhập vào số nguyên n (n > 10): "))
if n > 10:
    i = 0
    S1 = 1
    while i <= n:
        S1 += 6 ** i
        if S1 > n:
            break
        i += 1
    print("S1 =", S1)
else:
    print("Vui lòng nhập số nguyên lớn hơn 10.")