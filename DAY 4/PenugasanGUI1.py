import tkinter as tk
from tkinter import ttk

def hitung_total():
    try:
        harga = float(entry_harga.get())
        qty = int(entry_qty.get())
        total = harga * qty
        label_total.config(text=f"Total: Rp. {total:,.2f}")
    except ValueError:
        label_total.config(text="Total: Rp. 0.00")

# Window utama
root = tk.Tk()
root.title("Hitung Total")
root.geometry("300x200")

# Label & Entry Harga
label_harga = ttk.Label(root, text="Harga:")
label_harga.pack(pady=(10, 0))

entry_harga = ttk.Entry(root)
entry_harga.pack()

# Label & Entry Kuantitas
label_qty = ttk.Label(root, text="Kuantitas:")
label_qty.pack(pady=(10, 0))

entry_qty = ttk.Entry(root)
entry_qty.pack()

# Tombol Hitung
btn_hitung = ttk.Button(root, text="Hitung Total", command=hitung_total)
btn_hitung.pack(pady=10)

# Label Total
label_total = ttk.Label(root, text="Total: Rp. 0.00")
label_total.pack()

root.mainloop()
