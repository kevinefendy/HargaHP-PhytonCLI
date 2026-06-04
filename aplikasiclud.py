hp_prices = [['iphone', 15000000],['Samsung',12000000],['Vivo',10000000],['Realme',5000000],["Oppo",1000000],["Infinix",8000000]]




def display_menu():
    print("\nMenu")
    print("1. Lihat seluruh data")
    print("2. Tambah data")
    print("3. Hapus data")
    print("4. Ubah harga")
    print("5. Hitung rata-rata harga")
    print("6. Keluar")


def lihat_data():
    print ("\nData Harga HP:")

    # Jika data kosong
    if not hp_prices:
        print("Tidak ada data.")
        return
    
    # menampilkan setiap merek dan harga
    for hp, harga in hp_prices:
        print(f"-{hp}: Rp{harga:,}")



def tambah_data():
    nama = input("Masukkan nama HP: ")
    harga = input("Masukkan harga: ")
    harga = int(harga)
    data_baru = [nama, harga]
    hp_prices.append(data_baru)
    print(f"Data '{nama}' berhasil ditambahkan!")

def hapus_data():
    lihat_data()
    nama = input("\nMasukkan nama HP yang ingin dihapus: ")
    for item in hp_prices:
        if item[0].lower() == nama.lower():
            hp_prices.remove(item)
            print(f"Data '{nama}' berhasil dihapus!")
            return
    print(f"Data '{nama}' tidak ditemukan.")

def ubah_harga():
    lihat_data()
    nama = input("\nMasukkan nama HP yang ingin diubah harganya: ")
    for item in hp_prices:
        if item[0].lower() == nama.lower():
            harga_baru = input(f"Masukkan harga baru untuk '{item[0]}': ")
            item[1] = int(harga_baru)
            print(f"Harga '{item[0]}' berhasil diubah menjadi Rp{item[1]:,}")
            return
    print(f"Data '{nama}' tidak ditemukan.")

def rata_rata_harga():
    if not hp_prices:
        print("Tidak ada data untuk dihitung.")
        return
    total = sum(harga for _, harga in hp_prices)
    rata = total / len(hp_prices)
    print(f"\nRata-rata harga HP: Rp{rata:,.0f}")

def main():
    while True:
        display_menu()
        choice = input("Pilih menu (1-6): ") 

        if choice == '1':
            lihat_data()
        elif choice == '2':
            tambah_data()
        elif choice == '3':
            hapus_data()
        elif choice == '4':
            ubah_harga()
        elif choice == '5':
            rata_rata_harga()
        elif choice == '6':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("pilihan tidak valid. silahkan pilih lagi.")
main()