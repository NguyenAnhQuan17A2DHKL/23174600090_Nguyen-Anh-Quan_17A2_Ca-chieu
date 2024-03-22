#Hàm chuyển đổi số thành chữ:
def so_thanh_chu(n):
    duoi_20 = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    so_co_hang_dv_la_0 = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    doc_100 = {100: 'Hundred', 1000: 'Thousand'}

    if n < 20:
        return duoi_20[n]
    elif n < 100:
        return so_co_hang_dv_la_0[(n//10)-2] + ('' if n%10 == 0 else ' ' + duoi_20[n%10])
    else:
        return duoi_20[n//100] + ' Hundred' + ('' if n%100 == 0 else ' ' + so_thanh_chu(n%100))

#Nhập và xét chương trình:
if __name__ == '__main__':
    number = int(input("Nhập vào một số nguyên có ba chữ số: "))
    if 100 <= number <= 999:
        print("Cách đọc số nguyên này là:", so_thanh_chu(number))
    else:
        print("Xin hãy nhập một số có ba chữ số")