#Hàm tính tổng số tiền phải trả khi mua vé dựa trên số lượng người:
def tinh_tong_tien(so_nguoi):
    gia_ve = 120000  #Giá vé cho 1 người
    tong_tien = so_nguoi * gia_ve

    #Áp dụng các mức giảm giá dựa trên số lượng người:
    if 2 <= so_nguoi <= 4:
        tong_tien *= 0.95  #Giảm 5% số tiền
    elif 5 <= so_nguoi <= 10:
        tong_tien *= 0.90  #Giảm 10% số tiền
    elif so_nguoi > 10:
        tong_tien *= 0.80  #Giảm 20% số tiền

    return tong_tien

#Nhập số lượng người:
so_nguoi = int(input("Nhập số lượng người: "))

#Tính và in ra tổng số tiền phải trả:
tong_tien = tinh_tong_tien(so_nguoi)
print(f"Tổng số tiền phải trả là: {tong_tien} đồng")