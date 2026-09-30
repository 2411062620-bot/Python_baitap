# HOẠT ĐỘNG 6: ĐỆ QUY (GIAI THỪA, FIBONACCI)

def giai_thua_de_quy(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua_de_quy(n - 1)

def fibonacci_de_quy(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_de_quy(n - 1) + fibonacci_de_quy(n - 2)

print("=== HOẠT ĐỘNG 6 ===")
print("Giai thua cua 5:", giai_thua_de_quy(5))
print("Fibonacci thu 10:", fibonacci_de_quy(10))

print("\nDang tinh Fibonacci(30)...")
print("Fibonacci thu 30:", fibonacci_de_quy(30))

print("\n[TRA LOI CAU HOI HOAT DONG 6]:")
print("De quy Fibonacci tinh ton kem va cham hon vi co do phuc tap O(2^n).")
print("Cac nhanh de quy tinh lặp lai cung mot gia tri nhieu lan, lam tong so lan goi ham tang theo cap so nhan.")