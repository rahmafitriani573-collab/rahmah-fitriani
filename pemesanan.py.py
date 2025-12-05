import data_film

def cari_film(kode):
    for f in data_film.film_list:
        if f["kode"] == kode:
            return f
    return None

def pesan_tiket(kode, jumlah):
    film = cari_film(kode)
    if not film:
        return "Film tidak ditemukan."
    if film["kursi"] < jumlah:
        return "Kursi tidak cukup."
    
    film["kursi"] -= jumlah
    return f"{jumlah} tiket berhasil dipesan untuk '{film['judul']}'."

def batalkan_tiket(kode, jumlah):
    film = cari_film(kode)
    if not film:
        return "Film tidak ditemukan."
    
    film["kursi"] += jumlah
    return f"{jumlah} tiket untuk '{film['judul']}' berhasil dibatalkan."