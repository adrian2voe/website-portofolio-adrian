import tkinter as tk
from tkinter import messagebox

def simpan():
    messagebox.showinfo("Info", "Data berhasil disimpan")

def hapus():
    for entry in entries:
        entry.delete(0, tk.END)
    text_alamat.delete("1.0", tk.END)

# Window utama
root = tk.Tk()
root.title("MainWindow")
root.geometry("700x600")
root.configure(bg="#eaeaea")

# ===== Header =====
header = tk.Frame(root, bg="#b2ebf2", height=60)
header.pack(fill="x")

tk.Label(header, text="DATA SISWA BARU",
         font=("Arial", 18, "bold"),
         bg="#b2ebf2").pack(pady=15)

# ===== Form =====
form = tk.Frame(root, bg="#eaeaea")
form.pack(padx=30, pady=10, fill="x")

def field(label_text, default=""):
    tk.Label(form, text=label_text, bg="#eaeaea", anchor="w").pack(fill="x")
    e = tk.Entry(form)
    e.pack(fill="x", pady=5)
    e.insert(0, default)
    entries.append(e)

entries = []

field("Nama Lengkap", "Siswa Baru")
field("Tanggal Lahir", "7 Juli 2007")
field("Asal Sekolah", "SMP")
field("NISN", "12345")
field("Nama Ayah", "Ayah")
field("Nama Ibu", "Ibu")
field("Nomor Telepon / HP", "987654321")

tk.Label(form, text="Alamat", bg="#eaeaea", anchor="w").pack(fill="x")
text_alamat = tk.Text(form, height=4)
text_alamat.pack(fill="x", pady=5)
text_alamat.insert("1.0", "Rumah")

# ===== Tombol =====
btn_frame = tk.Frame(root, bg="#eaeaea")
btn_frame.pack(pady=15, anchor="e", padx=30)

tk.Button(btn_frame, text="Hapus", width=10,
          bg="#e57373", fg="white",
          command=hapus).pack(side="left", padx=5)

tk.Button(btn_frame, text="Simpan", width=10,
          bg="#ff8a65", fg="white",
          command=simpan).pack(side="left", padx=5)

root.mainloop()
