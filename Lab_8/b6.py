#Hàm kiểm tra số lẻ:
def so_le(num):
    return num % 2 != 0

#Danh sách ban đầu:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#Lọc số lẻ:
loc_so_le = list(filter(so_le, numbers))
print(loc_so_le)


#Hàm kiểm tra số chẵn:
def so_chan(num):
    return num % 2 == 0

#Danh sách ban đầu:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#Lọc số chẵn:
loc_so_chan = list(filter(so_chan, numbers))
print(loc_so_chan)


#Hàm tính lập phương:
def cube(num):
    return num ** 3

# Danh sách ban đầu:
numbers = [1, 2, 3, 4, 5]

#Tạo danh sách lập phương:
cubed_numbers = list(map(cube, numbers))
print(cubed_numbers)


#Kết hợp filter và map:
even_cubed_numbers = list(map(cube, filter(so_chan, numbers)))
print(even_cubed_numbers)


#Hàm tính bình phương:
def square(num):
    return num ** 2

#Kết hợp filter và map:
odd_squared_numbers = list(map(square, filter(so_le, numbers)))
print(odd_squared_numbers)