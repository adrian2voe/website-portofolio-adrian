import tkinter as tk
from tkinter import ttk
from datetime import datetime

BIAYA_PER_JAM = 2000

def hitung_biaya():
    try:
        masuk = datetime.strptime(entry_masuk.get(), "%H:%M")
        keluar = datetime.strptime(entry_keluar.get(), "%H:%M")
        durasi = (keluar - masuk).seconds // 3600
        if durasi == 0:
            durasi = 1

        biaya = durasi * BIAYA_PER_JAM
        entry_biaya.delete(0, tk.END)
        entry_biaya.insert(0, biaya)

        # masukkan ke tabel
        tree.insert("", tk.END, values=(
            entry_nopol.get(),
            entry_masuk.get(),
            entry_keluar.get(),
            f"Rp {biaya:,}"
        ))
    except:
        entry_biaya.delete(0, tk.END)
        entry_biaya.insert(0, "0")

# Window
root = tk.Tk()
root.title("Aplikasi Parkir Kelompok 6")
root.geometry("900x500")

# ===== Frame Kiri =====
frame_kiri = tk.Frame(root)
frame_kiri.pack(side=tk.LEFT, padx=20, pady=10)

tk.Label(frame_kiri, text="Aplikasi Parkir Kelompok 6",
         font=("Arial", 14, "bold")).pack(anchor="w")

tk.Label(frame_kiri, text="No Plat Polisi").pack(anchor="w", pady=(10, 0))
entry_nopol = tk.Entry(frame_kiri, width=30)
entry_nopol.pack()

tk.Label(frame_kiri, text="Waktu Masuk (HH:MM)").pack(anchor="w", pady=(10, 0))
entry_masuk = tk.Entry(frame_kiri, width=30)
entry_masuk.pack()

tk.Label(frame_kiri, text="Waktu Keluar (HH:MM)").pack(anchor="w", pady=(10, 0))
entry_keluar = tk.Entry(frame_kiri, width=30)
entry_keluar.pack()

tk.Label(frame_kiri, text="Biaya").pack(anchor="w", pady=(10, 0))
entry_biaya = tk.Entry(frame_kiri, width=30)
entry_biaya.pack()

tk.Button(frame_kiri, text="Button", command=hitung_biaya)\
    .pack(pady=10)

# ===== Frame Kanan =====
frame_kanan = tk.Frame(root)
frame_kanan.pack(side=tk.RIGHT, padx=20)

tk.Label(frame_kanan, text="Biaya Per Jam",
         font=("Arial", 14)).pack()

tk.Label(frame_kanan, text="Rp. 2.000",
         font=("Arial", 26, "bold"),
         fg="red").pack(pady=10)

# ===== Tabel =====
tk.Label(root, text="List Pelanggan Urut Terakhir Keluar",
         fg="blue").place(x=20, y=300)

columns = ("nopol", "masuk", "keluar", "biaya")
tree = ttk.Treeview(root, columns=columns, show="headings", height=6)

tree.heading("nopol", text="No Plat Polisi")
tree.heading("masuk", text="Masuk")
tree.heading("keluar", text="Keluar")
tree.heading("biaya", text="Biaya")

tree.column("nopol", width=120)
tree.column("masuk", width=80)
tree.column("keluar", width=80)
tree.column("biaya", width=100)

tree.place(x=20, y=330)

root.mainloop()
