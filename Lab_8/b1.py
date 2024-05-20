def snt(n):
    #Kiểm tra số n có phải là số nguyên tố hay không:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def snt_doi(limit):
    #In ra các cặp số nguyên tố sinh đôi nhỏ hơn giới hạn:
    for i in range(2, limit):
        j = i + 2
        if snt(i) and snt(j):
            print(f"({i}, {j})")

#In ra các cặp số nguyên tố sinh đôi nhỏ hơn 1000:
snt_doi(1000)