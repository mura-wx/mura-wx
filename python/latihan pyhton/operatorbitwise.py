# operator bitwise di gunakan untuk mengkalkulasi bilangan biner dengan operator logika

# | & ^ ~

# bitwise OR (|)
a = 10
b = 11

c = a | b

print("==============OR==============")
print('nilai a:',a, 'biner :',format(a, '08b'))
print('nilai b:',b, 'biner :',format(b, '08b'))
print("----------------------------- (|)")
print("hasil", c, "binary :", format(c, '08b'))

# bitwise AND (&)
c = a & b

print("==============AND==============")
print('nilai a:',a, 'biner :',format(a, '08b'))
print('nilai b:',b, 'biner :',format(b, '08b'))
print("----------------------------- (&)")
print("hasil", c, "binary :", format(c, '08b'))

# bitwise XOR (^)
c = a ^ b

print("==============XOR==============")
print('nilai a:',a, 'biner :',format(a, '08b'))
print('nilai b:',b, 'biner :',format(b, '08b'))
print("----------------------------- (&)")
print("hasil", c, "binary :", format(c, '08b'))

# bitwise NOT (~)
c = ~ a
d = ~ b
print("==============NOT==============")
print('nilai a:',a, 'biner :',format(a, '08b'))
print('nilai b:',b, 'biner :',format(b, '08b'))
print("----------------------------- (~)")
print("hasil not a", c, "binary :", format(c, '08b'))
print("hasil not b", d, "binary :", format(d, '08b'))