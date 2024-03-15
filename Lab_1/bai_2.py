#Nhập thông tin:
ma_sach = int(input("Nhập mã sách: "))
ten_sach = (input("Nhập tên sách: "))
tac_gia = (input("Nhập tên tác giả: "))
nam_xuat_ban = int(input("Nhập năm xuất bản: "))
so_luong_sach = int(input("Nhập số lượng sách: "))

#In ra màn hình:
print(f"Thư viện ĐHKTKTCN có {so_luong_sach} sách {ten_sach} với mã số {ma_sach}.\nCuốn sách của tác giả {tac_gia} được xuất bản vào năm {nam_xuat_ban}")