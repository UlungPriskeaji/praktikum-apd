from prettytable import PrettyTable

users = {
    "admin": {"password": "admin123"},
    "user": {"password": "ggmu"},
}

klub_ucl = {
    "Paris Saint-Germain F.C.": {"main": 3, "menang": 3, "seri": 0, "kalah": 0, "gol_dicetak": 13, "gol_kebobolan": 3},
    "FC Bayern München": {"main": 3, "menang": 3, "seri": 0, "kalah": 0, "gol_dicetak": 12, "gol_kebobolan": 2},
    "Inter Milan": {"main": 3, "menang": 3, "seri": 0, "kalah": 0, "gol_dicetak": 9, "gol_kebobolan": 0},
    "Arsenal F.C.": {"main": 3, "menang": 3, "seri": 0, "kalah": 0, "gol_dicetak": 8, "gol_kebobolan": 0},
    "Real Madrid": {"main": 3, "menang": 3, "seri": 0, "kalah": 0, "gol_dicetak": 8, "gol_kebobolan": 1}
}

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

def tampilkandata():
    table = PrettyTable()
    table.field_names = ["Klub", "Main", "Menang", "Seri", "Kalah", "Gol Dicetak", "Kebobolan"]
    
    for klub, stats in klub_ucl.items():
        table.add_row([
            klub,
            stats['main'],
            stats['menang'],
            stats['seri'],
            stats['kalah'],
            stats['gol_dicetak'],
            stats['gol_kebobolan']
        ])
    
    print(table)

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

def delete(klub_lama):
    if klub_lama in klub_ucl:
        del klub_ucl[klub_lama]
        print(f"Klub {klub_lama} berhasil dihapus.")
    else:
        print("Klub tidak ditemukan.")