suku1 = int(input("suku ke 1 : "))
suku2 = int(input("suku ke 2 : "))
suku3 = int(input("suku ke 3 : "))
hasil = int(input("mau suku ke berapa : "))
a1 = suku2-suku1
a2 = suku3-suku2
b =a2-a1
#suku ke n (Un)
x = int(suku1+(hasil-1)*(2*a1+(hasil-2*b))/2)
print(f"suku ke {hasil} adalah : {x}")

#jumlah n suku (Sn)
suku = []
suku.append(suku1)
suku.append(suku2)
suku.append(suku3)
for i in range(0, hasil) :
    k = int(suku1+(i+3)*(2*a1+(i+3-2*b))/2)
    suku.append(k)

print(f"jumlah {hasil} suku adalah : {sum(suku)}")

