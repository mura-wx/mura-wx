import test 
x = test.add(10,2)
print('x =', x)

# bisa peke from, tuh kalo from contohnya kayak gitu, simak ya
from test import fib
print(fib(100))

# kalian bisa import fungsi math gais

import math
a= 4.3
print(math.ceil(a))
print(math.floor(a)) # untuk membulatkan bilangan
b=9
print(int(math.sqrt(b))) # untuk mengembalikan akar kuadrat dari nomor yang diberikan
print(math.exp(3.0)) # untuk mengembalikan logaritma alami yang di anjurkan ke nomor yang di berikan berikan
print(math.log(2.0)) # ini mengembalikan jumlah integer sebelumnya dari nomor yang diberikan
print(math.pow(2.0,3.0))
print(math.sin(60))
print(math.cos(60))
print(math.tan(60))
print(math.pi) #ini pi ya
print(math.e)

# random
import random
print(random.random) # untuk mengembalikan nomor acak antara 0.0 and 1.0 dimana 1.0 adalah  ekslusif
print(random.randint(1,10)) # untuk mengebalikan nomor acak antara x dan y dimana keduanya adalah termasuk