# Input umur
umur = int(input("Masukkan umur: "))

# Proses klasifikasi
if umur <= 10:
    kategori = "Anak-anak"
elif umur <= 18:
    kategori = "Remaja"
elif umur <= 35:
    kategori = "Dewasa"
elif umur <= 65:
    kategori = "Parubaya"
else:
    kategori = "Tua"

# Output hasil
print("Kategori umur:", kategori)
