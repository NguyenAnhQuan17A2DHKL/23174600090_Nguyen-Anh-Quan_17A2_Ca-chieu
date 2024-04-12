#Nhập số nguyên dương:
so_nguyen_duong = int(input("Nhập số nguyên dương: "))

#Tạo chuỗi nhị phân:
nhi_phan = ''

#Kiểm tra nếu số nhập vào là 0:
if so_nguyen_duong == 0:
    nhi_phan = '0'
else:
    #Chuyển đổi số thập phân sang nhị phân:
    while so_nguyen_duong > 0:
        nhi_phan = str(so_nguyen_duong % 2) + nhi_phan
        so_nguyen_duong = so_nguyen_duong // 2

#In ra kết quả:
print("Số nhị phân là:", nhi_phan)