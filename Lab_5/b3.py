#Nhập vào chuỗi văn bản và từ cần tìm kiếm:
chuoi_van_ban = input("Nhập vào chuỗi văn bản: ")
tu_can_tim = input("Nhập vào từ cần tìm kiếm: ")

#Tìm vị trí của từ trong chuỗi:
vi_tri = chuoi_van_ban.find(tu_can_tim)
if vi_tri != -1:
    print(f"Vị trí của từ '{tu_can_tim}' trong chuỗi là: {vi_tri}")
else:
    print(f"Từ '{tu_can_tim}' không xuất hiện trong chuỗi")

#Kiểm tra từ xuất hiện nhiều nhất trong chuỗi:
tu_xuat_hien_nhieu_nhat = ''
so_lan_xuat_hien_nhieu_nhat = 0
cac_tu = chuoi_van_ban.split()

for tu in cac_tu:
    so_lan_xuat_hien = cac_tu.count(tu)
    if so_lan_xuat_hien > so_lan_xuat_hien_nhieu_nhat:
        tu_xuat_hien_nhieu_nhat = tu
        so_lan_xuat_hien_nhieu_nhat = so_lan_xuat_hien

print(f"Từ xuất hiện nhiều nhất là '{tu_xuat_hien_nhieu_nhat}' với {so_lan_xuat_hien_nhieu_nhat} lần")