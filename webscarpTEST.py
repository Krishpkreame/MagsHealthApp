import requests
from bs4 import BeautifulSoup
import random
url = "https://raw.githubusercontent.com/Krishpkreame/MagsHealthApp/main/quotes.txt"
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
text = soup.find_all(text=True)
text = text[0].split('\n')

print(random.sample(text, 1)[0])
