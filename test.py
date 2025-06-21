import requests

email = '123arp@gmail.com'
url = f'https://leakcheck.net/api/public?check={email}'

response = requests.get(url)
print(response.status_code)
print(response.json().get('sources'))
print(response.json().get('success'))

if response.json().get('success'):
    print("Email found in data leaks.")