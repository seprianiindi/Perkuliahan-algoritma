nim = ["03","04","05","06","07","08","09","10","11","12","13"]
nama = ["indri","Anggun","kartika","eka","silpe","istianah","lydia","jumahir","yudistira","multazam","doni"]
usia = [17,20,25,29,33,14,16,40,35,33,27]
status_perkawinan =[True,False,False,True,False,True,True,False,True,False,False]
tinggi = [160.6,150.9,165.3,170.3,144.5,149.3,140.0,160.5,170,175,180]
print(nama)

len(nama)

for i in range(0,len(nama)):
    print(i, end="\t")
    print(nim[i], end="\t")
    print(nama[i] ,end="\t")
    print(status_perkawinan[i], end="\t")
    print(tinggi[i])


