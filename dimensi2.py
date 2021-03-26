import math
import tkinter

main_window = tkinter.Tk()

class PersegiPanjang:
    
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        luas = self.panjang*self.lebar
        print(f"luas persegi panjang = {luas}")

    def keliling(self):
        keliling = 2*(self.panjang+self.lebar)
        print(f"keliling persegi panjang = {keliling}")
    
class Segitiga:

    def __init__(self, alas, tinggi,sisi1,sisi2,sisi3):
        self.alas = alas
        self.tinggi = tinggi
        self.sisi1 = sisi1
        self.sisi2 = sisi2
        self.sisi3 = sisi3

    def luas(self):
        luas = self.alas*self.tinggi/2
        print(f"luas segitiga = {luas}")

    def keliling(self):
        keliling = self.sisi1+self.sisi2+self.sisi3
        print(f"keliling segitiga = {keliling}")

class Lingkaran:

    def __init__(self, radius):
        self.radius = radius

    def luas(self):
        luas = self.radius*self.radius*math.pi
        print(f"luas lingkaran = {round(luas,2)}")

    def keliling(self):
        keliling = 2*self.radius*math.pi
        print(f"keliling lingkaran = {round(keliling,2)}")


while True:
    print("#Mencari Luas dan Keliling Dimensi 2")
    print("1. Persegi/Persegi Panjang")
    print("2. Segitiga")
    print("3. Lingkaran")
    print("0. keluar")
    input_user = input("pilih : ")
    
    if input_user=="0":
        break
    
    if input_user=="1":
        panjang_persegipanjang = int(input("panjang :"))
        lebar_persegipanjang = int(input("lebar :"))
        objek_1 = PersegiPanjang(panjang_persegipanjang,lebar_persegipanjang)
        objek_1.luas()
        objek_1.keliling()

    if input_user=="2":
        alas_segitiga = int(input("alas :"))
        tinggi_segitiga = int(input("tinggi :"))
        sisi_segitiga = input("ketiga sisi segitiga :")
        sisi = sisi_segitiga.split()
        sisi1 = int(sisi[0])
        sisi2 = int(sisi[1])
        sisi3 = int(sisi[2])
        objek_2 = Segitiga(alas_segitiga, tinggi_segitiga,sisi1,sisi2,sisi3)
        objek_2.luas()
        objek_2.keliling()
        
    if input_user=="3":
        jarijari = int(input("jari jari : "))
        objek_3 = Lingkaran(jarijari)
        objek_3.luas()
        objek_3.keliling()

label1 = tkinter.Label(main_window, text="persegi / persegi panjang")
tombol1 = tkinter.Button(main_window, text="tombol1", )
label2 = tkinter.Label(main_window, text="segitiga")
tombol2 = tkinter.Button(main_window, text="tombol2")
label3 = tkinter.Label(main_window, text="lingkaran")
tombol3 = tkinter.Button(main_window, text="tombol3")

label1.pack()
tombol1.pack()
label2.pack()
tombol2.pack()
label3.pack()
tombol3.pack()

main_window.mainloop()