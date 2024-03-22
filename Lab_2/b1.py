#Nhập các hệ số a và b:
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))

#Giải và biện luận phương trình bậc nhất:
if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    x = -b / a
    print(f"Phương trình có nghiệm duy nhất: x = {x}")