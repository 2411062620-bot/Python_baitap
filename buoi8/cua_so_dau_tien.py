import tkinter as tk

cua_so = tk.Tk()
cua_so.title("Vi du Frame")
cua_so.geometry("480x300")
cua_so.resizable(True, False)

khung_tren = tk.Frame(cua_so, bg="lightblue", height=100)
khung_tren.pack(fill="x")

khung_duoi = tk.Frame(cua_so, bg="lightyellow")
khung_duoi.pack(fill="both", expand=True)

nhan_tieu_de = tk.Label(khung_tren, text="Khu vuc tieu de", bg="lightblue")
nhan_tieu_de.pack(pady=10)

nhan_noi_dung = tk.Label(khung_duoi, text="Khu vuc noi dung", bg="lightyellow")
nhan_noi_dung.pack(pady=10)

cua_so.mainloop()