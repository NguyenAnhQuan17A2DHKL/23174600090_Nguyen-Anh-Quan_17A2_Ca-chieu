#Danh sách các thể loại phim và thời gian chiếu:
the_loai_phim = {
    'Hành động': ['Sáng', 'Trưa', 'Chiều', 'Tối'],
    'Kinh dị': ['Tối'],
    'Tình cảm': ['Tối'],
    'Hài hước': ['Sáng', 'Trưa', 'Chiều', 'Tối'],
    'Hoạt hình': ['Sáng', 'Trưa']
}

#Hàm hiển thị thông báo suất chiếu phim:
def thong_bao_suat_chieu(the_loai, thoi_gian):
    if thoi_gian in the_loai_phim[the_loai]:
        print(f"Phim {the_loai} được chiếu vào buổi {thoi_gian}")
    else:
        print("Không có suất chiếu")

#Nhập chương trình và hiển thị thông báo:
if __name__ == "__main__":
    #Hiển thị các lựa chọn thể loại phim:
    print("Các thể loại phim có sẵn: Hành động, Kinh dị, Tình cảm, Hài hước, Hoạt hình")
    
    #Yêu cầu người dùng nhập lựa chọn:
    the_loai = input("Nhập thể loại phim bạn muốn xem: ")
    thoi_gian = input("Nhập thời gian bạn muốn xem phim (Sáng, Trưa, Chiều, Tối): ")
    
    #Kiểm tra và hiển thị thông báo:
    if the_loai in the_loai_phim:
        thong_bao_suat_chieu(the_loai, thoi_gian)
    else:
        print("Thể loại phim không hợp lệ")