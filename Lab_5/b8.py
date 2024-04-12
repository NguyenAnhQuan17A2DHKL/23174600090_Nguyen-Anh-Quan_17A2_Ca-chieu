#Nhập chuỗi ký tự đầu vào:
input_string = input("Nhập chuỗi ký tự: ")

#a)Trích ra chuỗi ký tự con từ vị trí thứ 2 đến vị trí thứ 8:
substring_a = input_string[1:8]

#b)Trích ra chuỗi ký tự con gồm 5 ký tự kể từ vị trí thứ 5:
substring_b = input_string[4:9]

#c)Trích ra chuỗi ký tự con từ cuối chuỗi gồm 3 ký tự:
substring_c = input_string[-3:]

#d)Chuyển đổi các ký tự trong chuỗi thành chữ thường:
lowercase_string = input_string.lower()

#e)Chuyển đổi các ký tự trong chuỗi thành chữ hoa:
uppercase_string = input_string.upper()

#f)Đảo ngược chuỗi ký tự vừa nhập
reversed_string = input_string[::-1]

#In kết quả:
print("Chuỗi ký tự con từ vị trí thứ 2 đến vị trí thứ 8:", substring_a)
print("Chuỗi ký tự con gồm 5 ký tự từ vị trí thứ 5:", substring_b)
print("Chuỗi ký tự con từ cuối chuỗi gồm 3 ký tự:", substring_c)
print("Chuỗi chữ thường:", lowercase_string)
print("Chuỗi chữ hoa:", uppercase_string)
print("Chuỗi đảo ngược:", reversed_string)