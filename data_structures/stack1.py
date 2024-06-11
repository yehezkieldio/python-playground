"""
Struktur data stack menggunakan prinsip FIFO atau First In Last Out
Dimana data yang pertama masuk akan berada di posisi paling bawah
dan data yang terakhir masuk akan berada di posisi paling atas
"""

"Deklarasi stack"
"[]"

tumpukan = []


"Push"
"Menambahkan data ke dalam stack"
"[Dio]"

tumpukan.append("Dio")

print(f"Data nama sekarang adalah = {tumpukan}")
print(f"Jumlah nama sekarang adalah = {len(tumpukan)}")

"------------------------------------------"

"Push"
"Menambahkan data ke dalam stack"
"[Dio, Tristan]"

tumpukan.append("Tristan")

print(f"Data nama sekarang adalah = {tumpukan}")
print(f"Jumlah nama sekarang adalah = {len(tumpukan)}")

"------------------------------------------"

"Pop"
"Menghapus data dari dalam stack"
"[Dio]"

tumpukan.pop()

print(f"Data nama sekarang adalah = {tumpukan}")
print(f"Jumlah nama sekarang adalah = {len(tumpukan)}")