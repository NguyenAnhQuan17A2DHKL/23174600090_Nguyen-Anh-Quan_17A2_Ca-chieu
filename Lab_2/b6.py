#Nhập ba số nguyên từ bàn phím:
n1 = int(input("Nhập số nguyên thứ nhất: "))
n2 = int(input("Nhập số nguyên thứ hai: "))
n3 = int(input("Nhập số nguyên thứ ba: "))

#Hàm để tìm số lớn thứ hai:
def tim_so_lon_thu_hai(numbers):
    first, second = float('-inf'), float('-inf')
    for number in numbers:
        if number > first:
            second = first
            first = number
        elif first > number > second:
            second = number
    return second

#Tìm và in ra số lớn thứ hai:
so_lon_thu_hai = tim_so_lon_thu_hai([n1, n2, n3])
print("Số lớn thứ hai trong các số nguyên đó là:", so_lon_thu_hai)