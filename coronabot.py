from selenium import webdriver
import requests
import json
import time
import datetime

date = datetime.datetime.now()
url = 'https://api.kawalcorona.com/indonesia'
# url = 'http://localhost/yusufprananda/data.json'
response = requests.get(url).text
data = json.loads(response)

chrome_browser = webdriver.Chrome(executable_path='C:\Program Files (x86)\chromedriver.exe')
chrome_browser.get('https://web.whatsapp.com/')

time.sleep(15)

username_list = ["Muhammad Yusuf Prananda", "Della Sayang Love", "Moetjaba TI", "Bangfik TI", "Valir TI", "Enggarra TI", "Empud TI", "Winda TI", "Wanandi MASTER", "Ade Nara TI", "Bayu TI"]
waktu = True
while (waktu == True):
    if (date.strftime("%H:%M") == "21:00"):
        response = requests.get(url).text
        data = json.loads(response)
        for username in username_list:
            userplace = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(username))
            userplace.click()
            message_box = chrome_browser.find_element_by_xpath('//div[@class="_3uMse"]')
            # message_box.send_keys("*UPDATE COVID-19*\nPada hari ini, tanggal " + date.strftime("%d/%m/%Y") + ", total perkembangan penyebaran COVID-19 di Indonesia adalah sebagai berikut:\nKorban Positif: *" + data[0]["positif"] + "*\nKorban Sembuh: *" + data[0]["sembuh"] + "*\nKorban Meninggal: *" + data[0]["meninggal"] + "*\nKorban Dirawat: *" + data[0]["dirawat"] + "*\nUntuk informasi lebih lengkap, silahkan akses di https://kawalcovid19.id/\n BOT by Muhammad Yusuf Prananda")
            message_box.send_keys("Mohon maaf ini hanya pesan percobaan guna penyempurnaan sistem. Silahkan abaikan pesan ini. Mohon maaf menganggu.\n")
            # message_box = chrome_browser.find_element_by_xpath('//button[@class="_1U1xa"]')
            # message_box.click()
            print("Pesan telah terkirim ke " + username)
            time.sleep(5)
        break
    else:
        print("Belum waktunya!")
        print("Sekarang masih pukul " + date.strftime("%H:%M"))
        date = datetime.datetime.now()
        time.sleep(30)
