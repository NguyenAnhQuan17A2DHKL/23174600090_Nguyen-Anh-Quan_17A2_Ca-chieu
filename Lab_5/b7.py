#Chuỗi nhập vào:
chuoi = input("Nhập chuỗi của bạn: ")

#Khởi tạo bộ đếm:
so_chu_hoa = 0
so_chu_thuong = 0
so_chu_so = 0
so_ky_tu_dac_biet = 0

#Đếm các loại ký tự:
for ky_tu in chuoi:
    if ky_tu.isupper():
        so_chu_hoa += 1
    elif ky_tu.islower():
        so_chu_thuong += 1
    elif ky_tu.isdigit():
        so_chu_so += 1
    else:
        so_ky_tu_dac_biet += 1

#In kết quả:
print("Số chữ hoa:", so_chu_hoa)
print("Số chữ thường:", so_chu_thuong)
print("Số chữ số:", so_chu_so)
print("Số ký tự đặc biệt:", so_ky_tu_dac_biet)