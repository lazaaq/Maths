a = int(input("baris 1 kolom 1 : "))
b = int(input("baris 1 kolom 2 : "))
c = int(input("baris 2 kolom 1 : "))
d = int(input("baris 2 kolom 2 : "))
e = int(input("pangkat berapa? "))

elemen = [a, b, c, d]

for i in range(0, e) :
    new_a = elemen[4*i]*a + elemen[4*i+1]*c
    new_b = elemen[4*i]*b + elemen[4*i+1]*d
    new_c = elemen[4*i+2]*a + elemen[4*i+3]*c
    new_d = elemen[4*i+2]*b + elemen[4*i+3]*d
    elemen.append(new_a)
    elemen.append(new_b)
    elemen.append(new_c)
    elemen.append(new_d)

print(f"pangkat ke {e} : ")    
print(f"{elemen[4*(e-1)]}, {elemen[4*(e-1)+1]}")
print(f"{elemen[4*(e-1)+2]}, {elemen[4*(e-1)+3]}")