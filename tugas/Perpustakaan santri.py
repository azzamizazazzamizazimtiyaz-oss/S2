from datetime import date
from typing import List

class User:
    def __init__(self, nama: str):
        self.nama = nama


class Santri(User):
    pass


class Kitab:
    def __init__(self, judul: str, kategori: str, stok: int):
        self.judul = judul
        self.kategori = kategori
        self.__stok = stok

    @property
    def stok(self) -> int:
        return self.__stok

    def kurangi_stok(self) -> bool:
        if self.__stok > 0:
            self.__stok -= 1
            return True
        return False

    def tambah_stok(self) -> None:
        self.__stok += 1



class Peminjaman:
    def __init__(self, santri: Santri, kitab: Kitab):
        self.santri = santri
        self.kitab = kitab
        self.tanggal_pinjam = date.today()



class Perpustakaan:
    def __init__(self):
        self.daftar_kitab: List[Kitab] = []
        self.daftar_peminjaman: List[Peminjaman] = []

    def tambah_kitab(self, kitab: Kitab) -> None:
        self.daftar_kitab.append(kitab)

    def cari_kitab(self, keyword: str) -> List[Kitab]:
        return [
            kitab for kitab in self.daftar_kitab
            if keyword.lower() in kitab.judul.lower()
            or keyword.lower() in kitab.kategori.lower()
        ]

    def pinjam_kitab(self, nama_santri: str, judul_kitab: str) -> None:
        for kitab in self.daftar_kitab:
            if kitab.judul.lower() == judul_kitab.lower():
                if kitab.kurangi_stok():
                    santri = Santri(nama_santri)
                    peminjaman = Peminjaman(santri, kitab)
                    self.daftar_peminjaman.append(peminjaman)
                    print("✅ Peminjaman berhasil dicatat")
                else:
                    print("❌ Stok kitab habis")
                return
        print("❌ Kitab tidak ditemukan")

    def kembalikan_kitab(self, judul_kitab: str) -> None:
        for kitab in self.daftar_kitab:
            if kitab.judul.lower() == judul_kitab.lower():
                kitab.tambah_stok()
                print("✅ Kitab berhasil dikembalikan")
                return
        print("❌ Kitab tidak ditemukan")



def main():
    perpustakaan = Perpustakaan()

    # Data awal
    perpustakaan.tambah_kitab(Kitab("Fathul 'Ali", "Fiqih", 2))
    perpustakaan.tambah_kitab(Kitab("Aqidatuna", "Aqidah", 1))
    perpustakaan.tambah_kitab(Kitab("Nabiyyuna", "Siroh", 3))

    while True:
        print("\n=== PERPUSTAKAAN KITAB ===")
        print("1. Cari Kitab")
        print("2. Pinjam Kitab")
        print("3. Kembalikan Kitab")
        print("4. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            keyword = input("Masukkan judul/kategori: ")
            hasil = perpustakaan.cari_kitab(keyword)
            if hasil:
                for kitab in hasil:
                    print(f"- {kitab.judul} | {kitab.kategori} | Stok: {kitab.stok}")
            else:
                print("❌ Kitab tidak ditemukan")

        elif pilihan == "2":
            nama = input("Nama santri: ")
            judul = input("Judul kitab: ")
            perpustakaan.pinjam_kitab(nama, judul)

        elif pilihan == "3":
            judul = input("Judul kitab: ")
            perpustakaan.kembalikan_kitab(judul)

        elif pilihan == "4":
            print("Terima kasih 🙏")
            break

        else:
            print("❌ Pilihan tidak valid")


if __name__ == "__main__":
    main()
