n = int(input("Nhập vào số nguyên n (n>10): "))   
if n>10:    
   a=0    
   s=0    
   while True:      
       a+=1       
       s+=(-1)**a * a**2       
       if s>n:          
           break     
   print(f"S3={s}")   
else:     
     print("Vui lòng nhập số nguyên lớn hơn 10")  