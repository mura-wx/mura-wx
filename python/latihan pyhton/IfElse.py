# If dan Else

print ("masukan sebuah angka")
angka1 = input ("masukan angka pertama : ")
angka2 = input ("masukan angka kedua   : ")

if angka1 == angka2 :
    print("kedua angka yang anda masukan bernilai sama")
elif angka1 != angka2 :
    print("kedua angka yang anda masukan bernilai tidak sama")


print("\n",30 * "#")

print (10* "*","LOGIN", "*"*10)

Username_from_db = "muhammad rafli"
Password_from_db = "20092001"
temp = True
while temp :
    username = input("Username : ")
    password = input("Password : ")
    if [password, username] == [Password_from_db, Username_from_db] :
        temp = False
        print("\n","selamat datang".center(20, "#"),"\n")
    elif [password, username] != [Password_from_db, Username_from_db] :
        temp = True
        print("\nMaaf Username atau Password yang anda masukan salah!\n")
