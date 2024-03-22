#Nhập thông số của đường thẳng:
m = float(input("Nhập hệ số góc của đường thẳng (m): "))
c = float(input("Nhập hệ số tự do của đường thẳng (c): "))

#Nhập thông số của đường tròn:
td_x = float(input("Nhập tọa độ x của tâm đường tròn: "))
td_y = float(input("Nhập tọa độ y của tâm đường tròn: "))
ban_kinh = float(input("Nhập bán kính của đường tròn: "))

import math

#Hàm tính khoảng cách từ tâm đường tròn đến đường thẳng:
def khoang_cach_tu_tam_dtron_den_dthang(m, c, tam_duong_tron):
    x0, y0 = tam_duong_tron
    return abs(m*x0 - y0 + c) / math.sqrt(m**2 + 1)

#Hàm xác định vị trí tương đối:
def vi_tri_tuong_doi(m, c, tam_duong_tron, ban_kinh):
    distance = khoang_cach_tu_tam_dtron_den_dthang(m, c, tam_duong_tron)
    if distance > ban_kinh:
        return "Đường thẳng nằm ngoài đường tròn"
    elif distance == ban_kinh:
        return "Đường thẳng tiếp xúc đường tròn"
    elif distance < ban_kinh:
        return "Đường thẳng cắt đường tròn"

#Xác định và in ra kết quả:
ket_qua = vi_tri_tuong_doi(m, c, (td_x, td_y), ban_kinh)
print(ket_qua)