# Program menentukan bilangan ganjil atau genap

#angka = int(input("Masukkan angka : "))

#if angka % 2 == 0:
#    print(f"Angka {angka} tergolong bilangan GENAP!")
#else:
#    print(f"Angka {angka} tergolong bilangan GANJIL!")

    # Program Menghitung IMT (Indeks Massa Tubuh)

# input massa dan tinggi
massa = float(input("Masukkan Massa (kg) : "))
tinggi_cm = float(input("Masukkan Tinggi (cm) : "))

# ubah cm ke meter
tinggi_m = tinggi_cm / 100

# hitung IMT
imt = massa / (tinggi_m ** 2)

# tampilkan data
print(f"\nMassa {massa} kg dan tinggi {tinggi_m} m")
print(f"IMT = {imt}")

# cek kategori IMT
if imt < 18.5:
    print("BERAT BADAN KURANG!")
elif imt >= 18.5 and imt <= 24.9:
    print("BERAT BADAN IDEAL!")
elif imt >= 25.0 and imt <= 29.9:
    print("BERAT BADAN BERLEBIH!")
elif imt >= 30.0 and imt <= 39.9:
    print("BERAT BADAN SANGAT BERLEBIH!")
else:
    print("OBESITAS!")