PIN=input("masukkan pin anda:")

if PIN=="123456":
    saldo = 549000
    print("SELAMAT DATANG DI BANK BRI")
    print("1. TARIK TUNAI")
    print("2. STOR TUNAI")
    print("3. CEK SALDO")
    print("4. KELUAR")
    MENU = input ("pilih menu yang akan dilakukan : ")
    if MENU == '1' :
        print("anda memilih menu tarik tunai")
        JML_PENARIKAN = int (input("masukkan jumlah penarikan : "))
        SISA = saldo - JML_PENARIKAN
        print("jumlah penarikan : ", JML_PENARIKAN)
        print("sisa saldo : ", SISA)
    elif MENU == '2' :
        print ("anda memilih menu stor tunai")
    elif MENU == '3' :
        print ("anda memilih menu cek saldo")
        print ("saldo anda adalah ", saldo)
    elif MENU == '4' :
        print ("keluar")
    else:
        print("jangan iseng2")

else:
    print("PIN ANDA SALAH")
