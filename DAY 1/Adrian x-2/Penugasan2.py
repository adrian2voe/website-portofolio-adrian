print("Segitiga Bintang Siku Siku")
n = int(input("Masukkan jumlah baris: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()
