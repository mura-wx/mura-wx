# # membuat fungtion

# # 1. fungtion tanpa return

# print("fungtion tanpa return".center(45, "#"))
# def tanpa_parameter():
#     for i in range(1,5):
#         print("looping ke -", i)
# def dengan_parameter(akhir):
#     for i in range(1,akhir):
#         print("looping ke -",i)
    

# # fungtion tanpa parameter
# print ("tanpa parameter".center(30, "*"))
# print("contoh fungtion tanpa parameter")
# print("hasil =",tanpa_parameter())

# # fungtion dengan parameter
# print ("dengan parameter".center(30, "*"))
# print("contoh fungtion dengan parameter")
# print("hasil =",dengan_parameter(11))

# # 2. fungtion yang menggunakan return

# print("fungtion dengan return".center(45, "#"))
# def withoutparameter() :
#     temp = 0
#     for i in range(1,5):
#         temp += i
#         print ("looping ke -", i)
#     return temp

# def withparameter(hasil) :
#     temp = 0
#     for i in range(1,hasil) :
#         temp += i
#         print("looping ke -", i)
#     return temp

# print ("tanpa parameter".center(30, "*"))
# print ("hasil",withoutparameter())

# print ("dengan parameter".center(30, "*"))
# print ("hasil",withparameter(10))

# def sum(x,y):
#     print("Adding the two vallues")
#     print("Printing within function")
#     print(x+y)
#     return x+y

# def msg():
#     print("hello")
#     return

# total=sum(10,20)
# print("total :", total)
# msg()
# print("rest of code")

# Function argument
# ada empat macam argument yaitu:
# 1. Requiered argument
# 2. keyword arguments
# 3. Default arguments
# 4. Variable_legth arguments


# Required argument
def cube(x):
    "this x a passed num value into this function, return cube of x"
    y =x*x*x
    return y
    
z = cube(2)
print (z)

# Keyword Arguments
def remainder(data1,data2):
    x=data1%data2
    return x

rem = remainder(data1=10, data2=3)
print("remainder of 3%3 =", rem)

# Default argument
def datadiri(nama,emp_id,umur,company="tidak di isi"):
    print("Details of", nama)
    print("Id".ljust(11),":",emp_id)
    print("Umur".ljust(11),":",umur)
    print("Pekerjaan".ljust(11),":",company)

datadiri("Muhammad Rafli", 10001, 19, "Network engineer")
print("".center(40,"-"))
datadiri("Muhammad Rafli", 10001, 19)

# variabel legth argument
def jajal(data1,*datatuple):
    print("yang ini data1 :",data1)
    print("yang ini datatuple :",datatuple)
    return

jajal(100,11,22,43,53,"jaman")


# labda function(anonymous function)
# ini contoh lamda ya semoga gw jauh lebih baik lagi untuk memahami nya wkwkwk
iya = lambda x : x*x
print(iya(2))

# scape of variable