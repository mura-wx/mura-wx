# operasi logika atau boolean

# not, or, and, xor

# NOT
print("=====NOT=====")
a = False
b = not a
print('data a =', a)
print('--------NOT')
print("data b =", b)

# OR
print("=====OR=====")
a = False
b = False
c = a or b
print(a,"OR",b,"=",c)
a = True
b = False
c = a or b
print(a," OR",b,"=",c)
a = False
b = True
c = a or b
print(a,"OR",b,"=",c)
a = True
b = True
c = a or b
print(a," OR",b,"=",c)

#AND
print("====AND=====")
a = False
b = False
c = a and b
print(a,"AND",b,"=",c)
a = True
b = False
c = a and b
print(a," AND",b,"=",c)
a = False
b = True
c = a and b
print(a,"AND",b,"=",c)
a = True
b = True
c = a and b
print(a," AND",b,"=",c)

# XOR
print("=====XOR=====")
a = False
b = False
c = a ^ b
print(a,"XOR",b,"=",c)
a = True
b = False
c = a ^ b
print(a," XOR",b,"=",c)
a = False
b = True
c = a ^ b
print(a,"XOR",b,"=",c)
a = True
b = True
c = a ^ b
print(a," XOR",b,"=",c)