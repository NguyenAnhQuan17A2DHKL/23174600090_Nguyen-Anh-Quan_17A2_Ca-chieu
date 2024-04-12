#Nhập chuỗi từ bàn phím:
chuoi = input("Nhập một chuỗi: ")

#Tạo một từ điển để lưu trữ số lần xuất hiện của ký tự đặc biệt:
ky_tu_dac_biet = {}

#Duyệt qua từng ký tự trong chuỗi:
for ky_tu in chuoi:
    #Kiểm tra xem ký tự có phải là ký tự đặc biệt không (Không phải chữ và không phải số):
    if not ky_tu.isalnum():
        #Nếu là ký tự đặc biệt, tăng số lần xuất hiện trong từ điển:
        ky_tu_dac_biet[ky_tu] = ky_tu_dac_biet.get(ky_tu, 0) + 1

#Tính tổng số ký tự trong chuỗi:
tong_so_ky_tu = len(chuoi)

#In ra số lần xuất hiện và tỷ lệ phần trăm của từng ký tự đặc biệt:
for ky_tu, so_lan in ky_tu_dac_biet.items():
    ty_le_phan_tram = (so_lan / tong_so_ky_tu) * 100
    print(f"Ký tự '{ky_tu}' xuất hiện {so_lan} lần, chiếm {ty_le_phan_tram:.2f}% tổng số ký tự trong chuỗi")