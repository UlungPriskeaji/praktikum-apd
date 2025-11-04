import data
from prettytable import PrettyTable

def login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username in data.users and data.users[username]["password"] == password:
        print()
        print(f"Login berhasil! Selamat datang BROO {username}")
        if username == "admin":
            menuadmin()
        else:
            menuuser()
    else:
        print("Username atau Password Salah KINGGG! Coba Lagi KINGG!.")

def register():
    username = input("Buat username: ")
    password = input("Buat password: ")
    if username in data.users:
        print("Username sudah ada, coba yang lain!")
    else:
        data.users[username] = {"password": password}
        print("Registrasi berhasil! Silahkan login.")

def menuadmin():
    while True:
        table = PrettyTable()
        table.field_names = ["No", "Statistik Klub Liga Champions UEFA"]
        table.align = "l"  

        table.add_row(["1", "Tampilkan Data Klub"])
        table.add_row(["2", "Tambah Data Klub"])
        table.add_row(["3", "Update Data Klub"])
        table.add_row(["4", "Hapus Data Klub"])
        table.add_row(["0", "Keluar"])
        
        print()
        print(table)

        pilih = input("\n Silahkan Pilih Menu: ")
        if pilih == "1":
            data.tampilkandata()
        elif pilih == "2":
            klub = input("Nama Klub: ")
            try:
                main = int(input("Jumlah Main: "))
                menang = int(input("Jumlah Menang: "))
                seri = int(input("Jumlah Seri: "))
                kalah = int(input("Jumlah Kalah: "))
                gol_dicetak = int(input("Gol Dicetak: "))
                gol_kebobolan = int(input("Gol Kebobolan: "))
                data.tambahdata(klub, main, menang, seri, kalah, gol_dicetak, gol_kebobolan)
            except ValueError:
                print("Input harus berupa angka KINGGGG, input yang benar.")
        elif pilih == "3":
            print("Daftar Klub:")
            klub_list = list(data.klub_ucl.keys())
            for i in range(len(klub_list)):
                print(f"{i+1}. {klub_list[i]}")
            try:
                pilihan = int(input("Pilih nomor klub yang akan diubah: "))
                if 1 <= pilihan <= len(klub_list):
                    klub_lama = klub_list[pilihan - 1]
                    data.updatedata(klub_lama)
                else:
                    print("Nomor tidak valid.")
            except ValueError:
                print("Input harus berupa angka.")
        elif pilih == "4":
            print("Daftar Klub:")
            klub_list = list(data.klub_ucl.keys())
            for i in range(len(klub_list)):
                print(f"{i+1}. {klub_list[i]}")
            try:
                pilihan = int(input("Pilih nomor klub yang ingin dihapus: "))
                if 1 <= pilihan <= len(klub_list):
                    klub_lama = klub_list[pilihan - 1]
                    data.delete(klub_lama)
                else:
                    print("Nomor tidak valid.")
            except ValueError:
                print("Input harus berupa angka.")
        elif pilih == "0":
            print("Kembali ke menu login.")
            break
        else:
            print("Pilihan tidak valid!")

def menuuser():
    while True:
        table = PrettyTable()
        table.field_names = ["No", "Statistik Klub Liga Champions UEFA"]
        table.align = "l"  

        table.add_row(["1", "Tampilkan Data Klub"])
        table.add_row(["0", "Keluar"])

        print()
        print(table)
        
        pilih = input("\n Silahkan Pilih Menu: ")
        if pilih == "1":
            data.tampilkandata()
        elif pilih == "0":
            print("Kembali ke menu login.")
            break
        else:
            print("Pilihan tidak valid!")