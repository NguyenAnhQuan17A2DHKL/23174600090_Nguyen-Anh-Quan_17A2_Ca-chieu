#Chuỗi đầu vào:
chuoi_dau_vao = input("Nhập chuỗi đầu vào: ")

#Loại bỏ các ký tự không phải số:
chuoi_so = ''.join([char for char in chuoi_dau_vao if '0' <= char <= '9'])

#Chuyển đổi chuỗi số thành số nguyên:
so_nguyen = int(chuoi_so)

#Kiểm tra số nguyên tố:
la_so_nguyen_to = True
if so_nguyen < 2:
    la_so_nguyen_to = False
else:
    for i in range(2, int(so_nguyen**0.5) + 1):
        if so_nguyen % i == 0:
            la_so_nguyen_to = False
            break

#In kết quả:
if la_so_nguyen_to:
    print(f"{so_nguyen} là số nguyên tố")
else:
    print(f"{so_nguyen} không phải là số nguyên tố")