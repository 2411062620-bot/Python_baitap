# HOẠT ĐỘNG 4: PHẠM VI BIẾN - LOCAL, GLOBAL, TỪ KHÓA GLOBAL

so_luot_truy_cap = 0 

def tang_luot_truy_cap():
    global so_luot_truy_cap
    so_luot_truy_cap += 1

def vi_du_bien_local():
    so_luot_truy_cap = 100  
    print("Ben trong ham, bien local =", so_luot_truy_cap)

print("=== HOẠT ĐỘNG 4 ===")
tang_luot_truy_cap()
tang_luot_truy_cap()
print("So luot truy cap (global):", so_luot_truy_cap)

vi_du_bien_local()
print("Sau khi goi ham, bien global van la:", so_luot_truy_cap)

print("\n[TRA LOI CAU HOI HOAT DONG 4]:")
print("Neu bo dong 'global so_luot_truy_cap', Python se coi 'so_luot_truy_cap' trong ham là bien LOCAL.")
print("Khi thuc hien 'so_luot_truy_cap += 1', Python doc bien local truoc khi khoi tao nen bao loi UnboundLocalError.")


# HOẠT ĐỘNG 5: HÀM LAMBDA KẾT HỢP MAP(), FILTER(), SORTED()

print("\n=== HOẠT ĐỘNG 5 ===")

# Bài tập 5.1: map()
danh_sach_so = [1, 2, 3, 4, 5]
binh_phuong = list(map(lambda x: x ** 2, danh_sach_so))
print("Bai tap 5.1 - binh_phuong:", binh_phuong)

# Bài tập 5.2: filter()
so_chan = list(filter(lambda x: x % 2 == 0, danh_sach_so))
print("Bai tap 5.2 - so_chan:", so_chan)

# Bài tập 5.3: sorted()
danh_sach_sv = [
    {"ten": "An", "diem": 8.5},
    {"ten": "Binh", "diem": 7.0},
    {"ten": "Chi", "diem": 9.2}
]
sv_sap_xep = sorted(danh_sach_sv, key=lambda x: x["diem"], reverse=True)
print("Bai tap 5.3 - Sap xep sinh vien theo diem giam dan:")
for sv in sv_sap_xep:
    print(f"  {sv['ten']}: {sv['diem']}")