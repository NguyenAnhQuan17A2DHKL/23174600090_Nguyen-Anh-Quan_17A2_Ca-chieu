#Nhập các chuỗi:
str1 = input("Nhập chuỗi thứ nhất: ")
str2 = input("Nhập chuỗi thứ hai: ")

#Tạo biến để lưu chuỗi con chung ngắn nhất:
chuoi_con_chung_ngan_nhat = None

#Tìm chuỗi con chung ngắn nhất:
for i in range(len(str1)):
    for j in range(len(str2)):
        l = 0  #(Độ dài của chuỗi con chung tạm thời)
        
        #Tìm chuỗi con chung bắt đầu từ str1[i] và str2[j]:
        while (i + l < len(str1) and j + l < len(str2) and str1[i + l] == str2[j + l]):
            l += 1
        #Cập nhật chuỗi con chung ngắn nhất nếu cần:
        if l > 0:
            update_chuoicon = str1[i:i + l]
            if chuoi_con_chung_ngan_nhat is None or len(update_chuoicon) < len(chuoi_con_chung_ngan_nhat):
                chuoi_con_chung_ngan_nhat = update_chuoicon

#In kết quả:
if chuoi_con_chung_ngan_nhat:
    print("Chuỗi con chung ngắn nhất là:", chuoi_con_chung_ngan_nhat)
else:
    print("Không có chuỗi con chung")