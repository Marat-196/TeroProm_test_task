import requests

url = "https://www.gismeteo.ru/api/"

params = {
    "city": "New York"
}

headers = {
    "Accept": "application/json",
    "Authorization": "fsq3YW7XKLfdoXm3kTdb5Oh9VmCfBfZtHbi86d4D2G/Gy/4="
}

response = requests.request("GET", url, params=params, headers=headers)

print()