#Nhập thông số của hai đường thẳng:
a1 = float(input("Nhập hệ số góc của đường thẳng thứ nhất: "))
b1 = float(input("Nhập hệ số tự do của đường thẳng thứ nhất: "))
a2 = float(input("Nhập hệ số góc của đường thẳng thứ hai: "))
b2 = float(input("Nhập hệ số tự do của đường thẳng thứ hai: "))

#Hàm kiểm tra vị trí tương đối:
def kiem_tra_vitri_tuongdoi(a1, b1, a2, b2):
    if a1 == a2:
        if b1 == b2:
            return "Hai đường thẳng trùng nhau"
        else:
            return "Hai đường thẳng song song"
    elif a1 * a2 == -1:
        return "Hai đường thẳng vuông góc"
    else:
        return "Hai đường thẳng cắt nhau"

#In ra kết quả:
print(kiem_tra_vitri_tuongdoi(a1, b1, a2, b2))