#Khởi tạo danh sách để lưu các số đã nhập:
so_nguyen_duong = []
so_le = []
so_chan = []

#Nhập các số nguyên dương từ bàn phím:
while True:
    try:
        so = int(input("Nhập số nguyên dương (nhập 0 để kết thúc): "))
        if so <= 0:
            break
        so_nguyen_duong.append(so)
        if so % 2 == 0:
            so_chan.append(so)
        else:
            so_le.append(so)
    except ValueError:
        print("Vui lòng nhập số nguyên dương hợp lệ.")

#Tính tổng các số đã nhập:
tong = sum(so_nguyen_duong)

#In ra kết quả:
print(f"Các số đã nhập từ bàn phím là: {', '.join(map(str, so_nguyen_duong))}")
print(f"Các số lẻ đã nhập là: {', '.join(map(str, so_le))}")
print(f"Các số chẵn đã nhập: {', '.join(map(str, so_chan))}")
print(f"Số lượng các số nguyên đã nhập: {len(so_nguyen_duong)}")