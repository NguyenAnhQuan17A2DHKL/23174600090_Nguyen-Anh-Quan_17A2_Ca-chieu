#Nhập số n:
n = int(input("Nhập số n: "))

#Tạo danh sách Fibonacci sử dụng list comprehension:
ds_fibonacci = [0, 1] + [ds_fibonacci[-1] + ds_fibonacci[-2] for _ in range(n - 2)]

#Tạo danh sách số nguyên tố sử dụng list comprehension:
ds_snt = [num for num in range(2, 100) if all(num % i != 0 for i in range(2, int(num**0.5) + 1))]

#In ra danh sách Fibonacci và danh sách số nguyên tố:
print(f"Dãy Fibonacci gồm {n} số đầu tiên: {ds_fibonacci}")
print(f"Danh sách số nguyên tố nhỏ hơn 100: {ds_snt}")