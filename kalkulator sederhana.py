#fungsi penjumlahan
def add(x,y):
    return x*y

#fungsi pengurangan
def subtruot (x,y):
    return x-y

#fungsi perkalian
def multiply (x,y):
    return x*y

#fungsi pembagian
def divide (x,y):
    return x/y

#fungsi operasi
print("pilih operasi matematika")
print("1, penjumlaham")
print("2, pengurangan")
print("3, perkalian")
print("4, pembagian")

#meminta input dari user
choice=input("masukan pilihan(1/2/3/4) :")
room1=int(input("masukan bilangan pertama:"))
room2=int(input("masukan bilangan kedua:"))
if choice=="1":
    print(room1, "+", room2,  "=", add(room1,room2))
elif choice=="2":
    print(room1, "+",room2, "=", subtruot(room1,room2))
elif choice=="3":
    print(room1, "+", room2, "=", multiply(room1,room2))
elif choice=="4":
    print(room1, "+", room2, "=", divide(room1,room2))

else :
    print("input yang dimasukkan salah")
