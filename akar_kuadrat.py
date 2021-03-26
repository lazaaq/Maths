import math
angka = int(input())
bulat = int(math.sqrt(angka))
list_satu = []
for i in range(1,bulat+1):
    kuadrat = i*i
    var = int(angka/kuadrat)
    var1 = angka/kuadrat
    var2 = var - var1
    if var2 == 0.0:
        list_satu.append(var)
dalam_akar = list_satu[len(list_satu)-1]
luar_akar = int(math.sqrt(angka/list_satu[len(list_satu)-1]))
print(luar_akar, "akar", dalam_akar) 
