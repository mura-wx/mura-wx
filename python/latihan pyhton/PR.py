# ini tugas !!!!!!!

# -----0+++++5-----8++++++11-------
inputUser = float(input("masukan angka lebih dari 0 dan kurang dari 5\natau\nlebih dari 8 dan kurang dari 11\n:"))

angak0_5 = inputUser > 0 and inputUser < 5
angak8_11 = inputUser > 8 and inputUser < 11
hasil = angak0_5 or angak8_11

print("Angka yang anda masukan :", inputUser)
print("> 0 dan < 5 =", angak0_5)
print("> 8 dan < 11 =", angak8_11)
print("hasil dari nilai yang anda masukan =", hasil)

# +++++0-----5+++++8------11+++++
print(100*"$")
inputUser = float(input("masukan angka kurang dari 0\n atau lebih dari 5 dan 8 \natau lebih dari 11\n:"))

angak5_8 = inputUser > 5 and inputUser < 8
kurangdari0 = inputUser < 0
lebihdari11 = inputUser > 11
hasil = angak5_8 or kurangdari0 or lebihdari11

print("Angka yang anda masukan :", inputUser)
print("> 0 dan < 5 =", angak5_8)
print("< 0 =", kurangdari0)
print("> 11 =", lebihdari11)
print("hasil dari nilai yang anda masukan =", hasil)