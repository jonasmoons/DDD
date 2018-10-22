"""
To see an example of the Wikipedia API JSON look at this url:
https://en.wikipedia.org/api/rest_v1/page/summary/Japanese_cuisine
"""
import requests



def request(title, value):
	if req.status_code != 200:
		print(f"We got an error: {req.status_code}")
		exit()
	else:
		if want_url == "y":
			print(url)
		return content(title, value)	

def content(title, value):
	if value == "extract":
		data = req.json()
		return data["extract"]
	else:
		data = req.json()
		return data["description"]


title = input("Give an article you want to lookup").strip()
value = input("Do you want the description or the extract?").strip().lower()
want_url = input("Do you want to see the URL? y/n").strip().lower()
url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"
req = requests.get(url)


data = request(title, value)
print(data)

