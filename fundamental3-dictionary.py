# dictionary

kamus = {}
kamus['anak'] = 'son'
kamus['istri'] = 'wife'
kamus['ayah'] = 'father'
kamus['ibu'] = 'mother'
print(kamus)

print('\nData driver gojek disekitar pengguna aplikasi')
data_dari_server = {
    'tanggal': '2021-07-14',
    'driver_list': [
        {'nama': 'eka', 'jarak': 10},
        {'nama': 'dwi', 'jarak': 30},
        {'nama': 'tri', 'jarak': 100},
        {'nama': 'catur', 'jarak': 1000}
    ]
}

print(data_dari_server)
print(f"\nDriver disekitar sini {data_dari_server['driver_list']}")
print(f"Driver #1 {data_dari_server['driver_list'][0]}")
print(f"Driver no.1 berjarak {data_dari_server['driver_list'][0]['jarak']} meter")