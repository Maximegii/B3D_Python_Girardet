import requests
url = 'http://127.0.0.1:8000/api/posts/'
# pas bon
#headers = {'Authorization': 'Token 9054f7aa9305e012b3c2300408c3dfdf390fcddf'}
headers = {'Authorization': 'Token 4d4cb8cf12174d16143b4c4fb07162ae53f6d0d5'}
r = requests.get(url, headers=headers)
print (r.json())
