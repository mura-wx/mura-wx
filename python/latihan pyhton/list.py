#  mengenal List, Tuple , dan dictonary

# 1. list, untuk memasukan multidata pada sebuah variable
 # list menggunaka tanda [] untuk memasukan data
 # list tidak hanya dapa memasukan data berpa string atau integral tapi juga dapa memasukan data berupa variable

# untuk mengakses list bisa gunakan nama variable [jumlah indexnya], contoh datalist[2]
datalist = ["makan", "mulu", "anjing"]
print(datalist)
iya= ["jangan" ,"makan" ,"lagi", "stop"]
listbaru = datalist + iya
print(listbaru)

# python list slicing
print("\nlist slicing")
print(listbaru[3:6])#<list_name>[start:stop]
print(listbaru[5])
print(listbaru[1:7:3]) #<list_name>[start:stop:step]

# updating list
listbaru[3] = 14 # di bagian ini kita menambahkan sebuah value baru ke dalam sebuah list
print(listbaru)

# appending list, metode ini di gunakan untuk menambahkan elemen pada akhir elemen yang ada
print("\nappending")
listbaru.append(10990)
listbaru.append("data baru")
listbaru.append([1,2,3,4,5])
print (listbaru)

# extend, fungsinya hampir sama degan appeng hanya saja jika anda menambahkan sebuah bentuk list baru ke dala sebuah list makan list tersebut akan menyatu
print("\nextend")
listbaru.extend([10991])
listbaru.extend(["data baru1"])
listbaru.extend([1,2,3,4,5,6])
print (listbaru)

# insrt(), fungsinya sama juga untuk memasukan objek
print("\ninsert()")
listbaru.insert(3,'iya lkajfdah')
print(listbaru)


# pop, fungsinya untuk menhapus dengan memasukan indexnya
print("\npop()")
listbaru.pop(3)
print(listbaru)

# menhapus elemen
print("\nmengapus elemen")
del(listbaru[9])
print(listbaru)

# reverse, fungsinya untuk mengebalik unrutan dari element pada list
print("\nreverse()")
listbaru.reverse()
print(listbaru)

## list method
print("\nlist method")

# min(list)
print("min(list)")
list1 = [1,2,3,4]
lsit2 = ["iya", "bener"]
print ("nilai minimal dari list 1 adalah =",min(list1))
print("nilai minimal dari list 2 adalah =",min(lsit2))

# max(list)
print("max(list)")
list1 = [1,2,3,4]
lsit2 = ["iya", "bener"]
print ("nilai maksimal dari list 1 adalah =",max(list1))
print("nilai maksimal dari list 2 adalah =",max(lsit2))

# len, untuk mengukur jumlah elemen yang ada pada list
print("len()")
print("jumlah elemen pada list 1 adalah =", len(list1))
print("jumlah elemen pada list 2 adalah =", len(lsit2))

# list() perintah list ini untuk merubah sebuah kumpulan elemen mejadi sebuah list
print("merubah bentuk tuple menjadi list menggunakan perintah list()")
t = ('ini', 'tuple')
print(t)
new= list(t)
print (new)

# method

print ("\nmethod lagi")
# count()
Inilist = [1,2,3,'a','b','c',1,2,3]
print(Inilist)
print("jumlah angka 1 pada list =",Inilist.count(1))
print("jumlah huruf b pada list =",Inilist.count('b'))
print("jumlah angka 4 pada list =",Inilist.count(4))