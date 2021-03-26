p1x = int(input("persamaan 1 koefisien 1\t:"))
p1y = int(input("persamaan 1 koefisien 2\t:"))
p1z = int(input("persamaan 1 koefisien 3\t:"))
h1 = int(input("hasil persamaan 1\t:"))
p2x = int(input("persamaan 2 koefisien 1\t:"))
p2y = int(input("persamaan 2 koefisien 2\t:"))
p2z = int(input("persamaan 2 koefisien 3\t:"))
h2 = int(input("hasil persamaan 2\t:"))
p3x = int(input("persamaan 3 koefisien 1\t:"))
p3y = int(input("persamaan 3 koefisien 2\t:"))
p3z = int(input("persamaan 3 koefisien 3\t:"))
h3 = int(input("hasil persamaan 3\t:"))

determinan = (p1x*p2y*p3z)+(p1y*p2z*p3x)+(p1z*p2x*p3y)-(p1z*p2y*p3x)-(p1x*p2z*p3y)-(p1y*p2x*p3z)

x = (h1*p2y*p3z)+(p1y*p2z*h3)+(p1z*h2*p3y)-(p1z*p2y*h3)-(h1*p2z*p3y)-(p1y*h2*p3z)
y = (p1x*h2*p3z)+(h1*p2z*p3x)+(p1z*p2x*h3)-(p1z*h2*p3x)-(p1x*p2z*h3)-(h1*p2x*p3z)
z = (p1x*p2y*h3)+(p1y*h2*p3x)+(h1*p2x*p3y)-(h1*p2y*p3x)-(p1x*h2*p3y)-(p1y*p2x*h3)

if determinan !=0:
    print(f"nilai x : {x/determinan}")
    print(f"nilai y : {y/determinan}")
    print(f"nilai z : {z/determinan}")
else:
    print("tidak ada penyelesaian")