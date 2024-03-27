#Hàm tính các tổng:
def tinh_tong_chuoi(n):
    #Tính tổng chuỗi số thứ nhất:
    s_1 = sum([i for i in range(1, n+1)])
    
    #Tính tổng chuỗi số thứ hai:
    s_2 = sum([i**2 for i in range(1, n+1)])
    
    #Tính tổng chuỗi số thứ ba:
    s_3 = sum([1/i for i in range(1, n+1)])
    
    #Tính tổng chuỗi số thứ tư:
    s_4 = sum([(-1)**(i+1) for i in range(1, n+1)])
    
    return s_1, s_2, s_3, s_4

#Nhập số nguyên dương và in ra kết quả:
n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("Vui lòng nhập lại")
    exit()
ket_qua = tinh_tong_chuoi(n)
print(f"Tổng chuỗi số cho n={n} là: {ket_qua}")