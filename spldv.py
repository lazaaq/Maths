p1a = float(input("persamaan 1, koefisien 1 : "))
p1b = float(input("persamaan 1, koefisien 2 : "))
hasil1 = float(input("hasil dari persamaan 1 : "))
p2a = float(input("persamaan 2, koefisien 1 : "))
p2b = float(input("persamaan 2, koefisien 2 : "))
hasil2 = float(input("hasil dari persamaan 2 : "))
perbandingan = p1a/p2a
new_p2a = p2a*perbandingan
new_p2b = p2b*perbandingan
new_hasil2 = hasil2*perbandingan
a = p1b-new_p2b
b = hasil1 - new_hasil2
koefisien2 = b/a
koefisien1 = (hasil1 - p1b*koefisien2)/p1a
print("koefisien 1 bernilai : ", koefisien1)
print("koefisien 2 bernilai : ", koefisien2)
