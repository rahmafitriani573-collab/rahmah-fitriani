import tampilan
import pemesanan

while True:
    print("\n=== SISTEM TIKET BIOSKOP ===")
    print("1. Lihat Daftar Film")
    print("2. Pesan Tiket")
    print("3. Batalkan Tiket")
    print("4. Keluar")
    menu = input("Pilih menu: ")

    if menu == "1":
        tampilan.tampilkan_film()

    elif menu == "2":
        kode = input("Masukkan kode film: ")
        jumlah = int(input("Jumlah tiket: "))
        print(pemesanan.pesan_tiket(kode, jumlah))

    elif menu == "3":
        kode = input("Masukkan kode film: ")
        jumlah = int(input("Jumlah tiket yang dibatalkan: "))
        print(pemesanan.batalkan_tiket(kode, jumlah))

    elif menu == "4":
        print("Keluar...")
        break

    else:
        print("Menu tidak valid.")