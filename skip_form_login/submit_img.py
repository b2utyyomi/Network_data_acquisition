import requests

files = {'uploadFile': open('/media/hadoop/TAEKWOON/PYTHON/Net_data/store_data/logo.jpg', 'rb')}
r = requests.post("http://pythonscraping.com/files/processing2.php", files=files)

print(r.text)
