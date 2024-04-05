#Tạo danh sách các từ tương ứng với các chữ số:
so_sang_tu = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

#Nhập số từ bàn phím:
number = input("Nhập một số: ")

#In ra màn hình bằng chữ tiếng anh:
for digit in number:
    print(so_sang_tu[int(digit)], end=" ")