x1 = float(input("garis 1 x1 : "))
y1 = float(input("garis 1 y1 : "))
x2 = float(input("garis 2 x2 : "))
y2 = float(input("garis 2 y2 : "))

m1 = (-1)*y1/x1
m2 = (-1)*y2/x2

m = m1-m2
k = y1-y2
x = (-1)*k/m
y = m1*x+y1


print(f"persamaan 1 ==> y = {m1}x + {y1}")
print(f"persamaan 2 ==> y = {m2}x + {y2}")
print(f"(x,y) = ({x, y})")