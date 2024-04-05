#Tạo biến để kiểm tra xem người dùng có muốn tiếp tục hay không:
tiep_tuc = True

while tiep_tuc:
    #Nhập 2 số từ người dùng:
    a = float(input("Nhập số thứ nhất: "))
    b = float(input("Nhập số thứ hai: "))
    
    #Các phép tính:
    tong = a + b
    hieu = a - b
    tich = a * b
    thuong = a / b
    luy_thua = a ** b
    can_bac_hai_a = a ** 0.5
    can_bac_hai_b = b ** 0.5
    
    #In ra kết quả:
    print(f"Số thứ nhất + Số thứ hai = {tong}")
    print(f"Số thứ nhất - Số thứ hai = {hieu}")
    print(f"Số thứ nhất * Số thứ hai = {tich}")
    print(f"Số thứ nhất / Số thứ hai = {thuong}")
    print(f"Số thứ nhất ^ Số thứ hai = {luy_thua}")
    print(f"Căn bậc hai của số thứ nhất = {can_bac_hai_a}")
    print(f"Căn bậc hai của số thứ hai = {can_bac_hai_b}")
    
    #Hỏi người dùng có muốn tiếp tục không:
    lua_chon = input("Bạn có muốn tiếp tục không? (Nhập 'yes' hoặc 'no'): ")
    if lua_chon.lower() != 'yes':
        tiep_tuc = False