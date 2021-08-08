from obhavo import ObHavo

# Author: Akmal Isakulov
# All rights reserved, yana bilmadim shunaqa bo'lsa kerak
# Telegram channel: https://t.me/pythusuz

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

t = ObHavo("tashkent")

print("Sana:", t.sana)
print("Kunduzi", t.kunduz)
print("Kechasi:", t.kechasi)
print("Ayrim joylarda:", t.joylarda)
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

print(t.haftalik("tashkent"))
