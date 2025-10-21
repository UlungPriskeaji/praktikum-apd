# dictionary berisi data klub sepak bola di Liga Champions UEFA
klub_ucl = {
    "FC Bayern München": {"main": 2, "menang": 2, "seri": 0, "kalah": 0, "gol_dicetak": 8, "gol_kebobolan": 2},
    "Real Madrid": {"main": 2, "menang": 2, "seri": 0, "kalah": 0, "gol_dicetak": 7, "gol_kebobolan": 1},
    "Paris Saint-Germain F.C.": {"main": 2, "menang": 2, "seri": 0, "kalah": 0, "gol_dicetak": 6, "gol_kebobolan": 1},
    "Inter Milan": {"main": 2, "menang": 2, "seri": 0, "kalah": 0, "gol_dicetak": 5, "gol_kebobolan": 0},
    "Arsenal F.C.": {"main": 2, "menang": 2, "seri": 0, "kalah": 0, "gol_dicetak": 4, "gol_kebobolan": 0}
}

# dictionary untuk menyimpan username dan password
data_user = {
    "ggmu": "treble"
}

print("\nSelamat Datang di Sistem Data Statistik Klub UCL")
print("="*50)

# login bisa memakai usn: ggmu dan pw: treble, atau register yahhhhhhh
login_ok = False
while login_ok == False:
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilih_opsi = input("Pilih menu (1-3): ")

    if pilih_opsi == "1":
        username = input("Masukkan Username: ")
        password = input("Masukkan Password: ")
        
        if username in data_user and data_user[username] == password:
            login_ok = True
            print("Login berhasil!")
        else:
            print("Username atau Password Salah KINGGG! Coba Lagi KINGG!.\n")

    elif pilih_opsi == "2":
        usn_baru = input("Masukkan Username Baru: ")
        pass_baru = input("Masukkan Password Baru: ")
        data_user[usn_baru] = pass_baru
        print("Registrasi berhasil! Silahkan login.\n")

    elif pilih_opsi == "3":
        print("Terima kasih telah menggunakan sistem ini. Sampai jumpa!")
        exit()

    else:
        print("Opsi tidak valid. Silahkan coba lagi.\n")

while True:
    print("")
    print("="*50)
    print("Menu Statistik Klub UCL")
    print("="*50)
    print("1. Lihat Statistik Tim Klub")
    print("2. Tambah Data Klub")
    print("3. Update Data Klub")
    print("4. Hapus Data Klub")
    print("5. Keluar")

    pilihan = input("Silahkan Pilih Menu (1-5): ")

    if pilihan == "1":
        print("="*50)
        print("Statistik Tim Klub")
        print("="*50)
        list_klub = list(klub_ucl.keys())
        indeks = 1
        for klub in list_klub:
            stats = klub_ucl[klub]
            print(f"\n{indeks}. Klub: {klub}\nMain: {stats['main']},\nMenang: {stats['menang']},\nSeri: {stats['seri']},\nKalah: {stats['kalah']},\nGol Dicetak: {stats['gol_dicetak']},\nGol Kebobolan: {stats['gol_kebobolan']}")
            indeks += 1
            print("-"*50)

    elif pilihan == "2":
        print("="*50)
        print("Silahkan Tambah Data Klub")
        print("="*50)
        nama = input("Masukkan Nama Klub: ")
        main = int(input("Masukkan Jumlah Main: "))
        menang = int(input("Masukkan Jumlah Menang: "))
        seri = int(input("Masukkan Jumlah Seri: "))
        kalah = int(input("Masukkan Jumlah Kalah: "))
        goldicetak = int(input("Masukkan Jumlah Gol Dicetak: "))
        golkebobolan = int(input("Masukkan Jumlah Gol Kebobolan: "))
        klub_ucl[nama] = {
            "main": main,
            "menang": menang,
            "seri": seri,
            "kalah": kalah,
            "gol_dicetak": goldicetak,
            "gol_kebobolan": golkebobolan
        }
        print("Data klub Berhasil Ditambahkan.")

    elif pilihan == "3":
        print("="*50)
        print("Daftar Klub yang Bisa Diupdate:")
        list_klub = list(klub_ucl.keys())
        indeks = 1
        for klub in list_klub:
            print(f"{indeks}. {klub}")
            indeks += 1
        print("="*50)
        input_klub = input("Pilih Nomor Klub yang Ingin Diupdate: ")
        if input_klub.isdigit():
            index_klub = int(input_klub) - 1  # Karena indeks list mulai dari 0 di Output, dan mempermudah user
            if index_klub >= 0 and index_klub < len(list_klub):
                klub_terpilih = list_klub[index_klub]
                print(f"Update Data untuk {klub_terpilih}")
                main = int(input("Masukkan Jumlah Main: "))
                menang = int(input("Masukkan Jumlah Menang: "))
                seri = int(input("Masukkan Jumlah Seri: "))
                kalah = int(input("Masukkan Jumlah Kalah: "))
                goldicetak = int(input("Masukkan Jumlah Gol Dicetak: "))
                golkebobolan = int(input("Masukkan Jumlah Gol Kebobolan: "))
                klub_ucl[klub_terpilih] = {
                    "main": main,
                    "menang": menang,
                    "seri": seri,
                    "kalah": kalah,
                    "gol_dicetak": goldicetak,
                    "gol_kebobolan": golkebobolan
                }
                print("Data klub Berhasil Diupdate KINGGG!!.")
            else:
                print("Indeks tidak valid.")
        else:
            print("Indeks Harus Berupa Angka KINGGG!!.")

    elif pilihan == "4":
        print("="*50)
        print("Daftar Klub yang Bisa Dihapus:")
        list_klub = list(klub_ucl.keys())
        indeks = 1
        for klub in list_klub:
            print(f"{indeks}. {klub}")
            indeks += 1
        print("="*50)
        input_klub = input("Pilih Nomor Klub yang Ingin Dihapus: ")
        if input_klub.isdigit():
            index_klub = int(input_klub) - 1  # Karena indeks list mulai dari 0 di Output, dan mempermudah user
            if index_klub >= 0 and index_klub < len(list_klub):
                klub_terpilih = list_klub[index_klub]
                del klub_ucl[klub_terpilih]
                print("Data klub Berhasil Dihapus KINGGG!!.")
            else:
                print("Indeks tidak valid.")
        else:
            print("Indeks Harus Berupa Angka KINGGG!!.")

    elif pilihan == "5":
        print("Terima kasih telah menggunakan sistem ini. Sampai jumpa!")
        print("\nKING MU < LIVERPOOL 🤪 (19/10/2025)")
        print("kapan lagi mu menang di anfield aowmkoakowka")
        break


