import requests
url_1 = "http://localhost:5000/greeting/ruth"
r1 = requests.get(url_1)

print(r1.text)

url_3 = "http://localhost:5000/birthday"
r3 = requests.get(url_3)

print(r3.text)

url_4 = "http://localhost:5000/sum/3/5"
r4 = requests.get(url_4)

print(r4.text)

url_5 = "http://localhost:5000/product/3/5"
r5 = requests.get(url_5)

print(r5.text)

url_6 = "http://localhost:5000/favoritefoods"
r6 = requests.get(url_6)

print(r6.text)

