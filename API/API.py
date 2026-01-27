import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=38.72&longitude=-9.14&current_weather=true"
res = requests.get(url)

if res.status_code == 200:
    clima = res.json()
    print("Temperatura atual:", clima["current_weather"]["temperature"], "°C")