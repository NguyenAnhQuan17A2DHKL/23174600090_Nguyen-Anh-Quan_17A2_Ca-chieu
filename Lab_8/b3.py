def cubesum(n):
    #Tính tổng của các lập phương của các chữ số riêng lẻ của số n:
    total = 0
    for digit in str(n):
        total += int(digit) ** 3
    return total

def PrintArmstrong():
    #In ra tất cả các số Armstrong:
    for num in range(1, 1000):  #Limit Armstrong numbers in (1, 99)
        if num == cubesum(num):
            print(num)

def isArmstrong(n):
    #Kiểm tra xem một số n có phải là số Armstrong hay không:
    return n == cubesum(n)

#Ví dụ sử dụng:
print("Tổng của các lập phương của các chữ số riêng lẻ của 123:", cubesum(123))
PrintArmstrong()
print("Is 153 là số Armstrong?", isArmstrong(153))