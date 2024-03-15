#Nhập các hệ số:
a1,b1,c1 = map(float, input("Nhập lần lượt hệ số của phương trình 1: ").split())
a2,b2,c2 = map(float, input("Nhập lần lượt hệ số của phương trình 2: ").split())

#Tính định thức:
det = a1 * b2 - a2 * b1

#Tính giá trị của x và y:
x = (c1 * b2 - c2 * b1) / det
y = (a1 * c2 - a2 * c1) / det

#In kết quả: 
print("Kết quả của hệ phương trình là:")
print("x =", round(x,2))
print("y =", round(y,2))