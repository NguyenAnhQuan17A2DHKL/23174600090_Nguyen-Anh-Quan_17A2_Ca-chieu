def sum_of_divisors(num):
    #Tính tổng các ước số chính của một số:
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum

def are_amicable(num1, num2):
    #Kiểm tra xem hai số có phải là cặp số amicable hay không:
    return sum_of_divisors(num1) == num2 and sum_of_divisors(num2) == num1

#Ví dụ sử dụng:
num1 = 220
num2 = 284
if are_amicable(num1, num2):
    print(f"{num1} và {num2} là một cặp số amicable")
else:
    print(f"{num1} và {num2} không phải là một cặp số amicable")