jawab = True
nilai_perhitungan = []

while(jawab):
    print("Input nilai: ")
    nilai = input()
    nilai_perhitungan.append(nilai)
    
    jawab = input("Apakah Anda ingin input nilai lagi? (ya/tidak) ")
    
    if jawab == "tidak":
        jawab = False
        

for i in nilai_perhitungan:
    print(i)
    
print("Total nilai semua di sum adalah: ", sum([int(i) for i in nilai_perhitungan]))