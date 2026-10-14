import tkinter as tk

cua_so = tk.Tk()
cua_so.title("Bo cuc bang grid()")
cua_so.geometry("300x250")

nhan_ho_ten = tk.Label(cua_so, text="Ho ten:")
nhan_ho_ten.grid(row=0, column=0, padx=10, pady=5, sticky="w")

nhan_tuoi = tk.Label(cua_so, text="Tuoi:")
nhan_tuoi.grid(row=1, column=0, padx=10, pady=5, sticky="w")

nhan_email = tk.Label(cua_so, text="Email:")
nhan_email.grid(row=2, column=0, padx=10, pady=5, sticky="w")

nut_dong_y = tk.Button(cua_so, text="Dong y")
nut_dong_y.grid(row=3, column=0, padx=10, pady=15)

nut_huy = tk.Button(cua_so, text="Huy")
nut_huy.grid(row=3, column=1, padx=10, pady=15)

cua_so.mainloop()