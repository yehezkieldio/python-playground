"""
Masing-masing guru mendapatkan gaji pokok sebesar Rp. 2.000.000 / bulan. 
Untuk uang makan dan transport perhari dibayar Rp. 30.000 dan Rp. 20.000.

Untuk jam wajib mengajar selama 12 jam tidak akan dibayar. 
Jika guru mengajar lebihdari 12 jam maka dibayar sebesar Rp. 20.000 / jam. 
"""

jumlah_guru = 10
gaji_pokok = 2_000_000
uang_makan_perhari = 30_000
uang_transport_perhari = 20_000
jam_wajib_mengajar = 12
tarif_lembur_perjam = 20_000
jumlah_hari_kerja_dalam_sebulan = 30

def hitung_total_gaji(jumlah_jam_mengajar):
    #  Untuk jam wajib mengajar selama 12 jam tidak akan dibayar.
    if jumlah_jam_mengajar <= jam_wajib_mengajar:
        return gaji_pokok
    else:
        # Jika guru mengajar lebih dari 12 jam maka/jam dibayar sebesar Rp. 20.000. 
        jam_lembur = jumlah_jam_mengajar - jam_wajib_mengajar
        gaji_lembur = jam_lembur * tarif_lembur_perjam
        return gaji_pokok + gaji_lembur

for guru in range(1, jumlah_guru + 1):
    jumlah_jam_mengajar = int(input(f"Masukkan jumlah jam mengajar guru ke-{guru}: "))
    
    total_gaji = hitung_total_gaji(jumlah_jam_mengajar)
    total_uang_makan = uang_makan_perhari * jumlah_hari_kerja_dalam_sebulan
    total_uang_transport = uang_transport_perhari * jumlah_hari_kerja_dalam_sebulan
    
    total_gaji_bersih = total_gaji - total_uang_makan - total_uang_transport
    
    print()
    print(f"Informasi Gaji Guru ke-{guru}:")
    print(f"Total Gaji Pokok: Rp. {gaji_pokok}")
    print(f"Total Uang Makan (perbulan): Rp. {total_uang_makan}")
    print(f"Total Uang Transport (perbulan): Rp. {total_uang_transport}")
    print(f"Total Gaji Bersih: Rp. {total_gaji_bersih}")
    print()
