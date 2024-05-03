#Nhập số nguyên N:
N = int(input("Nhập số nguyên N: "))

#Tạo từ điển:
sv_dict = {}
for x in range(1, N + 1):
    sv_dict[x] = x ** 3

#In từ điển:
print("Từ điển với độ dài", N, "là:")
for key, value in sv_dict.items():
    print(f"{key}: {value}")