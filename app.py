from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)

API_KEY = '0849d85a8a56d0f01458f8b3e8e2250d'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def hava_durumu_getir(sehir):
    params = {
        'q': sehir,
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'tr'
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        sicaklik = data['main']['temp']
        aciklama = data['weather'][0]['description']
        icon = hava_durumu_ikonu(aciklama)
        return sicaklik, aciklama.capitalize(), icon
    else:
        return None, None, None

def hava_durumu_ikonu(aciklama):
    if 'bulutlu' in aciklama:
        return 'fas fa-cloud'
    elif 'güneşli' in aciklama:
        return 'fas fa-sun'
    elif 'yağmur' in aciklama:
        return 'fas fa-cloud-rain'
    else:
        return 'fas fa-smog'

@app.route('/', methods=['GET', 'POST'])
def index():
    sehir = ''
    sicaklik = ''
    aciklama = ''
    icon = ''
    tarih = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if request.method == 'POST':
        sehir = request.form['city']
        sicaklik, aciklama, icon = hava_durumu_getir(sehir)

    return render_template('index.html', sehir=sehir, sicaklik=sicaklik, 
                           aciklama=aciklama, icon=icon, tarih=tarih)

if __name__ == '__main__':
    app.run(debug=True)
