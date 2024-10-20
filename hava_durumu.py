import requests
import schedule
import time
from datetime import datetime 

# OpenWeatherMap API bilgileri
API_KEY = '0849d85a8a56d0f01458f8b3e8e2250d'  # Buraya API anahtarını eklenir
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def hava_durumu_getir(sehir):
    # API isteği için gerekli parametreler
    params = {
        'q': sehir,
        'appid': API_KEY,
        'units': 'metric',  # Sıcaklık değerini Celsius olarak almak için
        'lang': 'tr'  # Türkçe dil desteği
    }
    
    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        
        if response.status_code == 200:
            # Gerekli bilgileri ekrana bastıralım
            sehir_adi = data['name']
            sicaklik = data['main']['temp']
            aciklama = data['weather'][0]['description']
            print(f"\n{sehir_adi} için Hava Durumu:")
            print(f"Sıcaklık: {sicaklik}°C")
            print(f"Açıklama: {aciklama.capitalize()}")
        else:
            print(f"Hata: {data['message']}")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

def guncelle():
    
    # Kullanıcıdan şehir ismi alma ve hava durumunu getirme
    sehir = input("Hangi şehrin hava durumunu öğrenmek istersiniz? ")
    print("Hava durumu bilgisi güncelleniyor...")

    # Güncel tarihi ekrana yazdırma
    tarih = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\nGüncelleme zamanı: {tarih}")
    hava_durumu_getir(sehir)

guncelle()

# Program sürekli çalışacak ve her gün belirtilen saatte güncelleme yapacak
while True:
    schedule.run_pending()
    time.sleep(1)
