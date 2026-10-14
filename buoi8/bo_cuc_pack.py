import tkinter as tk

cua_so = tk.Tk()
cua_so.title("Bo cuc bang pack()")
cua_so.geometry("300x250")

nhan_ho_ten = tk.Label(cua_so, text="Ho ten:")
nhan_ho_ten.pack(pady=5)

nhan_tuoi = tk.Label(cua_so, text="Tuoi:")
nhan_tuoi.pack(pady=5)

nhan_email = tk.Label(cua_so, text="Email:")
nhan_email.pack(pady=5)

nut_dong_y = tk.Button(cua_so, text="Dong y")
nut_dong_y.pack(side="left", padx=20, pady=15)

nut_huy = tk.Button(cua_so, text="Huy")
nut_huy.pack(side="right", padx=20, pady=15)

cua_so.mainloop()