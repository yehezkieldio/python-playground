jawab = True
berulang = 0

while(jawab):
    print("Saya sedang belajar... (perulangan ke", berulang+1, ")")
    berulang += 1
    
    jawab = input("Apakah Anda ingin belajar? (ya/tidak) ")
    
    if jawab == "tidak":
        jawab = False

print("Total perulangan: ", berulang)