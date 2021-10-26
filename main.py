from obhavo import ObHavo

#Parse from http://obhavo.uz

# Ma'lumotlar

# To'g'ri viloyat nomlari:
'''
tashkent
jizzakh
andijan
namangan 
ferghana
gulistan
bukhara 
zarafshan
karshi
navoi
nukus
termez
urgench
khiva
samarkand
'''

t = ObHavo("toshkent")

print("Sana:", t.sana)
print("Kunduzi", t.kunduz)
print("Kechasi:", t.kechasi)
print("Namlik:", t.namlik)
print("Shamol:", t.shamol)
print("Bosim:", t.bosim)
print("Oy:", t.oy)
print("Quyosh chiqishi:", t.chiqish)
print("Quyosh botishi:", t.botish)
print("Tong:", t.tong)
print("Kun:", t.kun)
print("Oqshom:", t.oqshom)

# Haftalik ma'lumot

print(t.haftalik())
