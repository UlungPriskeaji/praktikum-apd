# Membuat set
buah = {"apel", "jeruk", "mangga", "apel"}

print(buah)

Daftar_buku = {
"Buku1" : "Bumi Manusia",
"Buku2" : "Laut Bercerita"
}

print(Daftar_buku["Buku1"])

# membuat dictionary

Nilai = {
    "Matematika": 80,
    "B. Indonesia": 90,
    "B. Inggris": 81,
    "Kimia": 78,
    "Fisika": 80
}
# Tanpa menggunakan items()
for i in Nilai:
    print(i)
print("") # pemisah
# Menggunakan items()
for i, j in Nilai.items():
    print(f"Nilai {i} anda adalah {j}")

Film = {
"Avenger Endgame" : "Action",
"Sherlock Holmes" : "Mystery",
"The Conjuring" : "Horror"
}

#Sebelum Ditambah
print(Film)
Film["Zombieland"] = "Comedy"
Film.update({"Hours" : "Thriller"})
#Setelah Ditambah
print(Film)

# #Sebelum Ditambah
# {'Avenger Endgame': 'Action', 'Sherlock Holmes': 'Mystery',
# 'The Conjuring': 'Horror'}
# #Setelah Ditambah
# {'Avenger Endgame': 'Action', 'Sherlock Holmes': 'Mystery',
# 'The Conjuring': 'Horror', 'Zombieland': 'Comedy', 'Hours':
# 'Thriller'}


#ubah
Film["Sherlock Holmes"] = "Action"
Film.update({"The Conjuring" : "Tragedy"})
print(Film)


# set default
Nilai = {
"Matematika" : 80,
"B. Indonesia" : 90,
"B. Inggris" : 81
}
#sebelum Setdefault
print(Nilai)
print("")
#menggunakan setdefault
print("Nilai : ", Nilai.setdefault("Kimia", 70))
print("")
#setelah menggunakan setdefault
print(Nilai)
{'Matematika': 80, 'B. Indonesia': 90, 'B. Inggris':
81}
Nilai : 70
{'Matematika': 80, 'B. Indonesia': 90, 'B. Inggris':
81, 'Kimia': 70}

# Dictionary of List and Nested Dictionary
Musik = {
"The Chainsmoker" : ["All we Know", "The Paris"],
"Alan Walker" : ["Alone", "Lily"],
"Neffex" : ["Best of Me", "Memories"]
}
for key, value in Musik.items():
    for i, j in Musik.items():
        print(f"Musik milik {i} adalah : ")
for song in j:
    print(song)
print("")