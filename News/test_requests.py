import requests

websitesi_html = requests.get('https://roblox.com').text

print(websitesi_html)