#Nhập dãy số từ bàn phím:
day_so = list(map(int, input("Nhập vào dãy số nguyên, cách nhau bởi dấu cách: ").split()))

#Giả sử ban đầu dãy số là cấp số cộng:
la_cap_so_cong = True

#Lấy sai số giữa hai phần tử đầu tiên làm sai số cố định để so sánh:
if len(day_so) > 1:
    sai_so = day_so[1] - day_so[0]

#Kiểm tra sai số giữa các phần tử liên tiếp:
for i in range(len(day_so) - 1):
    if day_so[i + 1] - day_so[i] != sai_so:
        la_cap_so_cong = False
        break

#In ra kết quả:
if la_cap_so_cong and len(day_so) > 1:
    print(f"Dãy số {day_so} tạo thành cấp số cộng")
elif len(day_so) == 1:
    print("Dãy số chỉ có một phần tử, không thể xác định là cấp số cộng")
else:
    print("Dãy số không tạo thành cấp số cộng")