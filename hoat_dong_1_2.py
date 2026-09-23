# HOAT DONG 1: CAU TRUC DIEU KIEN IF - ELIF - ELSE
# 1.3: Điều kiện lồng nhau

tuoi = 17
co_giay_phep =False

if tuoi >= 18:
    if co_giay_phep:
        print("Được phép lái xe")
    else:
        print("Đủ tuổi nhưng chưa có giấy phép lái xe")
else:
    print("Chưa đủ tuổi lái xe")

# 1.4: Biểu thức điều kiện rút gọn

diem = 4.5
ket_qua ="Đạt" if diem >= 5 else "Không đạt"
print(ket_qua)

so = -7
tri_tuyet_doi = so if so >= 0 else -so
print(tri_tuyet_doi)

# HOAT DONG 2: VAN DUNG IF - SAP XEP HOC LUC, TIM SO LON NHAT
# 2.1: Xep hoc lục đẩy đủ

ho_ten = "Nguyễn Mai Anh"
diem_toan, diem_ly, diem_hoa = 8.0, 7.5, 9.0

dtb = round((diem_toan + diem_ly + diem_hoa) / 3, 2)

if dtb >= 8:
    xep_loai = "Giỏi"
elif dtb >= 6.5:
    xep_loai = "Khá"
elif dtb >= 5:
    xep_loai = "Trung binh"
else:
    xep_loai = "Yếu"

print(f"{ho_ten} - DTB: {dtb} Xếp loại: {xep_loai}")

# 2.2: Tìm số lớn nhât trong 3 số
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))

if a >= b and a >= c:
    lon_nhat = a
elif b >= a and b >= c:
    lon_nhat = b
else:
    lon_nhat = c
print("Số lớn nhất là: ", lon_nhat)