import requests
from bs4 import BeautifulSoup
from time import sleep

class Weather:
    def __init__(self,viloyat):
        
        self.viloyat = viloyat
        
        
        url = f"http://obhavo.uz/{viloyat}"
        r =  requests.get(url)
        soup = BeautifulSoup(r.content,"html.parser")

        print("Viloyat nomi to'g'ri yozilganligiga ishonch hosil qiling, nomlarni ingliz tilida imlo xatolarisiz yozing!")
        sleep(5)
        print("Kuting...")
        sleep(1)
        print("Tayyor!!!")
        sleep(1)
        print("Natija:")

        print(f"{viloyat.capitalize()}da:")
        
        # Sana
        sana = soup.find("div",class_='current-day').get_text()
        sana_split = sana.split(",")
        self.sana = sana_split[1].strip()
        
        # Kunduzgi ob-havo
        kunduz = soup.find("div",class_="current-forecast").get_text()
        kunduz_split = kunduz.split()
        self.kunduz = kunduz_split[0].strip()        

        #Kechasi
        kechasi = soup.find("div",class_="current-forecast").get_text()
        kechasi_split = kechasi.split()
        self.kechasi = kechasi_split[1].strip()

        # Ayrim Joylarda
        joylarda = soup.find("div",class_="current-forecast-desc").get_text()
        joylarda_split = joylarda.split()
        self.joylarda = f"{joylarda_split[0]} {joylarda_split[1]}"

        #Qolgan ma'lumotlar
        infos = soup.find("div",class_="col-1").get_text()
        infos_split = infos.split()
        
        #Namlik
        namlik = infos_split[1].strip()
        self.namlik = namlik

        #Shamol 
        shamol = f"{infos_split[3]} {infos_split[4]} {infos_split[5]}"
        self.shamol = shamol.strip()

        #Bosim
        bosim = f"{infos_split[7]} {infos_split[8]} {infos_split[9]} {infos_split[10]}"
        self.bosim = bosim

        #Infos
        infos2 = soup.find("div",class_='col-2').get_text()
        infos2_split = infos2.split()

        #Oy 
        oy = f"{infos2_split[1]} {infos2_split[2]}"
        self.oy = oy

        #Quyosh chiqishi
        chiqish = f"{infos2_split[5]}"
        self.chiqish = chiqish
        
        #Quyosh botishi
        botish = f"{infos2_split[8]}"
        self.botish = botish 

        # Infos
        infos3 = soup.find("div",class_="current-forecast-day").get_text()
        infos3_split = infos3.split()
        self.infos = infos3_split

        #Tong 
        tong = infos3_split[1]
        self.tong = tong

        #Kun 
        kun = infos3_split[3]
        self.kun = kun

        #Oqshom 
        oqshom = infos3_split[5]
        self.oqshom = oqshom

        

    # Haftalik Ma'lumot
    def haftalik(self,viloyat):

        url = f"http://obhavo.uz/{viloyat}"
        r =  requests.get(url)
        soup = BeautifulSoup(r.content,"html.parser")
        
        # Haftalik

        all_info_kun = kun1 = soup.find_all("td",class_="weather-row-day")

        # Kun 1
        kun1 = all_info_kun[0].get_text()
        kun1_split = kun1.split()
        kun1_result = f"{kun1_split[1]} {kun1_split[2]}".strip()
        
        #Kun 2 
        kun2 = all_info_kun[1].get_text()
        kun2_split = kun2.split()
        kun2_result = f"{kun2_split[1]} {kun2_split[2]}"

        #Kun 3
        kun3 = all_info_kun[2].get_text()
        kun3_split = kun3.split()
        kun3_result = f"{kun3_split[1]} {kun3_split[2]}"

        #Kun 4
        kun4 = all_info_kun[3].get_text()
        kun4_split = kun4.split()
        kun4_result = f"{kun4_split[1]} {kun4_split[2]}"

        #Kun 5
        kun5 = all_info_kun[4].get_text()
        kun5_split = kun5.split()
        kun5_result = f"{kun5_split[1]} {kun5_split[2]}"

        #Kun 6
        kun6 = all_info_kun[5].get_text()
        kun6_split = kun6.split()
        kun6_result = f"{kun6_split[1]} {kun6_split[2]}"

        #Kun 7
        kun7 = all_info_kun[6].get_text()
        kun7_split = kun7.split()
        kun7_result = f"{kun7_split[1]} {kun7_split[2]}"

        all_info_harorat = soup.find_all("td",class_="weather-row-forecast")

        #Harorat 1
        harorat1 = all_info_harorat[0].get_text()
        harorat1_split = harorat1.split()
        harorat1_result = f"\nKunduzi: {harorat1_split[0]}\nKechasi: {harorat1_split[1]}"

        #Harorat 2
        harorat2 = all_info_harorat[1].get_text()
        harorat2_split = harorat1.split()
        harorat2_result = f"\nKunduzi: {harorat2_split[0]}\nKechasi: {harorat2_split[1]}"

        #Harorat 3
        harorat3 = all_info_harorat[2].get_text()
        harorat3_split = harorat3.split()
        harorat3_result = f"\nKunduzi: {harorat3_split[0]}\nKechasi: {harorat3_split[1]}"

        #Harorat 4
        harorat4 = all_info_harorat[3].get_text()
        harorat4_split = harorat4.split()
        harorat4_result = f"\nKunduzi: {harorat4_split[0]}\nKechasi: {harorat4_split[1]}"

        #Harorat 5
        harorat5 = all_info_harorat[4].get_text()
        harorat5_split = harorat5.split()
        harorat5_result = f"\nKunduzi: {harorat5_split[0]}\nKechasi: {harorat5_split[1]}"
        self.har = harorat5_split
        #Harorat 6
        harorat6 = all_info_harorat[5].get_text()
        harorat6_split = harorat6.split()
        harorat6_result = f"\nKunduzi: {harorat6_split[0]}\nKechasi: {harorat6_split[1]}"

        #Harorat 7
        harorat7 = all_info_harorat[6].get_text()
        harorat7_split = harorat7.split()
        harorat7_result = f"\nKunduzi: {harorat7_split[0]}\nKechasi: {harorat7_split[1]}"

        all_info_tavsif = soup.find_all("td",class_="weather-row-desc")

        #Tavsif 1
        tavsif1  = all_info_tavsif[0].get_text()
        tavsif1_split = tavsif1.strip()
        tavsif1_result = tavsif1_split

        #Tavsif 2
        tavsif2  = all_info_tavsif[1].get_text()
        tavsif2_split = tavsif2.strip()
        tavsif2_result = tavsif2_split

        #Tavsif 3
        tavsif3  = all_info_tavsif[2].get_text()
        tavsif3_split = tavsif3.strip()
        tavsif3_result = tavsif3_split

        #Tavsif 4
        tavsif4  = all_info_tavsif[3].get_text()
        tavsif4_split = tavsif4.strip()
        tavsif4_result = tavsif4_split

        #Tavsif 5
        tavsif5  = all_info_tavsif[4].get_text()
        tavsif5_split = tavsif5.strip()
        tavsif5_result = tavsif5_split

        #Tavsif 6
        tavsif6  = all_info_tavsif[5].get_text()
        tavsif6_split = tavsif6.strip()
        tavsif6_result = tavsif6_split

        #Tavsif 7
        tavsif7  = all_info_tavsif[6].get_text()
        tavsif7_split = tavsif7.strip()
        tavsif7_result = tavsif7_split

        all_info_yogin = soup.find_all("td",class_="weather-row-pop")

        # Yog'ingarchilik 1
        yogin1 = all_info_yogin[0].get_text()
        yogin1_result = yogin1.strip()

        # Yog'ingarchilik 2
        yogin2 = all_info_yogin[1].get_text()
        yogin2_result = yogin2.strip()

        # Yog'ingarchilik 3
        yogin3 = all_info_yogin[2].get_text()
        yogin3_result = yogin3.strip()

        # Yog'ingarchilik 4
        yogin4 = all_info_yogin[3].get_text()
        yogin4_result = yogin4.strip()

        # Yog'ingarchilik 5
        yogin5 = all_info_yogin[4].get_text()
        yogin5_result = yogin5.strip()

        # Yog'ingarchilik 6
        yogin6 = all_info_yogin[5].get_text()
        yogin6_result = yogin6.strip()

        # Yog'ingarchilik 7
        yogin7 = all_info_yogin[6].get_text()
        yogin7_result = yogin7.strip()

        # Haftalik Natija

        hafta = f"""1 hatfalik ob-havo ma'lumotlari!
Kun: {kun1_result}
Harorat: {harorat1_result}
Tavsif: {tavsif1_result}
Yog'ingarchilik: {yogin1_result}

Kun: {kun2_result}
Harorat: {harorat2_result}
Tavsif: {tavsif2_result}
Yog'ingarchilik: {yogin2_result}

Kun: {kun3_result}
Harorat: {harorat3_result}
Tavsif: {tavsif3_result}
Yog'ingarchilik: {yogin3_result}

Kun: {kun4_result}
Harorat: {harorat4_result}
Tavsif: {tavsif4_result}
Yog'ingarchilik: {yogin4_result}

Kun: {kun5_result}
Harorat: {harorat5_result}
Tavsif: {tavsif5_result}
Yog'ingarchilik: {yogin5_result}

Kun: {kun6_result}
Harorat: {harorat6_result}
Tavsif: {tavsif6_result}
Yog'ingarchilik: {yogin6_result}

Kun: {kun7_result}
Harorat: {harorat7_result}
Tavsif: {tavsif7_result}
Yog'ingarchilik: {yogin7_result}
"""
        return  hafta












