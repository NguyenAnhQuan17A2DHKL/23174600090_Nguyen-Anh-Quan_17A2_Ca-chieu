def sumPdivisors(num):
    divisors = [1] 
    for i in range(2, num):
        if num % i == 0:
            divisors.append(i)
    return sum(divisors)

#Ví dụ sử dụng hàm
number = 50
print(f"Tổng các ước số chính của số {number} là: {sumPdivisors(number)}")