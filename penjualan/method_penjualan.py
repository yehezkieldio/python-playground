# menghitung total belanja barang
# jika barang pepsodent maka harganya Rp. 30.000
# jika barang gula pasir maka harganya Rp. 15.000

# total_belanja = harga_barang * jumlah_barang

barang_list = ["pepsodent", "gula pasir"]

def hitung_total_belanja(harga, jumlah_beli):
    return harga * jumlah_beli

def show(nama_barang, harga_barang, jumlah_barang, total_belanja):
    harga_barang = "{:,.2f}".format(harga_barang)
    total_belanja = "{:,.2f}".format(total_belanja)
    
    print(f"Nama Barang: {nama_barang}")
    print(f"Harga (Rp.): {harga_barang}")
    print(f"Jumlah Barang: {jumlah_barang}")
    print(f"Total Belanja (Rp.): {total_belanja}")

def insert_data():
    print()
    print("Daftar Barang")
    print("1. Pepsodent (Rp. 30.000)")
    print("2. Gula Pasir (Rp. 15.000)")
    print()
    nama_barang = input("Input nama barang = ")
    nama_barang = nama_barang.lower()
    
    if nama_barang == "pepsodent":
        harga_barang = float(30000)
        jumlah_beli = int(input("Input jumlah beli = "))
        hasil = hitung_total_belanja(harga_barang, jumlah_beli)
        
        show(nama_barang, harga_barang, jumlah_beli, hasil)
    elif nama_barang == "gula pasir":
        harga_barang = float(15000)
        jumlah_beli = int(input("Input jumlah beli = "))
        hasil = hitung_total_belanja(harga_barang, jumlah_beli)
        
        show(nama_barang, harga_barang, jumlah_beli, hasil)
    else:
        print("Barang tidak tersedia")