#Câu a: Số nguyên tố nhỏ hơn 100:
n = 2
while n < 100:
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n, end=' ')
    n += 1