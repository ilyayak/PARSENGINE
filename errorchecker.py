import requests
res = requests.get('https://coinmarketcap.com/all/views/all/')
print(res.status_code)