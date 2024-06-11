# def bold(text):
#     return f"\033[1m{text}\033[0m"

# def cetak(length):
#     print("-" * length)

# def tampil(nama, jurusan):
#     data = f"Nama: {bold(nama):<15} | {"":<15} Jurusan: {bold(jurusan)}"
#     cetak(len(data))
#     print(data)
#     cetak(len(data))

# nama = input("Masukkan nama: ")
# jurusan = input("Masukkan jurusan: ")
# tampil(nama, jurusan)

def tambah(a, b):
        return int(a) + int(b)

def hitung_nilai():
    a = input("Masukkan angka pertama: ")
    b = input("Masukkan angka kedua: ")

    hasil = tambah(a, b)

    print(f"Hasil penjumlahan {a} + {b} = {hasil}")
    
def input_data():
    nama = input("Masukkan nama: ")
    jurusan = input("Masukkan jurusan: ")
    return nama, jurusan
    
hitung_nilai()