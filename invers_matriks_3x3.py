a = int(input("baris ke 1 kolom ke 1 : "))
b = int(input("baris ke 1 kolom ke 2 : "))
c = int(input("baris ke 1 kolom ke 3 : "))
d = int(input("baris ke 2 kolom ke 1 : "))
e = int(input("baris ke 2 kolom ke 2 : "))
f = int(input("baris ke 2 kolom ke 3 : "))
g = int(input("baris ke 3 kolom ke 1 : "))
h = int(input("baris ke 3 kolom ke 2 : "))
i = int(input("baris ke 3 kolom ke 3 : "))

print("matriks : ")
print(a, b, c)
print(d, e, f)
print(g, h, i)

det = a*e*i + b*f*g + c*d*h - c*e*g - a*f*h - b*d*i
print(f"determinannya adalah : {det}")

if det != 0 :
    m11 = (e*i-f*h)/det
    m12 = (f*g-d*i)/det
    m13 = (d*h-e*g)/det
    m21 = (c*h-b*i)/det
    m22 = (a*i-c*g)/det
    m23 = (b*g-a*h)/det
    m31 = (b*f-c*e)/det
    m32 = (c*d-a*f)/det
    m33 = (a*e-b*d)/det
    print("inversnya yaitu :")
    print("(", m11, m21, m31, ")")
    print("(", m12, m22, m32, ")")
    print("(", m13, m23, m33, ")")
else :
    print("tidak ada invers")