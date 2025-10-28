import requests

temps = []
urls = [
    'https://api.opensensemap.org/boxes/5eba5fbad46fb8001b799786/sensors/5eba5fbad46fb8001b799789',
    'https://api.opensensemap.org/boxes/5c21ff8f919bf8001adf2488/sensors/5c21ff8f919bf8001adf248d',
    'https://api.opensensemap.org/boxes/5ade1acf223bd80019a1011c/sensors/5ade1acf223bd80019a1011e'
]

for url in urls:
    response = requests.get(url)
    data = response.json()
    temp = data['lastMeasurement']['value']
    temps.append(float(temp))

average_temps = sum(temps) / len(temps)

def health_check(urls):
    accessible = 0

    for url in urls:
        try:
            response = requests.head(url, timeout=5)
            if response.status_code == 200:
                accessible += 1
        except requests.exceptions.RequestException as e:
            print(f"{url} inaccessible. error: {e}")

    return accessible >= (len(urls) / 2)