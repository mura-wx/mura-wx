data = 'ini adalah string'
print(data)
print(type(data))

# 1. Cara membuat string

'''
    1. dengan mengguanakan single quote '...'
    2. dengan mengguankana double quote "..."
'''

data = 'ini menggunakan single quote'
print(data)

data = "ini menggunakan double quote"
print(data)

print('"halo pak apa kabar?"')
print("hari ini hari jum'at")

# menggunakan tanda \

# membuat tada ' menjadi string
print('mari sholat jum\'at')

# backlash
print("C:\\User\\Rafli")

# tab
print("makan \t ey")

# backspace
print("makan \bey")

# newline
print("baris pertama \nbaris kedua.") # LF --> Line Feed
print("baris pertama \rbaris kedua.") # CR --> Carriage Return
print("baris pertama \r\nbaris kedua.") # CRLF --> Line Feed Cariage Return

# 3. string literal atau raw

# raw, berfungsi untuk menguabah semua yang ada di dalam raw menjadi string
print(r"C:\\\\\makan bang")

# literal, berfungsi untuk menampilkan hasil seperti apa yang kita tulis
print(
    r"""
    nama: muhamad rafli
    umur: 19 tahun
    C:\User\rafli
    """
)