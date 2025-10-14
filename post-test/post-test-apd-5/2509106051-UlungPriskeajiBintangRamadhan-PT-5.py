klub_ucl = [
    ["FC Bayern München", 2, 2, 0, 0, 8, 2],
    ["Real Madrid", 2, 2, 0, 0, 7, 1],
    ["Paris Saint-Germain F.C.", 2, 2, 0, 0, 6, 1],
    ["Inter Milan", 2, 2, 0, 0, 5, 0],
    ["Arsenal F.C.", 2, 2, 0, 0, 4, 0]
]

# login
usn = "ggmu"
pw = "treble"

print("\nSelamat Datang di Sistem Data Statistik Klub UCL")
print("\nSilahkan Masukkan Username dan Password Anda")

login_ok = False
while login_ok == False:
    username = input("Username: ")
    password = input("Password: ")
    
    if username == usn and password == pw:
        login_ok = True
        print("Login berhasil!")
    else:
        print("Username atau Password Salah KINGGG! Coba Lagi KINGG!.\n")

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
        for i in range(len(klub_ucl)):
            print(f"{i+1}. {klub_ucl[i][0]} - Main: {klub_ucl[i][1]}, Menang: {klub_ucl[i][2]}, Seri: {klub_ucl[i][3]}, Kalah: {klub_ucl[i][4]}, Gol Dicetak: {klub_ucl[i][5]}, Gol Kebobolan: {klub_ucl[i][6]}")

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
        klub_ucl.append([nama, main, menang, seri, kalah, goldicetak, golkebobolan])
        print("Data klub Berhasil Ditambahkan.")

    elif pilihan == "3":
        print("="*50)
        print("Daftar Klub yang Bisa Diupdate:")
        for i in range(len(klub_ucl)):
            print(f"{i+1}. {klub_ucl[i][0]}")
        print("="*50)
        input_klub = input("Pilih Nomor Klub yang Ingin Diupdate: ")
        print("="*50)
        if input_klub.isdigit():
            index_klub = int(input_klub) - 1  # Karena indeks list mulai dari 0 di Output, dan mempermudah user
            if index_klub >= 0 and index_klub < len(klub_ucl):
                print(f"Update Data untuk {klub_ucl[index_klub][0]}")
                nama = input("Masukkan Nama Klub: ")
                main = int(input("Masukkan Jumlah Main: "))
                menang = int(input("Masukkan Jumlah Menang: "))
                seri = int(input("Masukkan Jumlah Seri: "))
                kalah = int(input("Masukkan Jumlah Kalah: "))
                goldicetak = int(input("Masukkan Jumlah Gol Dicetak: "))
                golkebobolan = int(input("Masukkan Jumlah Gol Kebobolan: "))
                klub_ucl[index_klub] = [nama, main, menang, seri, kalah, goldicetak, golkebobolan]
                print("Data klub Berhasil Diupdate KINGGG!!.") 
            else:
                print("Indeks tidak valid.")
        else:
            print("Indeks Harus Berupa Angka KINGGG!!.")
    
    elif pilihan == "4":
        print("="*50)
        print("Daftar Klub yang Bisa Dihapus:")
        for i in range(len(klub_ucl)):
            print(f"{i+1}. {klub_ucl[i][0]}")
        print("="*50)
        input_klub = input("Pilih Nomor Klub yang Ingin Dihapus: ")
        print("="*50)
        if input_klub.isdigit():
            index_klub = int(input_klub) - 1  # Karena indeks list mulai dari 0 di Output, dan mempermudah user
            if index_klub >= 0 and index_klub < len(klub_ucl):
                del klub_ucl[index_klub]
                print("Data klub Berhasil Dihapus KINGGG!!.")
            else:
                print("Indeks tidak valid.")
        else:
            print("Indeks Harus Berupa Angka KINGGG!!.")

    elif pilihan == "5":
        print("\nTerima kasih telah menggunakan sistem ini. Sampai jumpa lagi KINGGG!!")
        print("\nwhen yah ada KING MU")
        break

    else:
        print("Pilihan tidak valid. Silahkan pilih menu antara 1-5.")
