#Yêu cầu người dùng nhập số lượng phần tử của mảng:
n = int(input("Nhập số lượng phần tử của mảng: "))

#Tạo mảng để lưu trữ các số nguyên dương:
mang = []

#Nhập các phần tử vào mảng:
for i in range(n):
    so = int(input(f"Nhập số nguyên dương thứ {i+1}: "))
    mang.append(so)

#Tạo biến để tính tổng số chẵn và số lẻ:
tong_chan = 0
tong_le = 0

#Phân loại và tính tổng:
for so in mang:
    if so % 2 == 0:
        tong_chan += so
    else:
        tong_le += so

#In ra kết quả:
print(f"Tổng của các số chẵn trong mảng là: {tong_chan}")
print(f"Tổng của các số lẻ trong mảng là: {tong_le}")