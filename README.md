# obhavo
O'zbekistondagi 12ta viloyat bo'yicha ob-havo ma'lumotlari.
### Hozirda mavjud joylashuvlar:
1.Toshkent
2.Andijon
3.Buxoro
4.Guliston
5.Jizzax
6.Zarafshon
7.Qarshi
8.Navoiy
9.Namangan
10.Nukus
11.Samarqand
12.Termiz
13.Urganch
14.Farg'ona
15.Xiva

# To'g'ri viloyat nomlari:
```
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
```

#### Eslatma: agar ingliz tilini bilsangiz inglizcha yozishingiz ham mumkin!

# Ma'lumot
Hozirda modulemizni ishlatish uchun ma'lum viloyatlar mavjud, hozirgi versiya 0.2-versiya hisoblanadi , bu modulga yangilik qo'shishga harakat qilaman
# O'rnatish
Ushbu modulni ishlatish uchun bizga BeautifulSoap4 paketi kerak bo'ladi, uni
`pip3 install bs4`
komandasi orqali o'rnatib olamiz

# Ishlatish

### Eslatma: ishlatish haqida **main.py** fayli ichida ham ma'lumot berilgan


```
# Avval import qilib olamiz

import obhavo

# Ma'lumotlarni chaqirish uchun avvalo obyekt yaratish kerak

info = obhavo.ObHavo('viloyat nomi')

#Sana

print(info.sana)

#Kunduzgi harorat

print(info.kunduz)

#Kechqurungi harorat

print(info.kechasi)

#Qo'shimcha ma'lumot

print(info.joylarda)

#Namlik

print(info.namlik)

#Shamol

print(info.shamol)

#Bosim

print(info.bosim)

#Oy

print(info.oy)

#Quyosh chiqishi

print(info.chiqish)

#Quyosh botishi

print(info.botish)

#Tongi harorat

print(info.tong)

#Kunduzgi harorat

print(info.kun)

#Oqshom harorati

print(info.oqshom)

#Haftalik ma'lumot olish uchun

print(info.haftalik())
```
