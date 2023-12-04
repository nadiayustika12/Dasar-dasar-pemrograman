hasil_akhir = [
    {'nama':'Reza', 'nilai':70}, 
    {'nama':'Ciut', 'nilai':63}, 
    {'nama':'Dian', 'nilai':80}, 
    {'nama':'Badu', 'nilai':40} 
]

def lulus_saja(data):
    lulus = []
    for mhs in data:
        if mhs ['nilai'] >= 65:
            lulus.append(mhs['nama'])
    return lulus

print(lulus_saja(hasil_akhir))

fruits = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
def balikan(list):
    hasil = []
    for item in list:
        hasil.insert(0, item)
    return hasil

print(balikan(fruits))

daftar_buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
duplikasi_buah = []

for buah in daftar_buah:
    duplikasi_buah.append(buah)
    duplikasi_buah.append(buah)

print(duplikasi_buah)

kampus = "Nurul Fikri"
print(kampus[::2].replace('i','r'))