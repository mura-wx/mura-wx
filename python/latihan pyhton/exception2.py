# sebuah_list = [1,2,4,5,6]
# sebuah_tuple = (1,2,3,4,5,6)
# sebuah_dictonary = {"muhammad rafli", "@muhammad09rafli", "Tangerang selatan"}

# try :
#     print(sebuah_list[10])
# except IndexError :
#     print ("eror karena")

# try :
#     print(sebuah_tuple[10])
# except IndexError :
#     print ("eror karena")

# print(sebuah_list[7])
# print(sebuah_tuple[7])

# exception Attribute error

# class persegipanjang :
#     panjang = 0
#     lebar = 0
#     def __init__ (self, p , l):
#         self.panjang = p
#         self.lebar = l

# psg_pjg = persegipanjang(10,5)

# try :
#     print ("panjang :", psg_pjg.panjang)
#     print ("lebar :", psg_pjg.lebar)
#     print ("tinggi:", psg_pjg.tinggi)
# except AttributeError :
#     print ("eror karena",)

# exception IOError

# try :
#     f = open('iya.txt')
# except IOError :
#     print("input error") 

# # multiple exception
# print("operasi pembagian")
# try :
#     angka1 = int (input("masukan angka ke-1 :"))
#     angka2 = int (input("masukan angka ke-2 :"))
#     hasil = angka1 / angka2
#     print ("hasil =", hasil )

# except ZeroDivisionError :
#     print("\nERROOR ANGKA BERAPAPUN GAK BISA DI BAGI DEGAN 0 NJIR\n".center())
# except ValueError :
#     print("\nyang di masukan angka tolol!!")

# # multiple exception 2
# print("operasi pembagian")
# try :
#     angka1 = int (input("masukan angka ke-1 :"))
#     angka2 = int (input("masukan angka ke-2 :"))
#     hasil = angka1 / angka2
#     print ("hasil =", hasil )
# except (ZeroDivisionError, ValueError,TypeError):
#     print("\nada yang salah tolol!\n")

# # Try-Except bersarang
 
# try :
#     angka1 = int (input("masukan angak ke-1 : "))
#     angka2 = int (input("masukan angak ke-2 : "))
#     hasil = angka1/angka2
#     try :
#         print("hasil", hasil)
#     except ZeroDivisionError :
#         print("angka berapapun gk bisa di bagi 0", ZeroDivisionError)
# except ValueError: 
#     print("yang di masukin itu angka bamabang !!", ValueError)

# # membuat exception sendiri

# class IntError(Exception):
#     def __init__ (self,value):
#         self.value = value

#     def __int__(self):
#         s = "hanya boleh memasukan angka" + int(self.value)
#         return s

# def cek(angka):
#     if angka == int :
#         raise IntError(angka)

# try :
#     pin = input("masukan pin : ")
#     int (pin)
# except (IntError,TypeError ):
#     print("hanya boleh memasukan angka")

# membuat finally pada exception

    
print("operasi pembagian")
while (ZeroDivisionError) :
    try :
        angka1 = int (input("masukan angka ke-1 :"))
        angka2 = int (input("masukan angka ke-2 :"))
        hasil = angka1 / angka2
        print ("hasil =", hasil)

    except (ZeroDivisionError, ValueError,TypeError):
        print("\nada yang salah tolol!\n")

    finally:
        print("coba periksa lagi apa yang anda masukan")
