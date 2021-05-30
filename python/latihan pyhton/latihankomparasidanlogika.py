# latihan komparasi dan logika 

# ++++++++5-------10+++++++
inputUser = float (input("masukan angka kurang dari 5\natau\nlebih dari 10\n:"))
iskurangdari = (inputUser < 5)
islebihdari = (inputUser > 10)
print("nilai yang anda masukan :", inputUser)
print('kurang dari 3 =', iskurangdari)
print("lebih dari 10 =", islebihdari)
hasilnilai = iskurangdari or islebihdari
print('hasil dari yang anda masukan adalah =', hasilnilai)

# ---------5++++++10--------
print(10*"*")
inputUser = float (input("masukan angka lebih dari 5\ndan\nkurang dari 10\n:"))
islebidari = (inputUser > 5)
iskurangdari = (inputUser < 10)
print("nilai yang anda masukan :", inputUser)
print('lebih dari 5 =', islebidari)
print("kurang dari 10 =", iskurangdari)
hasilnilai = iskurangdari and islebidari
print('hasil dari yang anda masukan adalah =', hasilnilai)