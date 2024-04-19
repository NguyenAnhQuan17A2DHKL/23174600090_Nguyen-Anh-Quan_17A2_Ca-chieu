#Nhập dãy số:
day_so = input("Nhập dãy số, cách nhau bằng dấu phẩy: ")

#Tách các số thành danh sách:
danh_sach_so = day_so.split(",")

#Tạo biến lớn nhất và nhỏ nhất:
max_number = float("-inf")
min_number = float("inf")

#Tìm số lớn nhất và số nhỏ nhất:
for num in danh_sach_so:
    try:
        current_number = float(num)
        if current_number > max_number:
            max_number = current_number
        if current_number < min_number:
            min_number = current_number
    except ValueError:
        print(f"Không thể chuyển đổi '{num}' thành số. Bỏ qua...")

#In ra kết quả:
print(f"Số lớn nhất trong dãy số là: {max_number}")
print(f"Số nhỏ nhất trong dãy số là: {min_number}")