# Operasi Komperasi

# setiap hasil dari Operasi Kompersasi adalah boolean

# >,<=,>=,<,,==,!=,is,is not

a = 4
b = 5

# lebih dari >
print("====== lebih dari (>)")
hasil = a > 3
print(a,">",3,"=", hasil)
hasil = a > 6
print(a,">", 6,"=", hasil)
hasil = b > 5
print(b,">", 5,"=", hasil)

# kurang  dari >
print("====== kurang dari (>)")
hasil = a < 3
print(a,"<",3,"=", hasil)
hasil = a < 6
print(a,"<", 6,"=", hasil)
hasil = b < 5
print(b,">", 5,"=", hasil)

# lebih dari sama dengan >=
print("====== lebih dari sama dengan (>=)")
hasil = a >= 3
print(a,">=",3,"=", hasil)
hasil = a >= 6
print(a,">=", 6,"=", hasil)
hasil = b >= 5
print(b,">=", 5,"=", hasil)

# sama dengan sama dengan ==
print("====== sama dengan sama dengan (==)")
hasil = a == 3
print(a,"==",3,"=", hasil)
hasil = a == 6
print(a,"==", 6,"=", hasil)
hasil = b == 5
print(b,"==", 5,"=", hasil)

# tidak sama dengan !=
print("====== sama dengan sama dengan (!=)")
hasil = a != 3
print(a,"!=",3,"=", hasil)
hasil = a != 6
print(a,"!=", 6,"=", hasil)
hasil = b != 5
print(b,"!=", 5,"=", hasil)

# is 
print("===== object indentity (is)")
x = 5
y = 5
c = 6
print (x, "=", hex(id(x)))
print (y, "=", hex(id(y)))
print (c, "=", hex(id(c)))
hasil = y is x
print (y, "is", x, "=", hasil)
hasil = y is c
print (y, "is", c, "=", hasil)

# is not 
print("===== object indetity (is not)")
x = 5
y = 5
c = 6
print (x, "=", hex(id(x)))
print (y, "=", hex(id(y)))
print (c, "=", hex(id(c)))
hasil = y is not x
print (y, "is not", x, "=", hasil)
hasil = y is not c
print (y, "is not", c, "=", hasil)