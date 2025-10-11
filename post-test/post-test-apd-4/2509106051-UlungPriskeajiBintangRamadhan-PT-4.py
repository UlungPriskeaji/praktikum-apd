# login
usnbenar = "ulung"  
pwbenar = "051"   

print("Silahkan Masukkan Username dan Password Anda")

login_berhasil = False
while login_berhasil == False:
    username = input("Username: ")
    password = input("Password: ")
    
    if username == usnbenar and password == pwbenar:
        login_berhasil = True
        print("Login berhasil!")
    else:
        print("Username atau Password salah! Silahkan coba lagi.")

# variabel penyimpan total darah
A_plus = 0
A_minus = 0
B_plus = 0
B_minus = 0
AB_plus = 0
AB_minus = 0
O_plus = 0
O_minus = 0

# loop input data donor
lanjut = "Y"

while lanjut == "Y":
    print()
    print("INPUT DATA DONOR DARAH")
    
    # input golongan darah
    golongan_valid = False
    while golongan_valid == False:
        golongan = input("Masukkan golongan darah (A/B/AB/O): ").upper()
        if golongan == "A" or golongan == "B" or golongan == "AB" or golongan == "O":
            golongan_valid = True
        else:
            print("Golongan darah tidak valid! Harus A, B, AB, atau O.")
    
    # input rhesus
    rhesus_valid = False
    while rhesus_valid == False:
        rhesus = input("Masukkan Rhesus (+/-): ")
        if rhesus == "+" or rhesus == "-":
            rhesus_valid = True
        else:
            print("Rhesus tidak valid! Harus + atau -.")
    
    gol_lengkap = golongan + rhesus
    print("Golongan darah lengkap:", gol_lengkap)
    
    # input jumlah kantong darah
    kantong_valid = False
    while kantong_valid == False:
        kantong = input("Masukkan jumlah kantong darah: ").strip()
        if kantong == "":
            print("Jumlah kantong darah tidak boleh kosong.")
        elif kantong.isdigit() == False:
            print("Input harus angka bulat positif.")
        elif int(kantong) <= 0:
            print("Jumlah kantong darah harus lebih dari 0.")
        else:
            kantong_valid = True
    
    jumlah_kantong = int(kantong)
    jumlah_ml = jumlah_kantong * 500
    print()
    print("Jumlah darah:", jumlah_kantong, "kantong =", jumlah_ml, "ml")
    
    # update total variabel penyimpan darah
    if gol_lengkap == "A+":
        A_plus += jumlah_ml
        print("Golongan Darah: A+")
    elif gol_lengkap == "A-":
        A_minus += jumlah_ml
        print("Golongan Darah: A-")
    elif gol_lengkap == "B+":
        B_plus += jumlah_ml
        print("Golongan Darah: B+")
    elif gol_lengkap == "B-":
        B_minus += jumlah_ml
        print("Golongan Darah: B-")
    elif gol_lengkap == "AB+":
        AB_plus += jumlah_ml
        print("Golongan Darah: AB+")
    elif gol_lengkap == "AB-":
        AB_minus += jumlah_ml
        print("Golongan Darah: AB-")
    elif gol_lengkap == "O+":
        O_plus += jumlah_ml
        print("Golongan Darah: O+")
    elif gol_lengkap == "O-":
        O_minus += jumlah_ml
        print("Golongan Darah: O-")
    
    # lanjut/tidak
    lanjut_valid = False
    while lanjut_valid == False:
        lanjut = input("Apakah anda masih mau input lagi? (Y/T): ").upper()
        if lanjut == "Y" or lanjut == "T":
            lanjut_valid = True
        else:
            print("Masukkan Y atau T saja!")

# ringkasan
print()
print("TOTAL DARAH YANG TERKUMPUL")

print("Golongan A+  :", A_plus, "ml")
print("Golongan A-  :", A_minus, "ml")
print("Golongan B+  :", B_plus, "ml")
print("Golongan B-  :", B_minus, "ml")
print("Golongan AB+ :", AB_plus, "ml")
print("Golongan AB- :", AB_minus, "ml")
print("Golongan O+  :", O_plus, "ml")
print("Golongan O-  :", O_minus, "ml")

total_semua = A_plus + A_minus + B_plus + B_minus + AB_plus + AB_minus + O_plus + O_minus
print("TOTAL KESELURUHAN:", total_semua, "ml")
print()
print("Terima kasih telah menggunakan sistem donor darah!")
