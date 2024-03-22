#Nhập điểm số:
diem_so = float(input("Nhập vào điểm số của bạn: "))

#Kiểm tra và in ra:
if 0 <= diem_so < 5:
    print("Điểm kém")
elif 5 <= diem_so < 7:
    print("Điểm trung bình")
elif 7 <= diem_so < 8.5:
    print("Điểm khá")
elif 8.5 <= diem_so <= 10:
    print("Điểm tốt")
else:
    print("Điểm số không hợp lệ")