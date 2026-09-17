import math

print("--- BAI TAP 3.1 & 3.2 ---")
a = -7
b = 2.6789
c = 3 + 4j

print(abs(a))
print(round(b))
print(round(b, 2))
print(pow(2, 3))
print(divmod(10, 3))

print("\n--- BAI TAP 3.3 ---")
a_pt = 1
b_pt = -3
c_pt = 2

delta = b_pt ** 2 - 4 * a_pt * c_pt
x1 = (-b_pt + math.sqrt(delta)) / (2 * a_pt)
x2 = (-b_pt - math.sqrt(delta)) / (2 * a_pt)

print(f"Delta = {delta}")
print(f"Nghiem x1 = {round(x1, 2)}, x2 = {round(x2, 2)}")

print("\n--- BAI TAP 4.1 ---")
cau = "Lap trinh Python rat thu vi"

print(cau[0])
print(cau[-1])
print(cau[4:10])
print(cau[:8])
print(cau[11:])
print(cau[::-1])

chuoi_test = "radar"
is_palindrome = (chuoi_test == chuoi_test[::-1])
print(f"Chuoi '{chuoi_test}' co la Palindrome khong?: {is_palindrome}")

print("\n--- BAI TAP 4.2 ---")
ten = "Nam"
ten_moi = "T" + ten[1:]
print("Ten moi:", ten_moi)

print("\n--- BAI TAP 4.3 ---")
cau_vd = "  Toi dang HOC Python rat vui  "

print(cau_vd.strip())
print(cau_vd.strip().upper())
print(cau_vd.strip().lower())
print(cau_vd.strip().replace("HOC", "hoc"))
print(cau_vd.strip().split())
print(len(cau_vd.strip().split()))
print(cau_vd.count("o"))
print(cau_vd.find("Python"))
print(cau_vd.strip().startswith("Toi"))
print(cau_vd.strip().endswith("vui"))
print("-".join(["Python", "that", "thu", "vui"]))

print("\n--- BAI TAP 4.4 ---")
ho_ten_tho = "   nguyen   van   an   "
ho_ten_sach = " ".join(ho_ten_tho.split()).title()
print("Ho ten sau chuan hoa:", ho_ten_sach)