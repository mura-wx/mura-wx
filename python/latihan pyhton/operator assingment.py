# operator assignment

a = 10
a += 1
print("nilai a += 1","menjadi", a)
a -= 1
print("nilai a -= 1","menjadi", a)
a *= 4
print("nilai a *= 4","menjadi", a)
a /= 2
print("nilai a /= 2","menjadi", a)
a //= 3
print("nilai a //= 3","menjadi", a)
a **= 3
print("nilai a **= 3","menjadi", a)
a %= 3
print("nilai a %= 3","menjadi", a)


# operasi bitwise
# OR
c = True
print("\nnilai c =", c)
c |= False
print("nilai c |= False","menjadi", c)

c = False
print("nilai c =", c)
c |= False
print("nilai c |= False","menjadi", c)

# AND
c = True
print("\nnilai c =", c)
c &= False
print("nilai c &= False","menjadi", c)

c = True
print("nilai c =", c)
c &= True
print("nilai c &= False","menjadi", c)

# XOR
c = True
print("\nnilai c =", c)
c ^= False
print("nilai c ^= False","menjadi", c)

c = True
c ^= True
print("nilai c ^= False","menjadi", c)

# geser - geser
d = 10
print("\nnilai d =", format (d, '04b'))

d >>= 2
print("nilai d >>= 2","menjadi", format (d, '04b'))
d <<= 2
print("nilai d <<= 2","menjadi", format (d, '04b'))