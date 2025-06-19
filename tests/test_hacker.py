import requests

proxies = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890'
}

response = requests.get('https://news.ycombinator.com/', proxies=proxies, timeout=10)
print(response.status_code)
print(response.text[:200])