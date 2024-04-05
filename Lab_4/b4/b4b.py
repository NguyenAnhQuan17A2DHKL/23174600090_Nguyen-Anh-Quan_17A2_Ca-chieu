#Câu b:
n = int(input("Nhập vào số nguyên n (n > 10): "))
if n > 10:
    i = 3 
    S2 = 0 
    while True: 
        term = (i - 2) / (i**3) 
        S2 += term 
        if S2 + ((i+1)-2)/((i+1)**3) > n: 
            break 
        i += 3  
        
    print(f"S2 ={S2}")  
else:   
     print("Vui lòng nhập số nguyên lớn hơn 10") 