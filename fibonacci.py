suku = [1,1]
hasil = int(input("mau suku ke berapa : "))
for i in range(0, hasil-2) : 
    a = suku[i]+suku[i+1]
    suku.append(a)

print(f"suku ke {hasil} dalam barisan fibonacci adalah : {suku[hasil-1]}")