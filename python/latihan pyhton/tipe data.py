# tipe data: Angka satuan (integer)
data_integer= 10
print("data:", data_integer)
print("-bertipe:", type(data_integer))

# tipe data: angka dengan koma (float)
data_float= 1.10
print("data:", data_float)
print("-bertipe:", type(data_float))

# tipe data: kumpulan karakter (string)
data_string= "makan dulu bang"
print("data:", data_string)
print("-bertipe:", type(data_string))

# tipe data: biner true/false (boolean)
data_bool= True
print("data:", data_bool)
print("-bertipe:", type(data_bool))

# tipe data khusus

# bilangan kompleks
data_complex = complex(1,5)
print("data:", data_complex)
print("-bertipe:", type(data_complex))

# tipe data dari bahasa c
from ctypes import c_double
data_c_double = c_double(20.5)
print("data:", data_c_double)
print("-bertipe:", type(data_c_double))