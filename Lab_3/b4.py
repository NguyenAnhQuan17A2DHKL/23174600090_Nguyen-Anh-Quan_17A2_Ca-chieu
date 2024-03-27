#Vẽ hình 1:
def hinh_1(n):
    for i in range(n):
        print(' ' * (n-i-1) + '* ' * (i+1))
    for i in range(1):  
        print('* ' * 5) 
    for i in range(n-1):
        print(' ' * (i+1) + '* ' * (n-i-1))
hinh_1(5)

#Vẽ hình 2: 
#Số lượng dòng:
n = 7
# Vẽ hình sao:
for i in range(n):
    print(' ' * (n-i-1) + '*' * (2*i+1))
#Vẽ hình chữ nhật dọc:
#Số dòng và cột:
rows = 3
cols = 3
#Vẽ hình chữ nhật:
for i in range(rows):
    print((' ' * 5 + '*' * (cols)))