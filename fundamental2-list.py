# TIPE DATA LIST
buah = ['jeruk', 'nenas', 'pepaya', 'rambutan']
print(buah)
buah.append('salak')
print(buah)

#sorting
print(f'Aku mau {buah[2]}')

#perulangan cara simpel
for i in buah:
    print(f'Saya suka {i}')

#perulangan cara ribet
for i in range(0,len(buah)):
    print(f'{i+1}.Saya suka buah {buah[i]}')

