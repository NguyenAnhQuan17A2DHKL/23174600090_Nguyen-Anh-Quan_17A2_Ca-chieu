def main():
    #Số lượng viên bi trong hộp:
    tat_ca_bi = 50
    #Số lượng viên bi màu đỏ, xanh và vàng:
    bi_do = 20
    bi_xanh = 15
    bi_vang = 15

    #Nhập số lượng viên bi muốn rút:
    n = int(input("Nhập số lượng viên bi muốn rút: "))

    #Tính xác suất cho từng trường hợp:
    #1. Tất cả là bi đỏ:
    tat_ca_la_bi_do = (bi_do / tat_ca_bi) ** n

    #2. Ít nhất một viên là bi xanh (complement của không có viên bi xanh):
    it_nhat_1_bi_xanh = 1 - (bi_xanh / tat_ca_bi) ** n

    #3. Đúng hai viên là bi vàng:
    dung_2_vien_la_bi_vang = (bi_vang / tat_ca_bi) ** 2 * ((tat_ca_bi - bi_vang) / tat_ca_bi) ** (n - 2)

    #Hiển thị kết quả:
    print(f"Xác suất tất cả là bi đỏ: {tat_ca_la_bi_do:.4f}")
    print(f"Xác suất ít nhất một viên là bi xanh: {it_nhat_1_bi_xanh:.4f}")
    print(f"Xác suất đúng hai viên là bi vàng: {dung_2_vien_la_bi_vang:.4f}")

if __name__ == "__main__":
    main()
