while True:
    nilai_siswa = int(input("Masukkan nilai siswa: "))

    if nilai_siswa >= 75:
        print("Tuntas")
        break
    else:
        mengulang = input("Apakah ingin mengulang? (Ya/Tidak): ")

        if mengulang.lower() != "ya":
            print("Tidak Tuntas")
            break
