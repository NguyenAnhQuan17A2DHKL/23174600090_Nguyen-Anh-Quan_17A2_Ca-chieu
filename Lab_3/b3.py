import math

#Câu a: In ra các số nguyên tố từ 100 đến 1000:
def so_nt(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

print("Các số nguyên tố từ 100 đến 1000 là:")
for i in range(100, 1001):
    if so_nt(i):
        print(i, end=' ')
print("\n")



#Câu b: In ra các số chính phương từ 1 đến 1000:
print("Các số chính phương từ 1 đến 1000 là:")
for i in range(1, 32):  
    print(i**2, end=' ')
print("\n")



#Câu c: In ra chuỗi Fibonacci sao cho số cuối cùng trong chuỗi nhỏ hơn 100:
def chuoi_fibonacci(limit):
    sequence = [0, 1]
    while True:
        next_value = sequence[-1] + sequence[-2]
        if next_value < limit:
            sequence.append(next_value)
        else:
            break
    return sequence

print("Chuỗi Fibonacci nhỏ hơn 100 là:")
print(chuoi_fibonacci(100))



#Câu d: In ra các số hoàn hảo bé hơn 500:
def so_hh(n):
    tong_cac_uoc_so = sum([i for i in range(1, n) if n % i == 0])
    return tong_cac_uoc_so == n

print("Các số hoàn hảo bé hơn 500 là:")
for i in range(1, 500):
    if so_hh(i):
        print(i, end=' ')
print("\n")



#Câu e: In ra tổng của các số ngũ giác từ 1 đến 200:
def so_ngu_giac(n):
    return n * (3*n - 1) // 2

print("Tổng của các số ngũ giác từ 1 đến 200 là:")
print(sum(so_ngu_giac(i) for i in range(1, 201)))