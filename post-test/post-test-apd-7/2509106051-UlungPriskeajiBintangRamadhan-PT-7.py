# Data pengguna (username dan password)
users = {
    "admin": {"password": "admin123"},
    "user": {"password": "ggmu"},
}

# Data statistik klub UCL
klub_ucl = {
    "Paris Saint-Germain F.C.": {"main": 3, "menang": 3, "seri": 0, "kalah": 0, "gol_dicetak": 13, "gol_kebobolan": 3},
    "FC Bayern München": {"main": 3, "menang": 3, "seri": 0, "kalah": 0, "gol_dicetak": 12, "gol_kebobolan": 2},
    "Inter Milan": {"main": 3, "menang": 3, "seri": 0, "kalah": 0, "gol_dicetak": 9, "gol_kebobolan": 0},
    "Arsenal F.C.": {"main": 3, "menang": 3, "seri": 0, "kalah": 0, "gol_dicetak": 8, "gol_kebobolan": 0},
    "Real Madrid": {"main": 3, "menang": 3, "seri": 0, "kalah": 0, "gol_dicetak": 8, "gol_kebobolan": 1}
}

# Fungsi untuk registrasi pengguna baru
def register():
    global users
    username = input("Buat username: ")
    password = input("Buat password: ")
    if username in users:
        print("Username sudah ada, coba yang lain!")
    else:
        users[username] = {"password": password}
        print("Registrasi berhasil! Silahkan login.")

# Fungsi untuk login user dan admin
def login():
    global users
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username in users and users[username]["password"] == password:
        print()
        print(f"Login berhasil! Selamat datang BROO {username}")
        if username == "admin":
            menuadmin()
        else:
            menuuser()
    else:
        print("Username atau Password Salah KINGGG! Coba Lagi KINGG!.")

# Fungsi menu awal 
def menuawal():
    while True:
        print("\nPilih opsi:")
        print("1. Register")
        print("2. Login")
        print("0. Keluar")
        pilihan = input("Masukkan pilihan: ")

        if pilihan == "1":
            register()
        elif pilihan == "2":
            login()
        elif pilihan == "0":
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid, coba lagi!")

# Fungsi menu admin 
def menuadmin():
    while True:
        print(
            """
            ========================================
            |  Statistik Klub Liga Champions UEFA  |
            ========================================
            |    1. Tampilkan Data Klub            |
            |    2. Tambah Data Klub               |
            |    3. Update Data Klub               |
            |    4. Hapus Data Klub                |
            |    0. Keluar                         |
            ========================================
            """
        )
        pilih = input("Silahkan Pilih Menu: ")
        if pilih == "1":
            tampilkandata()
        elif pilih == "2":
            klub = input("Nama Klub: ")
            try:
                main = int(input("Jumlah Main: "))
                menang = int(input("Jumlah Menang: "))
                seri = int(input("Jumlah Seri: "))
                kalah = int(input("Jumlah Kalah: "))
                gol_dicetak = int(input("Gol Dicetak: "))
                gol_kebobolan = int(input("Gol Kebobolan: "))
                tambahdata(klub, main, menang, seri, kalah, gol_dicetak, gol_kebobolan)
            except ValueError:
                print("Input harus berupa angka KINGGGG, input yang benar.")
        elif pilih == "3":
            print("Daftar Klub:")
            klub_list = list(klub_ucl.keys())
            for i in range(len(klub_list)):
                print(f"{i+1}. {klub_list[i]}")
            try:
                pilihan = int(input("Pilih nomor klub yang akan diubah: "))
                if 1 <= pilihan <= len(klub_list):
                    klub_lama = klub_list[pilihan - 1]
                    updatedata(klub_lama)
                else:
                    print("Nomor tidak valid.")
            except ValueError:
                print("Input harus berupa angka.")
        elif pilih == "4":
            print("Daftar Klub:")
            klub_list = list(klub_ucl.keys())
            for i in range(len(klub_list)):
                print(f"{i+1}. {klub_list[i]}")
            try:
                pilihan = int(input("Pilih nomor klub yang ingin dihapus: "))
                if 1 <= pilihan <= len(klub_list):
                    klub_lama = klub_list[pilihan - 1]
                    delete(klub_lama)
                else:
                    print("Nomor tidak valid.")
            except ValueError:
                print("Input harus berupa angka.")
        elif pilih == "0":
            print("Kembali ke menu login.")
            break
        else:
            print("Pilihan tidak valid!")

# Fungsi menu user
def menuuser():
    while True:
        print(
            """
            ========================================
            |  Statistik Klub Liga Champions UEFA  |
            ========================================
            |    1. Tampilkan Data Klub            |
            |    0. Keluar                         |
            ========================================
            """
        )
        pilih = input("Silahkan Pilih Menu: ")
        if pilih == "1":
            tampilkandata()
        elif pilih == "0":
            print("Kembali ke menu login.")
            break
        else:
            print("Pilihan tidak valid!")

# Fungsi tambah data klub
def tambahdata(klub, main, menang, seri, kalah, gol_dicetak, gol_kebobolan):
    klub_ucl[klub] = {
        "main": main,
        "menang": menang,
        "seri": seri,
        "kalah": kalah,
        "gol_dicetak": gol_dicetak,
        "gol_kebobolan": gol_kebobolan
    }
    print(f"Data klub {klub} berhasil ditambahkan.")

# Fungsi menampilkan data klub
def tampilkandata():
    for klub, stats in klub_ucl.items():
        print(f"\nKlub: {klub}")
        print(f"Main: {stats['main']}")
        print(f"Menang: {stats['menang']}")
        print(f"Seri: {stats['seri']}")
        print(f"Kalah: {stats['kalah']}")
        print(f"Gol Dicetak: {stats['gol_dicetak']}")
        print(f"Gol Kebobolan: {stats['gol_kebobolan']}")

# Fungsi update data klub
def updatedata(klub_lama):
    if klub_lama in klub_ucl:
        try:
            main = int(input("Jumlah Main baru: "))
            menang = int(input("Jumlah Menang baru: "))
            seri = int(input("Jumlah Seri baru: "))
            kalah = int(input("Jumlah Kalah baru: "))
            gol_dicetak = int(input("Gol Dicetak baru: "))
            gol_kebobolan = int(input("Gol Kebobolan baru: "))
        except ValueError:
            print("Input harus berupa angka, gagal mengubah data.")
            return

        klub_ucl[klub_lama] = {
            "main": main,
            "menang": menang,
            "seri": seri,
            "kalah": kalah,
            "gol_dicetak": gol_dicetak,
            "gol_kebobolan": gol_kebobolan
        }
        print(f"Data klub {klub_lama} berhasil diubah.")
    else:
        print("Klub tidak ditemukan.")

# Fungsi delete data klub
def delete(klub_lama):
    if klub_lama in klub_ucl:
        del klub_ucl[klub_lama]
        print(f"Klub {klub_lama} berhasil dihapus.")
    else:
        print("Klub tidak ditemukan.")

menuawal()
