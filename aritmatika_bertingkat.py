#program tentang aritmatika bertingkat
#aritmatika bertingkat mirip seperti deret aritmatika, hanya saja beda antar sukunya memiliki tingkatan 
#di program ini tingkatan dari matematika bertingkat hanya ada dua. 
#program ini tidak bisa menghandle untuk yang tingkatan lebih dari sama dengan tiga

#inputan user
suku1 = int(input("suku ke 1 : "))
suku2 = int(input("suku ke 2 : "))
suku3 = int(input("suku ke 3 : "))
hasil = int(input("mau suku ke berapa : "))

#mencari beda suku tingkatan pertama
a1 = suku2-suku1
a2 = suku3-suku2
b = a2-a1

#suku ke n (Un)
x = int(suku1+(hasil-1)*(2*a1+(hasil-2)*b)/2) #rumus
print(f"suku ke {hasil} adalah : {x}")

#jumlah n suku (Sn)
suku = []
suku.append(suku1)
suku.append(suku2)
suku.append(suku3)
for i in range(0, hasil) :
    k = int(suku1+(i+3)*(2*a1+(i+3-2*b))/2) #memasukkan Un, kedalam list suku
    suku.append(k)

print(f"jumlah {hasil} suku adalah : {sum(suku)}")

#catatan : program tidak bisa menghandle big integer, limit nya hanya sampai 9,223,372,036,854,775,807

"""
sample input    : suku ke 1 : 1
                  suku ke 2 : 2
                  suku ke 3 : 4
                  mau suku ke berapa : 5
sample output   : suku ke 5 adalah : 11
                  jumlah 5 suku adalah : 78



sample input    : suku ke 1 : 3
                  suku ke 2 : 4
                  suku ke 3 : 7
                  mau suku ke berapa : 6
sample output   : suku ke 5 adalah : 28
                  jumlah 5 suku adalah : 97
"""
