import random

soal = random.randint(0, 2000)

tebakan = int(input("Masukkan Tebakan anda"))

while tebakan != soal:
    
    if tebakan > soal:
        print("tebakkan anda terlalu besar")
    else:
        print("tebakan anda terlalu kecil")
    tebakan = int(input("Masukan Tebakan anda"))
        
    
print("Selamat Tebakan anda benar")

