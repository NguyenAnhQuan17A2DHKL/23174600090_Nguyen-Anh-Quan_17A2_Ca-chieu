#Chuỗi ban đầu và chuỗi mục tiêu:
chuoi_ban_dau = "chuoi1"
chuoi_muc_tieu = "chuoi2"

#Khởi tạo biến:
len1, len2 = len(chuoi_ban_dau), len(chuoi_muc_tieu)
i = j = count = 0
co_the_chuyen_doi = True

#Kiểm tra xem có thể chuyển đổi hay không:
if abs(len1 - len2) > 1:
    co_the_chuyen_doi = False

while i < len1 and j < len2:
    if chuoi_ban_dau[i] != chuoi_muc_tieu[j]:
        if count == 1:
            co_the_chuyen_doi = False
            break
        if len1 > len2:
            i += 1
        elif len1 < len2:
            j += 1
        else:
            i += 1
            j += 1
        count += 1
    else:
        i += 1
        j += 1

if i < len1 or j < len2:
    count += 1

if count > 1:
    co_the_chuyen_doi = False

#In kết quả:
print("Có thể chuyển đổi:", co_the_chuyen_doi)