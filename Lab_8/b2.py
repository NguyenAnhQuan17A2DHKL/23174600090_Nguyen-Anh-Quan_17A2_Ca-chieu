def factorial(n):
    #Tính giai thừa của n:
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def permutations(n, r):
    #Tính số hoán vị của n phần tử lấy r phần tử mỗi lần:
    return factorial(n) // factorial(n - r)

def combinations(n, r):
    #Tính số tổ hợp của n phần tử lấy r phần tử mỗi lần:
    return factorial(n) // (factorial(r) * factorial(n - r))

#Giá trị sử dụng:
n = 6
r = 2
print(f"Số hoán vị của {n} phần tử lấy {r} phần tử mỗi lần: {permutations(n, r)}")
print(f"Số tổ hợp của {n} phần tử lấy {r} phần tử mỗi lần: {combinations(n, r)}")