"""
Struktur data stack menggunakan prinsip FIFO atau First In Last Out
Dimana data yang pertama masuk akan berada di posisi paling bawah
dan data yang terakhir masuk akan berada di posisi paling atas
"""

# Implementasi stack menggunakan list dengan class
# Class dalam python adalah sebuah blueprint atau cetakan untuk membuat instance dari object
# Class digunakan untuk mendefinisikan atribut dan method yang akan dimiliki oleh object
# Class juga digunakan untuk mengelompokkan data dan fungsi agar lebih mudah diorganisir dan digunakan
# Class Stack digunakan untuk membuat stack dengan menggunakan list

class Stack:
    # Inisialisasi stack
    def __init__(self):
        self._data = []

    # Menambahkan data ke dalam stack menggunakan metode append
    # Data yang dimasukkan akan berada di posisi paling belakang
    def push(self, data):
        self._data.append(data)
        print(f"Data yang di input adalah = {data}")
    
    # Melakukan pengecekan apakah stack kosong atau tidak
    def is_empty(self):
        return len(self._data) == 0
    
    # Shift yaitu menghapus data yang berada di posisi paling depan
    def shift(self):
        if self.is_empty():
            print("Stack kosong")
        else:
            self._data.pop(0)
    
    # Pop yaitu menghapus data yang berada di posisi paling belakang
    # Jika tidak ada index yang diinputkan, maka data yang dihapus adalah data yang berada di posisi paling belakang
    # Jika ada index yang diinputkan, maka data yang dihapus adalah data yang berada di index tersebut
    def pop(self, index = 0):
        if self.is_empty():
            print("Stack kosong")
        else:
            self._data.pop(index)


    # Mengembalikan jumlah data yang ada di dalam stack
    def __len__(self):
        return len(self._data)
    # Mengembalikan data yang ada di dalam stack
    def __str__(self):
        return str(self._data)

# Fungsi utama untuk menjalankan program
def main():
    # Meminta input jumlah data yang akan dimasukkan ke dalam stack
    jumlahData = int(input("Masukkan jumlah data: "))
    # Buat stack baru dengan nama tumpukan
    tumpukan = Stack()

    # Looping untuk memasukkan data ke dalam stack berdasarkan jumlah data yang diinputkan
    for i in range(jumlahData):
        # Meminta input data yang akan dimasukkan ke dalam stack
        data = input(f"Masukkan data ke: ")
        # Memasukkan data ke dalam stack
        tumpukan.push(data)

    # Menampilkan data yang ada di dalam stack
    print("\n")
    print("Data sekarang adalah: ")
    print(f"Data sekarang adalah = {tumpukan}")
    print(f"Jumlah data sekarang adalah = {len(tumpukan)}")
    print("\n")

    # Looping untuk menghapus data dari stack
    while True:
        try:
            # Meminta input index data yang akan dihapus
            print("Menghapus data dari stack")
            index = input("Masukkan index data yang akan dihapus (tulis kata apa saja untuk keluar): ")
            
            # Jika index yang diinputkan adalah huruf, maka program akan keluar
            if index.isalpha():
                break
            
            # Menghapus data dari stack
            index = int(index)
            tumpukan.pop(index)
            
            # Menampilkan data yang ada di dalam stack
            print(f"Data sekarang adalah = {tumpukan}")
            print(f"Jumlah data sekarang adalah = {len(tumpukan)}")
            print("\n")
            
            # Jika stack kosong, maka program akan keluar
            if tumpukan.is_empty():
                print("Stack kosong")
                break
        
        # Jika menangkap Ctrl+C, maka program akan keluar
        except KeyboardInterrupt:
            print("\nInterrupted by Ctrl+C")
            break
    
    # Menampilkan data yang ada di dalam stack
    print("\n")
    print("Data sekarang adalah: ")
    print(f"Data sekarang adalah = {tumpukan}")
    print(f"Jumlah data sekarang adalah = {len(tumpukan)}")
    print("\n")

# Menjalankan program
main()