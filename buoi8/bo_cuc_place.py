import tkinter as tk

cua_so = tk.Tk()
cua_so.title("Bo cuc bang place()")
cua_so.geometry("300x250")

nhan_ho_ten = tk.Label(cua_so, text="Ho ten:")
nhan_ho_ten.place(x=20, y=20)

nhan_tuoi = tk.Label(cua_so, text="Tuoi:")
nhan_tuoi.place(x=20, y=60)

nhan_email = tk.Label(cua_so, text="Email:")
nhan_email.place(x=20, y=100)

nut_dong_y = tk.Button(cua_so, text="Dong y")
nut_dong_y.place(x=40, y=160)

nut_huy = tk.Button(cua_so, text="Huy")
nut_huy.place(x=150, y=160)

cua_so.mainloop()