#Hàm kiểm tra số nguyên tố:
snt = lambda num: all(num % i != 0 for i in range(2, int(num**0.5) + 1)) and num > 1

#Hàm kiểm tra số hoàn hảo:
shh = lambda num: sum(i for i in range(1, num) if num % i == 0) == num

#Nhập mảng số nguyên dương từ bàn phím:
n = int(input("Nhập số lượng phần tử của mảng: "))
m = [int(input(f"Nhập phần tử thứ {i+1}: ")) for i in range(n)]

#Tìm và in ra màn hình tất cả các số nguyên tố trong mảng:
print("Các số nguyên tố trong mảng:", [num for num in m if snt(num)])

#Tìm và in ra màn hình tất cả các số hoàn hảo trong mảng:
print("Các số hoàn hảo trong mảng:", [num for num in m if shh(num)])