#Câu b: Số chính phương nhỏ hơn 100:
n = 1
while n < 100:
    if int(n**0.5)**2 == n:
        print(n, end=' ')
    n += 1