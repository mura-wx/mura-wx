# mengenak buitl in fungsion pada Class dan Object

#  __doc__, di gunakan untuk mengakses dokumetasi yang terdapat pada kelas
# __name__, di gunakan untuk mengakses nama kelas
# __dict__, di gunakaan untuk mendapatkan namespace dari kelas tersebut
# __module__, digunakan untuk mendapatkan informasi dimana lokasi modul yang mendefinisikan kelas tersebut
# __bases__, digunakan untuk melihat darimana kelas tersebit diwasriskan.

class persegipanjang:
    def __init__(self,panjang,lebar):
        self.panjang = panjang
        self.lebar = lebar
    
    def hitung_luas(self):
        return self.panjang * self.lebar

    def hitung_keliling(self):
        return (2*self.panjang)+(2*self.lebar)
    
PersegipanjangA=persegipanjang(20,10)

print ( "Persegi panjanga A") 
print ("Panjang".ljust(13),":", PersegipanjangA.panjang)
print ("Lebar".ljust(13),":", PersegipanjangA.lebar) 
print ("Luas".ljust(13),":", PersegipanjangA.hitung_luas())
print ("Keliling".ljust(13),":", PersegipanjangA.hitung_keliling())

print("modulnya =",PersegipanjangA.__module__)
print("doc nya =",PersegipanjangA.__doc__)
print("dict nya =",PersegipanjangA.__dict__)
