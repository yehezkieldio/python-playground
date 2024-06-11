def cari_vokal_konsonan(nama):
    vokal = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    
    hasil_vokal = []
    hasil_konsonan = []
    
    for huruf in nama:
        if huruf in vokal:
            hasil_vokal.append(huruf)
        elif huruf.isalpha():
            hasil_konsonan.append(huruf)
        else:
            pass
    return hasil_vokal, hasil_konsonan

nama = input("Nama kamu: ")
 
cari = cari_vokal_konsonan(nama)

print(f"Nama kamu: {nama}")
print(f"Vokal: {cari[0]}")
print(f"Konsonan: {cari[1]}")
