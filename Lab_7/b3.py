#Đoạn văn bản cần phân tích:
text = "I m a student of 8th class. I like all my subjects but English attracts me the most. Reading short stories is my favorite pastime. I want to become a story writer like Ruskin Bond. I want to write stories for children which convey a moral message in very subtle way. Children will enjoy the story and messages will slip silently in their mind. Messages should not be loud. I believe this is the best way of passing knowledge to the children without preaching and very less teaching."

#Loại bỏ dấu câu và chuyển tất cả thành chữ thường:
loai = ''.join(char.lower() if char.isalnum() or char.isspace() else ' ' for char in text)

#Tách từ và tạo từ điển đếm số lượng:
dem = {}
for word in loai.split():
    dem[word] = dem.get(word, 0) + 1

#Tìm từ có số lượng nhiều nhất và ít nhất:
tu_nhieu_nhat = max(dem, key=dem.get)
tu_it_nhat = min(dem, key=dem.get)

#In kết quả:
print(f"Từ xuất hiện nhiều nhất: '{tu_nhieu_nhat}' với {dem[tu_nhieu_nhat]} lần")
print(f"Từ xuất hiện ít nhất: '{tu_it_nhat}' với {dem[tu_it_nhat]} lần")