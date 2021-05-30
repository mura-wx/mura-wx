# dictonary, adalah sebuah wadah untuk menyimpan sebuah value, dan value yang di simpan harus memiliki key

dicto = {1: "makan", 2:"lagi", 'c':"iya"}
print(dicto)
print("value pada dictonary dengan key 1 =",dicto[1])
print("value pada dictonary dengan key 'c' =",dicto['c'])
# jika kita mecoba mengakses data pada dictonary dengan keys yang tidak tepat makan akan muncul pesan keyerror

# untuk mengetauhui keys yang ada pada dictonary gunakan method keys()
print(dicto.keys())

# upadating dictonary elemen, kalian dapat menambahkan elemen baru atau merubah elemen yang sudah ada
dicto[3]="JavaScript"
dicto[1]="Python"
dicto[2]="MySQL"
dicto['c']=1
print("list dictonary yang sudah di update =",dicto)

# deleting dictonary elemen
dicto2 = {1: "makan", 2:"lagi", 'c':"iya"}
print(dicto2)
del dicto2['c'] # menhapus element pada dictonary dengan menggunakan key
print (dicto2)

dicto2.clear() # menhapus semua isi dari dictonary
print("selruh isi dari dictoray sudah di hapus",dicto2)
del dicto2 # menghapus dictodary dicto2
try :
 print(dicto2)
except NameError :
    print ("variable dicto2 sudah di hapus!")

# untuk mengetahui isi dari dicto
print(len(dicto))

# untuk meng-copy isi dari dictonary yang sudah ada 
dicto3= dicto.copy()
print(dicto3)

# merubah isi dari sebuah kumpulah element menjadi sebuah keys
keybaru = (1,2,3,4)
print(keybaru,type(keybaru))
dicto4 = dict.fromkeys(keybaru)
print(dicto4, type(dicto4))
dicto4[1] = "lagi"
dicto4[2] = "belajar"
dicto4[3] = "python"
dicto4[4] = "bambang"
print(dicto4, type(dicto4))

# items(), untuk mengembalikan dictonary menjadi sebuah tuple
print(dicto4.items(), type(dicto4.items()))

# keys untuk mengambil keys pada dictonary
allkeys = dicto4.keys()
print(allkeys, type(allkeys))

# upadate(), untuk mengapdate dictonary dengan merubah isi nya degan isi yang di pilih
dicto.update(dicto4)
print(dicto)

# value, untuk mengabil list yang ada di dictonary
print(dicto.values(), type(dicto.values()))

# set default, jadi kita akan mengeset default dari dictonary, apapun yang ingin kita tampilkan maka defauult yang aka muncul sebagain gantinya
dicto.setdefault('muhamad',"rafli")
print(dicto[1])
print(dicto['muhamad'])