# # cara membuat file pada python

# # untuk mencegah error kita biasakan menggunakan try except
# # membuat dan mengisi file

# try :
#     sebuah_file = open("absen.txt", 'w')
#     print ("nama file yang telah di buat".ljust(30),":", sebuah_file.name)
#     print("mode pembacaan".ljust(30),":", sebuah_file.mode)
#     print("apakah file sudah di tutup".ljust(30),":", sebuah_file.closed)

#     sebuah_file.write("1. Muhamad Rafli\n")
#     sebuah_file.write("2. bagus sanjaya\n")
#     sebuah_file.write("3. ahmad solihin\n")
    
# except IOError :
#     print("proses gagal", IOError)

# # membaca file
# try :
#     sebuah_file = open("absen.txt", 'r')
    
#     print ("isi dari file :\n" + sebuah_file.read())
#     print ("posisi pointer pada file".ljust(30),":", sebuah_file.tell())
#     print("posisi pointer berubah ke awal".ljust(30),":", sebuah_file.seek(0,0))

# except IOError :
#     print("gagal membaca file")

# # # membaca file baris per baris
# # try :
# #     sebuah_file = open("absen.txt", 'r')
    
# #     print ("\nmembaca file baris per baris\n")
# #     for line in sebuah_file :
# #         print (line)
# #     sebuah_file.close()
# #     print("apakah file sudah di tutup".ljust(30),":", sebuah_file.closed)

# except IOError :
#     print("gagal membaca file")
# print("\nmengganti nama file\n")
import os
# os.rename('absen.txt', 'daftar_hadir') # untuk merubah nama dari sebuah file
# os.mkdir("direktori baru") # untuk membuat direktori
# print(os.getcwd()) #untuk mengecek direktori saat ini
# os.rmdir("direktori baru")
