print("Hello World!")
# cara membuat fungsi pakai `def`
# struktur: `def namaFungsi(parameterNya)`
def hello(name):
    print(f"Halo bli, {name}")
# panggil dibawah, gk boleh nyatu dengan def
hello("Kadek")
hello("Made")
hello("Nyoman")
hello("Komang")

# minta 3 parameter
def nilai(nama, uts, uas):
    rumus = (uts + uas) / 2
    print(f"Nilai Akhir {nama}: {rumus}")

nilai("bayu", 80, 90)
nilai("asep", 70, 80)
nilai("ujang", 75, 85)