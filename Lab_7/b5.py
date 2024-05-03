#Từ điển kho và giá tiền:
kho = {
 "banana": 6,
 "apple": 5,
 "orange": 32,
 "pear": 15
}

gia_tien = {
 "banana": 4,
 "apple": 2,
 "orange": 1.5,
 "pear": 3
}

#Tạo hóa đơn:
hoa_don = {}
tong_tien = 0

print("Hóa đơn mua hàng:")
print("Mặt hàng\tSố lượng\tĐơn giá\tSố tiền")

for mat_hang in kho:
    so_luong = kho[mat_hang]
    don_gia = gia_tien[mat_hang]
    so_tien = so_luong * don_gia
    tong_tien += so_tien
    hoa_don[mat_hang] = {'Số lượng': so_luong, 'Đơn giá': don_gia, 'Số tiền': so_tien}
    print(f"{mat_hang}\t{so_luong}\t\t{don_gia}\t{so_tien}")

print(f"Tổng số tiền của hóa đơn: {tong_tien}")

#In lại số lượng hàng trong kho:
print("\nSố lượng hàng trong kho sau khi mua:")
for mat_hang in kho:
    print(f"{mat_hang}: {kho[mat_hang]}")