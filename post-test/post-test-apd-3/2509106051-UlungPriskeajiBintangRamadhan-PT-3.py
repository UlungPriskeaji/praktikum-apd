# login
username = input("Masukkan Username :")
password = input("Masukkan Password :")
if username == "ulung" and password == "051":
    print("Login Berhasil")

# konversi
    print("PILIHAN KONVERSI")
    print("1. Konversi Panjang")
    print("2. Konversi Massa")
    print("3. Konversi Suhu")
    print("4. Konversi Waktu")
    print("5. Konversi Mata Uang")
    pil = input("Masukkan Pilihan Anda (1-5): ")

    if pil == "1":
        print("KONVERSI PANJANG")
        print("1. Kaki(feet) ke Meter")
        print("2. Kilometer ke Meter")
        print("3. Centimeter ke Meter")
        pil_panjang = input("Masukkan Pilihan Anda (1-3): ")
        nilai = float(input("Masukkan Nilai yang Ingin Dikonversi: "))
        if pil_panjang == "1":
            print("Hasil adalah: ", nilai * 0.3048, "Meter")
        elif pil_panjang == "2":
            print("Hasil adalah: ", nilai * 1000, "Meter")
        elif pil_panjang == "3":
            print("Hasil adalah: ", nilai * 0.01, "Meter")
        else:
            print("Hasil Tidak Valid")

    elif pil == "2":
        print("KONVERSI MASSA")
        print("1. Pound ke Kilogram")
        print("2. Ton ke Kilogram")
        print("3. Ons ke Kilogram")
        print("4. Gram ke Kilogram")
        print("5. Miliram ke Kilogram")
        pil_massa = input("Masukkan Pilihan Anda (1-3): ")
        nilai = float(input("Masukkan Nilai yang Ingin Dikonversi: "))
        if pil_massa == "1":
            print("Hasil adalah: ", nilai * 0.453592, "Kilogram")
        elif pil_massa == "2":
            print("Hasil adalah: ", nilai * 1000, "Kilogram")
        elif pil_massa == "3":
            print("Hasil adalah: ", nilai * 0.1, "Kilogram")
        elif pil_massa == "4":
            print("Hasil adalah: ", nilai * 0.001, "Kilogram")
        elif pil_massa == "5":
            print("Hasil adalah: ", nilai * 0.000001, "Kilogram")
        else:
            print("Hasil Tidak Valid")

    elif pil == "3":
        print("KONVERSI SUHU")
        print("1. Celcius ke Kelvin")
        print("2. Fahrenheit ke Kelvin")
        print("3. Reamur ke Kelvin")
        pil_suhu = input("Masukkan Pilihan Anda (1-3): ")
        nilai = float(input("Masukkan Nilai yang Ingin Dikonversi: "))
        if pil_suhu == "1":
            print("Hasil adalah: ", nilai + 273.16, "Kelvin")
        elif pil_suhu == "2":
            print("Hasil adalah: ", (nilai - 32) * 5/9 + 273.16 , "Kelvin")
        elif pil_suhu == "3":
            print("Hasil adalah: ", (nilai * 5/4) + 273.16, "Kelvin")
        else:
            print("Hasil Tidak Valid")

    elif pil == "4":
        print("KONVERSI WAKTU")
        print("1. Menit ke Detik")
        print("2. Jam ke Detik")
        pil_waktu = input("Masukkan Pilihan Anda (1-2): ")
        nilai = float(input("Masukkan Nilai yang Ingin Dikonversi: "))
        if pil_waktu == "1":
            print("Hasil adalah: ", nilai * 60, "Detik")
        elif pil_waktu == "2":
            print("Hasil adalah: ", nilai * 3600, "Detik")
        else:
            print("Hasil Tidak Valid")

    elif pil == "5":
        print("KONVERSI MATA UANG")
        print("1. Ringgit ke Rupiah")
        print("2. Rupiah ke Ringgit")
        print("3. Yen ke Rupiah")
        print("4. Rupiah ke Yen")
        print("5. Poundsterling(GBP) ke Rupiah")
        print("6. Rupiah ke Poundsterling(GBP)")
        pil_uang = input("Masukkan Pilihan Anda (1-6): ")  
        nilai = float(input("Masukkan Nilai yang Ingin Dikonversi: "))
        if pil_uang == "1":
            print("Hasil adalah: ", nilai * 3960, "Rupiah")
        elif pil_uang == "2":
            print("Hasil adalah: ", nilai / 3960, "Ringgit")
        elif pil_uang == "3":
            print("Hasil adalah: ", nilai * 112, "Rupiah")
        elif pil_uang == "4":
            print("Hasil adalah: ", nilai / 112, "Yen")
        elif pil_uang == "5":
            print("Hasil adalah: ", nilai * 22427, "Rupiah")
        elif pil_uang == "6":
            print("Hasil adalah: ", nilai / 22427, "Poundsterling(GBP)")
        else:
            print("Hasil Tidak Valid")

    else:
        print("Pilihan Tidak Valid")

else:
    print("Login Gagal")
