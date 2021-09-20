import requests
from bs4 import BeautifulSoup

url = 'https://www.york.ac.uk/teaching/cws/wws/webpage1.html'

response = requests.get(url)
print(response.status_code)
# page = response.text

# soup = BeautifulSoup(page, 'html.parser')
# print(soup.prettify())