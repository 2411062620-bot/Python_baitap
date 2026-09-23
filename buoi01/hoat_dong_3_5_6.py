# ============================================================
# HOẠT ĐỘNG 3: ĐỊNH DANH & CHUẨN ĐẶT TÊN PEP8
# ============================================================
print("=== HOẠT ĐỘNG 3 ===")
# Bài tập 3.2: Đặt lại tên biến theo đúng chuẩn PEP8
ten = "Nguyen Van A"
diem_toan = 8.5
diem_van = 7.0
so_luong_mon_hoc = 2
MUC_LUONG_TOI_THIEU = 5000000  # Hằng số viết hoa toàn bộ

print("Họ tên:", ten)
print("Điểm Toán:", diem_toan)
print("Điểm Văn:", diem_van)
print("Số lượng môn học:", so_luong_mon_hoc)
print("Mức lương tối thiểu:", MUC_LUONG_TOI_THIEU)


# ============================================================
# HOẠT ĐỘNG 5: TOÁN TỬ
# ============================================================
print("\n=== HOẠT ĐỘNG 5 ===")

# Bài tập 5.1: Toán tử số học
a = 17
b = 5
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)

# Bài tập 5.2: Toán tử so sánh & logic
diem = 6.5
tuoi = 20

la_khab = (diem >= 6.5) and (diem < 8.0)
chua_du_tuoi_hoac_gia = (tuoi < 18) or (tuoi > 60)
phu_dinh_dieu_kien = not (tuoi < 18 or tuoi > 60)

print("Đạt loại Khá?:", la_khab)
print("Chưa đủ 18 hoặc trên 60 tuổi?:", chua_du_tuoi_hoac_gia)
print("Phủ định điều kiện trên:", phu_dinh_dieu_kien)

# Bài tập 5.3: Toán tử gán & đặc biệt
x = 10
x += 5
print("x sau khi += 5:", x)
x -= 3
print("x sau khi -= 3:", x)
x *= 2
print("x sau khi *= 2:", x)
x /= 4
print("x sau khi /= 4:", x)
x //= 2
print("x sau khi //= 2:", x)
x **= 3
print("x sau khi **= 3:", x)

danh_sach = [1, 2, 3, "python"]
print("Kiem tra 3 co trong danh sach?:", 3 in danh_sach)

list1 = [1, 2, 3]
list2 = list1
print("list1 va list2 co cung trỏ toi 1 list?:", list1 is list2)

# Bài tập 5.4: Độ ưu tiên toán tử
print("Kết quả 2 + 3 * 4 ** 2 =", 2 + 3 * 4 ** 2)
print("Kết quả (2 + 3) * 4 ** 2 =", (2 + 3) * 4 ** 2)
print("Kết quả 10 > 5 and 3 < 1 or not False =", 10 > 5 and 3 < 1 or not False)


# ============================================================
# HOẠT ĐỘNG 6: BIẾN & DYNAMIC TYPING
# ============================================================
print("\n=== HOẠT ĐỘNG 6 ===")

# Bài tập 6.1: Dynamic typing
bien = 10
print(bien, type(bien))

bien = "Xin chao"
print(bien, type(bien))

bien = 3.14
print(bien, type(bien))

bien = True
print(bien, type(bien))

# Bài tập 6.2: Mini bài toán tổng hợp
ho_ten = "Nguyen Van A"
diem_toan = 8.0
diem_ly = 7.5
diem_hoa = 9.0

dtb = (diem_toan + diem_ly + diem_hoa) / 3

la_gioi = dtb >= 8.0
la_kha = (dtb >= 6.5) and (dtb < 8.0)
la_trung_binh = (dtb >= 5.0) and (dtb < 6.5)
la_yeu = dtb < 5.0

print(ho_ten, "- DTB:", round(dtb, 2))
print("Dat loai Gioi?", la_gioi)
print("Dat loai Kha?", la_kha)
print("Dat loai Trung binh?", la_trung_binh)
print("Dat loai Yeu?", la_yeu)
print("Kieu du lieu cua la_gioi:", type(la_gioi))