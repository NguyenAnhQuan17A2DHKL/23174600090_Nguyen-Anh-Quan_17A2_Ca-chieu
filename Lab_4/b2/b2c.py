#Câu c: Các số Fibonacci nhỏ hơn 1000:
a, b = 0, 1
while a < 1000:
    print(a, end=' ')
    a, b = b, a + b