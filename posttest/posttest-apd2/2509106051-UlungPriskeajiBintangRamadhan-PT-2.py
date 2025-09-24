# Variabel suhu dalam celcius
suhu = [27, 33, 46, 55, 67,92]

# Konversi suhu
# Celcius ke Fahrenheit
f1 = (suhu[0] * 9/5)+32
f2 = (suhu[1] * 9/5)+32

# Celcius ke Kelvin
k1 = suhu[2] + 273.15
k2 = suhu[3] + 273.15

# Celcius ke Reamur
r1 = suhu[4] * 4/5
r2 = suhu[5] * 4/5

# Jumlah
jumlah = f1 + f2 + k1 + k2 + r1 + r2

# Rata-rata
rata2 = jumlah / len(suhu)

# NIM
NIM = 51

# Perbandingan
Bolean = NIM < rata2

# Output
print("Suhu Celcius (dalam list) =", suhu)
print("Suhu 1 dan 2 (Fahrenheit) =", f1, " dan ", f2)
print("Suhu 3 dan 4 (Kelvin) =", k1, " dan ", k2)
print("Suhu 5 dan 6 (Reamur) =", r1, " dan ", r2)
print("Bolean =", Bolean)