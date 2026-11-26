
# =====================================================
# APLIKASI KASIR RESTORAN SEDERHANA
# UJIAN TENGAH SEMESTER PEMROGRAMAN BERORIENTASI OBJEK
# =====================================================

# -----------------------------------------------------
# SUPERCLASS: MENU
# -----------------------------------------------------
class Menu:
    def __init__(self, kode, nama, harga):
        # Atribut private
        self.__kode = kode
        self.__nama = nama
        self.__harga = harga

    # Getter untuk mengambil data private
    def get_kode(self):
        return self.__kode

    def get_nama(self):
        return self.__nama

    def get_harga(self):
        return self.__harga

    # Method untuk mengubah harga
    def ubah_harga(self, harga_baru):
        if harga_baru > 0:
            self.__harga = harga_baru
            return True
        return False

    # Method untuk menampilkan informasi
    def tampilkan_info(self):
        print(f"Kode  : {self.__kode}")
        print(f"Nama  : {self.__nama}")
        print(f"Harga : Rp{self.__harga:,.0f}")


# -----------------------------------------------------
# SUBCLASS: MAKANAN
# -----------------------------------------------------
class Makanan(Menu):
    def __init__(self, kode, nama, harga, kategori,
                 tingkat_pedas, stok):
        super().__init__(kode, nama, harga)

        self.__kategori = kategori
        self.__tingkat_pedas = tingkat_pedas
        self.__stok = stok

    def get_kategori(self):
        return self.__kategori

    def get_stok(self):
        return self.__stok

    def kurangi_stok(self, jumlah):
        if 0 < jumlah <= self.__stok:
            self.__stok -= jumlah
            return True
        return False

    def tambah_stok(self, jumlah):
        if jumlah > 0:
            self.__stok += jumlah
            return True
        return False

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Jenis : Makanan")
        print(f"Kategori : {self.__kategori}")
        print(f"Tingkat pedas : {self.__tingkat_pedas}")
        print(f"Stok : {self.__stok}")


# -----------------------------------------------------
# SUBCLASS: MINUMAN
# -----------------------------------------------------
class Minuman(Menu):
    def __init__(self, kode, nama, harga, jenis,
                 ukuran, stok):
        super().__init__(kode, nama, harga)

        self.__jenis = jenis
        self.__ukuran = ukuran
        self.__stok = stok

    def get_jenis(self):
        return self.__jenis

    def get_stok(self):
        return self.__stok

    def kurangi_stok(self, jumlah):
        if 0 < jumlah <= self.__stok:
            self.__stok -= jumlah
            return True
        return False

    def tambah_stok(self, jumlah):
        if jumlah > 0:
            self.__stok += jumlah
            return True
        return False

    def tampilkan_info(self):
        super().tampilkan_info()
        print("Jenis : Minuman")
        print(f"Kategori : {self.__jenis}")
        print(f"Ukuran : {self.__ukuran}")
        print(f"Stok : {self.__stok}")


# -----------------------------------------------------
# CLASS RELASI: PESANAN
# Satu pesanan dapat memiliki beberapa Menu
# -----------------------------------------------------
class Pesanan:
    def __init__(self, kode_pesanan, nama_pelanggan):
        self.__kode_pesanan = kode_pesanan
        self.__nama_pelanggan = nama_pelanggan
        self.__daftar_menu = []
        self.__status = "Diproses"

    def get_kode_pesanan(self):
        return self.__kode_pesanan

    def get_status(self):
        return self.__status

    def get_nama_pelanggan(self):
        return self.__nama_pelanggan

    # Menambahkan menu ke pesanan
    def tambah_menu(self, menu, jumlah):
        if jumlah <= 0:
            return False

        if isinstance(menu, (Makanan, Minuman)):
            if not menu.kurangi_stok(jumlah):
                return False

        self.__daftar_menu.append((menu, jumlah))
        return True

    # Menghitung total pembayaran
    def hitung_total(self):
        total = 0
        for menu, jumlah in self.__daftar_menu:
            total += menu.get_harga() * jumlah
        return total

    # Mengubah status pesanan
    def ubah_status(self, status_baru):
        pilihan = ["Diproses", "Selesai", "Dibatalkan"]

        if status_baru in pilihan:
            self.__status = status_baru
            return True
        return False

    # Menampilkan informasi pesanan
    def tampilkan_pesanan(self):
        print("\nKode Pesanan :", self.__kode_pesanan)
        print("Pelanggan    :", self.__nama_pelanggan)
        print("Status       :", self.__status)
        print("\nDaftar Menu:")

        if not self.__daftar_menu:
            print("Belum ada menu.")
        else:
            for menu, jumlah in self.__daftar_menu:
                subtotal = menu.get_harga() * jumlah
                print(
                    f"- {menu.get_nama()} x{jumlah} "
                    f"= Rp{subtotal:,.0f}"
                )

        print(f"Total: Rp{self.hitung_total():,.0f}")


# -----------------------------------------------------
# PROGRAM UTAMA
# -----------------------------------------------------

daftar_menu = []
daftar_pesanan = []


# Fungsi mencari menu berdasarkan kode
def cari_menu(kode):
    for menu in daftar_menu:
        if menu.get_kode() == kode:
            return menu
    return None


# Fungsi menambahkan menu
def tambah_data():
    print("\n=== TAMBAH MENU ===")
    print("1. Makanan")
    print("2. Minuman")

    jenis = input("Pilih jenis menu: ")

    kode = input("Masukkan kode menu: ")

    if cari_menu(kode):
        print("Kode menu sudah digunakan!")
        return

    nama = input("Masukkan nama menu: ")

    try:
        harga = int(input("Masukkan harga: "))
        stok = int(input("Masukkan stok: "))

        if harga <= 0 or stok < 0:
            print("Harga harus positif dan stok tidak boleh negatif.")
            return

        if jenis == "1":
            kategori = input("Kategori makanan: ")
            pedas = input("Tingkat pedas: ")

            menu = Makanan(
                kode, nama, harga, kategori, pedas, stok
            )

        elif jenis == "2":
            kategori = input("Jenis minuman: ")
            ukuran = input("Ukuran minuman: ")

            menu = Minuman(
                kode, nama, harga, kategori, ukuran, stok
            )

        else:
            print("Pilihan tidak valid!")
            return

        daftar_menu.append(menu)
        print("Menu berhasil ditambahkan!")

    except ValueError:
        print("Harga dan stok harus berupa angka!")


# Fungsi menampilkan semua menu
def tampilkan_data():
    print("\n=== DAFTAR MENU RESTORAN ===")

    if not daftar_menu:
        print("Belum ada data menu.")
        return

    for menu in daftar_menu:
        print("-------------------------")
        menu.tampilkan_info()


# Fungsi mencari data
def cari_data():
    print("\n=== CARI MENU ===")
    kode = input("Masukkan kode menu: ")

    menu = cari_menu(kode)

    if menu:
        print("\nData ditemukan:")
        menu.tampilkan_info()
    else:
        print("Menu tidak ditemukan!")


# Fungsi mengubah harga menu
def ubah_data():
    print("\n=== UBAH DATA MENU ===")
    kode = input("Masukkan kode menu: ")

    menu = cari_menu(kode)

    if menu:
        try:
            harga_baru = int(input("Masukkan harga baru: "))

            if menu.ubah_harga(harga_baru):
                print("Harga berhasil diperbarui!")
            else:
                print("Harga harus lebih dari nol!")

        except ValueError:
            print("Harga harus berupa angka!")
    else:
        print("Menu tidak ditemukan!")


# Fungsi membuat pesanan
def buat_pesanan():
    print("\n=== BUAT PESANAN ===")

    if not daftar_menu:
        print("Belum ada menu yang tersedia.")
        return

    kode = "P" + str(len(daftar_pesanan) + 1)

    nama = input("Nama pelanggan: ")

    pesanan = Pesanan(kode, nama)

    while True:
        tampilkan_data()

        kode_menu = input(
            "\nMasukkan kode menu (0 untuk selesai): "
        )

        if kode_menu == "0":
            break

        menu = cari_menu(kode_menu)

        if menu is None:
            print("Menu tidak ditemukan!")
            continue

        try:
            jumlah = int(input("Jumlah pesanan: "))

            if pesanan.tambah_menu(menu, jumlah):
                print("Menu berhasil dimasukkan ke pesanan!")
            else:
                print("Stok tidak cukup atau jumlah tidak valid!")

        except ValueError:
            print("Jumlah harus berupa angka!")

    if pesanan.hitung_total() > 0:
        daftar_pesanan.append(pesanan)
        print("\nPesanan berhasil dibuat!")
        pesanan.tampilkan_pesanan()
    else:
        print("Pesanan kosong, tidak disimpan.")


# Fungsi mengecek status pesanan
def cek_status():
    print("\n=== CEK STATUS PESANAN ===")

    kode = input("Masukkan kode pesanan: ")

    for pesanan in daftar_pesanan:
        if pesanan.get_kode_pesanan() == kode:
            pesanan.tampilkan_pesanan()

            print("\nUbah status?")
            print("1. Diproses")
            print("2. Selesai")
            print("3. Dibatalkan")
            print("0. Kembali")

            pilihan = input("Pilih: ")

            status = {
                "1": "Diproses",
                "2": "Selesai",
                "3": "Dibatalkan"
            }

            if pilihan in status:
                if pesanan.ubah_status(status[pilihan]):
                    print("Status berhasil diperbarui!")
            elif pilihan == "0":
                print("Status tidak diubah.")
            else:
                print("Pilihan tidak valid!")

            return

    print("Pesanan tidak ditemukan!")


# -----------------------------------------------------
# MENU UTAMA PROGRAM
# -----------------------------------------------------

def main():
    while True:
        print("\n================================")
        print("     KASIR RESTORAN SEDERHANA")
        print("================================")
        print("1. Tambah Data Menu")
        print("2. Tampilkan Data Menu")
        print("3. Cari Data Menu")
        print("4. Ubah Data Menu")
        print("5. Buat Pesanan")
        print("6. Cek Status Pesanan")
        print("7. Keluar")
        print("================================")

        pilihan = input("Pilih menu (1-7): ")

        if pilihan == "1":
            tambah_data()
        elif pilihan == "2":
            tampilkan_data()
        elif pilihan == "3":
            cari_data()
        elif pilihan == "4":
            ubah_data()
        elif pilihan == "5":
            buat_pesanan()
        elif pilihan == "6":
            cek_status()
        elif pilihan == "7":
            print("Terima kasih telah menggunakan aplikasi!")
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")


# Menjalankan program
if __name__ == "__main__":
    main()
