n = int(input("Masukkan jumlah baris: "))

for i in range(1, n + 1):
    # spasi
    print(" " * (n - i), end="")
    # bintang
    print("* " * i)
