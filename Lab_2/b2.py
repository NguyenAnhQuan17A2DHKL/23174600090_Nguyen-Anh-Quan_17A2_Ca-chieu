#Nhận vào một số nguyên từ người dùng:
so_nguyen = int(input("Nhập một số nguyên: "))

#Tính chữ số hàng nghìn:
chu_so_hang_nghin = (so_nguyen // 1000) % 10

#Xuất ra chữ số hàng nghìn của số đó, nếu không có thì xuất ra 0:
print("Chữ số hàng nghìn của số đó là:", chu_so_hang_nghin)