#Nhập hai chuỗi:
string1 = input("Nhập chuỗi thứ nhất: ")
string2 = input("Nhập chuỗi thứ hai: ")

#Cả hai chuỗi đều có cùng độ dài bằng cách thêm khoảng trắng vào cuối chuỗi ngắn hơn:
max_len = max(len(string1), len(string2))
string1 = string1.ljust(max_len)
string2 = string2.ljust(max_len)

#Khởi tạo chuỗi kết quả:
result = ""

#Duyệt qua từng cặp ký tự và thêm vào chuỗi kết quả:
for i in range(max_len):
    result += string1[i] + '-' + string2[i]

#Loại bỏ dấu gạch nối cuối cùng:
result = result.rstrip('-')

#In kết quả:
print(result)