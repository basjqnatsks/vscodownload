import requests

while True:
	v = input("Link: ")
	r = requests.get(v).text.split('="og:image" content="')[1].split('?w=')[0]
	open(v.split("media/")[1]+".jpg", "wb").write(requests.get(r).content)