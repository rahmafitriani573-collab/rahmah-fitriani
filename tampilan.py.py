import data_film

def tampilkan_film():
    print("\n=== DAFTAR FILM ===")
    for f in data_film.film_list:
        print(f"Kode: {f['kode']} | Judul: {f['judul']} | Kursi Tersisa: {f['kursi']}")