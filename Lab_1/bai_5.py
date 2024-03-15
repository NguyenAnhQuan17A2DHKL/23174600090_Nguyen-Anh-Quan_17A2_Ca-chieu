t = float(input("nhập vào số giờ cần tính: "))
U = 220
I = 1.5

#Điện năng tiêu thụ là: 
A = U*I*t 

#Đổi đơn vị Wh sang kWh: 
s = A/1000

#Tổng số tiền điện phải trả với thời gian t nhập vào là:
tien = s*5000
print("Tổng số tiền điện phải trả cho việc sử dụng máy lọc không khí với giá điện 5000 đồng/kWh là:", tien)