# exception, adalah sebuah cara di python untuk menjebak eror, dan menangani eror tak terduga

sebuah_angka = 29
try :
    print(sebuah_angka / 0)
except :
    print("proses perhituangan gagal")

print("proses cetak ini masih dapat di jalankan")

try :
    print(sebuah_angka / 0)
except ZeroDivisionError :
    print("proses perhituangan gagal karena :")

print("proses cetak ini masih dapat di jalankan")

print(sebuah_angka / 0)

# di dalam try terdapa kode yang kemungkinan akan memunculkan excetion. sedangkan di dalam excep adalah kode yang akan di ekseksi jika exception itu muncul

