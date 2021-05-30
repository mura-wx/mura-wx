# membuat program atm sederhana menggunakan python

print("Selamat datang di ATM BAPAKKAU")
print("Silakan pilih option di bawah ini :")
print("1. Cek jumlah rekening")
print("2. Tarik rekening")
print("3. masukan uang ke dalam rekening")
print("0. kembali")
option = int(input("input : "))
rekening = 0
if option==1 :
    print("jumlah rekening anda = ",  rekening)
    print("0. kembali")
    option = int(input("input : "))
elif option==2 :
    print ("Jumlah saldo anda :", rekening)
    print("Pilih julmlah penarikan pada rekening :")
    print ("1.RP 50.000")
    print ("2.RP 100.000")
    print ("3.RP 200.000")
    print ("4.RP 300.000")
    print ("5.RP 400.000")
    print ("6.RP 500.000")
    print("0. kembali")
    option2 = int(input("input : "))
    tumb = 0
    if rekening <= tumb :
        print("saldo anda tidak cukup !")
    elif option2 == 1 :
        tumb = 50000
        rekening -= tumb
        print("uang kamu sekarnga berjumlah :", rekening)
    elif option == 2 :
        rekening -= 100000
        print("uang kamu sekarnga berjumlah :", rekening)
    elif option == 3 :
        rekening -= 20000
        print("uang kamu sekarnga berjumlah :", rekening)
    elif option == 4 :
        rekening -= 3000000
        print("uang kamu sekarnga berjumlah :", rekening)
    elif option == 5 :
        rekening -= 4000000
        print("uang kamu sekarnga berjumlah :", rekening)
    elif option == 6 :
        rekening -= 5000000
        print("uang kamu sekarnga berjumlah :", rekening)
elif option ==3 :
    print ("Jumlah saldo anda :", rekening)
    print("silakan masukan jumlah saldo yang ingin anda masukan :")
    rekening = int(input("inpunt : "))
    


