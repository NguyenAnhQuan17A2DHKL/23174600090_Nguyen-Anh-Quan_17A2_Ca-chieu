#Tạo danh sách chứa thông tin của 10 sinh viên:
sv = []
for i in range(10):
    ten = input(f"Nhập tên của sinh viên {i+1}: ")
    diem = float(input(f"Nhập điểm thi của sinh viên {i+1}: "))
    sv.append((ten, diem))

#Xếp loại học lực và thống kê:
xep_loai = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
for ten, diem in sv:
    if diem >= 8.5:
        xep_loai['A'] += 1
    elif diem >= 7.0:
        xep_loai['B'] += 1
    elif diem >= 5.5:
        xep_loai['C'] += 1
    elif diem >= 4.0:
        xep_loai['D'] += 1
    else:
        xep_loai['F'] += 1

#In kết quả:
print("\nXếp loại học lực của sinh viên:")
for xep_loai, count in xep_loai.items():
    print(f"{xep_loai}: {count} sinh viên")