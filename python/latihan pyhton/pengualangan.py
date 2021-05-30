# pengulangan for dan while

# 1. for
judul = "FOR"
print("\n", judul.center(45, "=") )

# pengulangan menggunakan list

judul = "pengulangan list"
print("\n", judul.center(35, "=") )
for i in [1,2,3,4,5]:
    print("pengulangan ke -", i) #untuk pengulangan menggunakan list dapa juga di lakukan dengan bentuk string

# pengulangan string
judul = "pengulangan string"
print("\n", judul.center(35, "=") )
for srt in "abc":
    print(srt, "adalah huruf abjad") 

# pengulangan menggunakan range

judul = "pengulangan range"
print("\n", judul.center(35, "="))
for r in range(1, 10):
    print("ini pengulangan ke -", r)

# 2. While

judul = "WHILE"
print("\n", judul.center(45, "=") )
x = 0
while (x < 10):
    print ("mengulang ke -", x)
    x +=1

Tanya = True
while Tanya :
    temp = int(input("masukan angka kurang dari 10!! : "))
    if temp <  10 :
        Tanya = False
        print("Jawabannya bener pak")
    else :
        Tanya = True
        print ("Salah, ulang lagi!!")

# pengulangan akan terus di lakukan selama nilai yang di masukan bernilai True 