import math
# Hoạt động 4: Tuple khai báo, bất biến, unpacking
toa_do = (3, 5)
print(toa_do, type(toa_do))

x, y = toa_do
print("x =", x, ", y =", y)

a, b = 10, 20
a, b = b, a
print("a =", a, ", b =", b)

c, d = 17, 5
thuong, du = divmod(c, d)
print(f"{c} chia {d} duoc thuong {thuong}, du {du}")

# Hoạt động 5: Vận dụng Tuple - Toạ độ điểm & khoảng cách
diem_a = (2, 3)
diem_b = (7, 8)

xa, ya = diem_a
xb, yb = diem_b

khoang_cach = math.sqrt((xb - xa)  ** 2 + (yb - ya) ** 2)
print(f"Khoang_cach giua {diem_a} va {diem_b} la: {round(khoang_cach, 2)}")

danh_sach_cac_diem = [(0, 0), (3, 4), (6, 8)]

for diem in danh_sach_cac_diem:
    x, y = diem
    kc = math.sqrt(x**2 + y**2)
    print(f"Khoang cach tu {diem} den goc toa do (0,0) la: {round(kc, 2)}")