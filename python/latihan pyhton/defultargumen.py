# default argument pada python

# def data_siswa(nama,kota, umur = 19): # default argument berati kita menggunakan argument default seperti yang sudah kita buat, seperti contoh di sampi kita sudah membuat sebuah argument yang di mana umur=18 dan argument tersebut di sebut default argument
#     print("Nama :", nama)
#     print("Umur :", umur)
#     print("Kota :", kota)

#     return

# print(data_siswa(nama = "Muhamad Rafli", kota = "Tangerang Selatan", umur = 18))

# print (data_siswa(nama= "Muhamad Rafli,", kota = "Tangerang Selatan"))

# # variable-leght argument
# # * untuk memasukan sisa data ke dalam bentuk tuple
# # variable-leght argument di gunakan untuk jika kita ingin memasukan data lebih maka data tersebut akan di masukan ke dalam variabel-leght argument
# def data_siswa1(nama, instagram, *scores):
#     print("Nama".ljust(11),":", nama)
#     print ("Instagram".ljust(11),":", instagram)
#     print(scores)
#     i = 0
#     for score in scores:
#         i += 1
#         print("score ke -",i,score)
    
#     return

# print(data_siswa1("muhamad rafli", "@muhamad09rafli", 90, 99, 100, 98))

# # keyword-leght argument
# # ** untuk memasukan sisa data ke dalam bentuk detonant
# # data yang berlebih akan di simpah dalam bentuk detonant
# # kesimpulannya adalah data yang tersisa akan di masukan ke dalam **datalain sebagai bentuk dictonary
# def acak(nama, alamat, **datalain):
#     print ("Nama".ljust(11),":", nama)
#     print ("alamat".ljust(11),":", alamat)
#     print(datalain)
#     for data in datalain:
#         print ("sisa data".ljust(11), ":",datalain[data])
    
#     return

# print(acak("Muhammad Rafli", "Tangerang Selatan", tinggi="173cm",beratbadan= "52"))

# pass by reference dan pass by value
# ini adalah contoh pass by reference dan pass by value
# def fungsi (list):
#     list =[1,2,3,4,5]
#     print(list)

# def fungsi_lagi(list):
#     list.append ([10,20,30,40,50])
#     print(list)

# sebuah_list = [10,20,30,40,50]
# ini_list = [100,200,300,400,500]
# print("apakah list ini berubah?")
# print (sebuah_list)
# fungsi(sebuah_list)
# print (sebuah_list)
# fungsi_lagi(sebuah_list)
# print (sebuah_list)

# print("apakah list ini berubah?")
# print (ini_list)
# fungsi(ini_list)
# print (ini_list)
# fungsi_lagi(ini_list)
# print (ini_list)

# # variable scope pada python
# # jadi denga perintah global pada sebuah fungsi kita dapa mengakses nya di luar sebuah fungsi
# def sebuah_fungsi():
#     angka = 10
#     print("di dalam sebuah_fungsi, angka bernilai", angka)

# def sebuah_fungsi_lainya():
#     global angka # ini memungkinkan kita dapa mengakses sebuah variable secara global
#     angka = 114
#     print("di dalam sebuah_fungsi_lainya, angka bernilai", angka)

# angka = 123

# print("Sebelum di panggil sebuah_fungsi :",angka)
# sebuah_fungsi()
# print("Sesudah di panggil sebuah_fungsi :",angka)

# print ("\n")

# print("Sebelum di panggil sebuah_fungsi_lainya :",angka)
# sebuah_fungsi_lainya()
# print("Sesudah di panggil sebuah_fungsi_lainya :",angka)
    