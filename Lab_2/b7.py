#Hàm tính chỉ số BMI:
def tinh_bmi(can_nang, chieu_cao):
    bmi = can_nang / (chieu_cao ** 2)
    return bmi

#Hàm phân loại chỉ số BMI:
def phan_loai_bmi(bmi):
    if bmi < 18.5:
        return "Gầy"
    elif 18.5 <= bmi <= 24.9:
        return "Bình thường"
    elif 25.0 <= bmi <= 29.9:
        return "Hơi béo"
    else:
        return "Béo"

#Nhập các thông số và in ra kết quả:
if __name__ == "__main__":
    chieu_cao = float(input("Nhập chiều cao (m): "))
    can_nang = float(input("Nhập cân nặng (kg): "))
    
    bmi = tinh_bmi(can_nang, chieu_cao)
    phan_loai = phan_loai_bmi(bmi)
    
    print(f"Chỉ số BMI của bạn là: {bmi:.2f}")
    print(f"Phân loại: {phan_loai}")