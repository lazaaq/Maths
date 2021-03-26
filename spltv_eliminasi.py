p1a = float(input("persamaan 1, koefisien 1 : "))
p1b = float(input("persamaan 1, koefisien 2 : "))
p1c = float(input("persamaan 1, koefisien 3 : "))
hasil1 = float(input("hasil dari persamaan 1 : "))
p2a = float(input("persamaan 2, koefisien 1 : "))
p2b = float(input("persamaan 2, koefisien 2 : "))
p2c = float(input("persamaan 2, koefisien 3 : "))
hasil2 = float(input("hasil dari persamaan 2 : "))
p3a = float(input("persamaan 3, koefisien 1 : "))
p3b = float(input("persamaan 3, koefisien 2 : "))
p3c = float(input("persamaan 3, koefisien 3 : "))
hasil3 = float(input("hasil dari persamaan 3 : "))

perbandingan1 = p1a/p2a
p4_p2b = p2b*perbandingan1
p4_p2c = p2c*perbandingan1
p4_hasil2 = hasil2*perbandingan1
p4_1 = p1b-p4_p2b
p4_2 = p1c-p4_p2c
p4_3 = hasil1-p4_hasil2

perbandingan2 = p2a/p3a
p5_p3b = p3b*perbandingan2
p5_p3c = p3c*perbandingan2
p5_hasil3 = hasil3*perbandingan2
p5_1 = p2b-p5_p3b
p5_2 = p2c-p5_p3c
p5_3 = hasil2-p5_hasil3

perbandingan3 = p4_1/p5_1
new_p51 = p5_2*perbandingan3
new_p52 = p5_3*perbandingan3
p61 = p4_2-new_p51
p62 = p4_3-new_p52
z = p62/p61

y = (p4_3-p4_2*z)/p4_1

x = (hasil1-p1b*y-p1c*z)/p1a

print("nilai x1 adalah : ", x)
print("nilai x2 adalah : ", y)
print("nilai x3 adalah : ", z)
