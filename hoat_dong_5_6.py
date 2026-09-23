# HOẠT ĐỘNG 5: PASS, BREAK, CONTINUE
# 5.1 - pass (câu lệnh giữ chỗ)
diem = 6.5

if diem >= 8.0:
    pass 
elif diem >= 5.0:
    print("Đạt yêu cầu")
else:
    pass

# 5.2 - break: Kiểm tra số nguyên tố
so = 29
la_so_nguyen_to = True

if so < 2:
    la_so_nguyen_to = False
else:
    for i in range(2, so):
        if so % i == 0:
            la_so_nguyen_to = False
            break  

print(f"{so} có phải số nguyên tố không? {la_so_nguyen_to}")

# 5.3 - break: Tìm số nguyên tố đầu tiên lớn hơn n
n = 20
so_hien_tai = n + 1

while True:
    la_so_nguyen_to = True
    for i in range(2, so_hien_tai):
        if so_hien_tai % i == 0:
            la_so_nguyen_to = False
            break

    if la_so_nguyen_to:
        break

    so_hien_tai += 1

print(f"Số nguyên tố đầu tiên lớn hơn {n} là: {so_hien_tai}")

# 5.4 - continue: Lọc phần tử hợp lệ trong danh sách
danh_sach = [5, -3, 8, 0, -1, 12, 7, -9]
danh_sach_hop_le = []

for so in danh_sach:
    if so <= 0:
        continue 
    danh_sach_hop_le.append(so)

print("Các số hợp lệ (dương):", danh_sach_hop_le)

# HOẠT ĐỘNG 6: VÒNG LẬP LỒNG NHAU - IN HÌNH BẰNG KÝ TỰ
# 6.1 - Tam giác sao
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

# 6.2 - Hình thoi sao
n = 4

# Nửa trên của hình thoi
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# Nửa dưới của hình thoi
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))