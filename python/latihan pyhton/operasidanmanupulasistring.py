# operasi dan manipulasi string

# 1. menyambung string (concatenate)
n_pertama = "Rafli"
n_kedua = "D"
n_ketiga = "Facto"

nama_lengkap = n_pertama +" "+ n_kedua +"'"+ n_ketiga
print(nama_lengkap)

# 2. menghitung panjang string
panjang = len(nama_lengkap)
print("jumlah karakter dari",'"' + nama_lengkap + '"', " adalah =", panjang)

# 3. operator untuk string

# mengecek apakah ada komponen char atau string di string (in)

char = "Rafli"
status = char in nama_lengkap
print ("apakah kata",'"' + char + '"', "ada di dalam kaliamat", nama_lengkap, "=", status)

char = "KONTOL"
status = char in nama_lengkap
print ("apakah kata",'"' + char + '"', "ada di dalam kaliamat", nama_lengkap, "=", status)
char = "KONTOL"

status = char not in nama_lengkap
print ("apakah kata",'"' + char + '"', "tidak ada di dalam kaliamat", nama_lengkap, "=", status)

# mengulang string
print("MAMPUS " *20)

# indexing
print("index ke-0 :", nama_lengkap[0])
print("index ke-(-1) :", nama_lengkap[-1])
print("index ke-(0:5) :", nama_lengkap[0:5])
print("index ke-(0:5:2) :", nama_lengkap[0:5:3]) # artinya adalah 0 dengan range 5 dan longkap 2

# item paling kecil
print("paling kecil :", min(nama_lengkap))

# item paling besar
print("paling besar :", max(nama_lengkap))

ascci_code = ord("t")
print("ascci code pada hurt t adalah :",ascci_code)

# 4. operator dalam bentuk motd

data = "makan dulu yakan yakali gak makan nanati sakit kan nnn"
jumlah = data.count("n")
print(r'jumlah huruf "n" pada', data, "=", jumlah)