# operator dalam bentuk motd

## merubah case dari string

# semua ke upper
salam = "bacot"
print("normal :", salam)
print("upper  :",salam.upper())

# semua ke lower
salam = "Iya JuGa yA"
print("normal :", salam)
print("lower  :",salam.lower())

## pengecekan dengan isx method

# contoh pengecekan lower case dan upper case

print("\n",30 *"#")
data = "nama saya"
data2 = "NAMA SAYA"
data3 = "Rafli 20092001"
print("apakah", data, "islower =", data.islower())
print("apakah", data2, "islower =", data2.islower())
print("apakah", data2, "isupper =", data2.isupper())

# isalpha() <-- untuk mengecek huruf
# isalnum() <-- untuk mengecek huruf
# isdecimal() <-- untuk mengecek huruf
# isspace() <-- untuk mengecek huruf
# istittle() <-- untuk mengecek huruf

print("apakah", data3, "isalpha =", data3.isalpha())
print("apakah", data3, "isdecimal =", data3.isdecimal())
print("apakah", data3, "isalnum =", data3.isalnum())
print("apakah", data3, "isupper =", data3.isupper())
print("apakah", data3, "islower =", data3.islower())
print("apakah", data3, "istitle =", data3.istitle())
print("apakah", data3, "isspace =", data3.isspace())

## ngecek komponen startswith() dan endswith()

nama = "Muhamad rafli"

print("\napakah kata", nama , "startswith Muhamad =", nama.startswith("Muhamad"))
print("apakah kata", nama , "endswith rafli =", nama.endswith("rafli"))

# join
variable = ["makan", "dulu", "tong"]
iyajoin = " ".join(variable)
print(variable)
print(iyajoin)

# split
gabung = "ah masa si gk gitu lohhhh ya kali"
print(gabung)
print (gabung.split(" "))

# alokasi karakter

print(10*"#", "BACOT", "#" *10)

# rjust(), ljust(), center()

contoh = "IYAKAH"
contoh2 = contoh.ljust(10,"-")

print('"'+contoh.rjust(10, "-")+'"')
print('"'+contoh.center(10, "-")+'"')
print('"'+contoh.ljust(10, "-")+'"')

# strip untuk menhilangkan fungsi rjust,center,dan ljust
strip = "apakah s saya s mengantuk?"
print(contoh2.strip("-"))