from prettytable import PrettyTable
from auth import login, register

def menuawal():
    while True:
        table = PrettyTable()
        table.field_names = ["No", "Program Liga Champions UEFA"]
        table.align = "l"   
        table.add_row(["1", "Login"])
        table.add_row(["2", "Register"])
        table.add_row(["0", "Keluar"])

        print()
        print(table)

        pilihan = input("\n Silahkan Pilih Menu: ")
        if pilihan == "1":
            login()
        elif pilihan == "2":
            register()
        elif pilihan == "0":
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid, coba lagi!")

if __name__ == "__main__":
    menuawal()