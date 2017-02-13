import requests
url_1 = "http://localhost:5000/greeting/ruth"
r1 = requests.get(url_1)

print(r1.text)

url_2 = "http://localhost:5000/"
r2 = requests.get(url_2)

print(r2.text)

url_3 = "http://localhost:5000/birthday"
r3 = requests.get(url_3)

print(r3.text)
