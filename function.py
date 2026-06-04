# def salam():
#     print('Hello selamat datang di Purwadhika!')
#     print('Semoga hari anda menyenangkan!')

# salam()
# # Hello selamat datang di Purwadhika!
# # Semoga hari anda  menyenangkan!
# salam()
# # Hello selamat datang di Purwadhika!
# # Semoga hari anda  menyenangkan!


# def hai () :
#     print("halo")

# hai()


# def salam (nama):
#     print("Halo", nama)

# salam("TB")


# def data(nama, umur):
#     print("Nama:", nama)
#     print("Umur:", umur)
# data("Nia", 17)


# def tambah(a, b):
#     return a + b

# hasil = tambah(5,3)
# print(hasil)


# def luas_persegi(s):
#     return s * s

# hasil = luas_persegi(4)
# print(hasil + 10)


# def hitung_gaji(gaji_pokok, bonus):
#     return gaji_pokok + bonus

# gaji_nia = hitung_gaji (3000000, 500000)
# pajak = gaji_nia * 0.1

# print("Gaji bersih:", gaji_nia - pajak)


def login(username, password):
    if username == "admin" and password == "123":
        return "Login berhasil"
    else:
        return "Login Gagal"
    
print(login("admin", "123"))
print(login("admin", "456"))

