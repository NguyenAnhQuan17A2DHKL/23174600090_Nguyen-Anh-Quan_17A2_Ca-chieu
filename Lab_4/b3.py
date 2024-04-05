#Nhập số nguyên:
number = int(input("Nhập một số nguyên: "))

#Khởi tạo biến đếm số chữ số:
count = 0

#Sử dụng vòng lặp while để đếm số chữ số:
while number != 0:
    count += 1
    number //= 10

#In ra số chữ số của số nguyên:
print(f"Số chữ số của số nguyên: {count}")