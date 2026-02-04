# Program CRUD sederhana - Data Hero MLBB 

data = [
    {"id": 1, "nama": "Minatour", "kelas": "Tank/Fighter"},
    {"id": 2, "nama": "Kadita", "kelas": "Mage"},
    {"id": 3, "nama": "Joy", "kelas": "Assassin"},
    {"id": 4, "nama": "Alpha", "kelas": "Fighter"},
    {"id": 5, "nama": "Obsidia", "kelas": "Marksman"}
]

def tambah_data():
    print("\n=== Tambah Hero ===")
    id_data = int(input("Masukkan ID: "))
    nama = input("Nama Hero: ")
    kelas = input("Role Hero: ")

    data.append({
        "id": id_data,
        "nama": nama,
        "kelas": kelas
    })
    print("Hero berhasil ditambahkan!")

def tampil_data():
    print("\n=== Daftar Hero MLBB ===")
    if len(data) == 0:
        print("Data kosong")
    else:
        for d in data:
            print(f"ID: {d['id']} | Hero: {d['nama']} | Role: {d['kelas']}")

def ubah_data():
    print("\n=== Ubah Data Hero ===")
    id_cari = int(input("Masukkan ID Hero: "))

    for d in data:
        if d["id"] == id_cari:
            d["nama"] = input("Nama baru: ")
            d["kelas"] = input("Role baru: ")
            print("Data hero berhasil diubah!")
            return

    print("Hero tidak ditemukan")

def hapus_data():
    print("\n=== Hapus Hero ===")
    id_cari = int(input("Masukkan ID Hero: "))

    for d in data:
        if d["id"] == id_cari:
            data.remove(d)
            print("Hero berhasil dihapus!")
            return

    print("Hero tidak ditemukan")

while True:
    print("\n=== MENU HERO MLBB ===")
    print("1. Tambah hero")
    print("2. Tampilkan hero")
    print("3. Ubah hero")
    print("4. Hapus hero")
    print("0. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_data()
    elif pilihan == "2":
        tampil_data()
    elif pilihan == "3":
        ubah_data()
    elif pilihan == "4":
        hapus_data()
    elif pilihan == "0":
        print("Keluar program")
        break
    else:
        print("Pilihan tidak valid")