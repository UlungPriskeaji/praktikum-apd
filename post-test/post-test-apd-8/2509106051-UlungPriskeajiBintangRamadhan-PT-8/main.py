from auth import login, register

def menuawal():
    while True:
        print(
            """
            ========================================
            |     Program Liga Champions UEFA      |
            ========================================
            |    1. Login                          |
            |    2. Register                       |
            |    0. Keluar                         |
            ========================================
            """
        )
        pilihan = input("Silahkan Pilih Menu: ")
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