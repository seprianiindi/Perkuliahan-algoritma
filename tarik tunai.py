PIN=input("masukkan pin anda")
if PIN =='123456':
    print("selamat datang di atm bri")
    print("1.tarik tunai")
    print("2.stoe tunai")
    print("3.cek saldo")
    print("4.keluar")
    menu=input ("pilih menu yang dilakukan")
    if menu =='1':
        print("tarik tunai")
    elif menu =="2":
        print("stor tunai")
    elif menu =="3":
        print("cek saldo")
    elif menu =="4":
        print("keluar")
        
else:
    print("pin anda salah")
