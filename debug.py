import requests
from bs4 import BeautifulSoup

url = 'https://ollama.com/library'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(response.text, 'html.parser')

links = soup.select('a[href^="/library/"]')
for i, link in enumerate(links[:5]):
    # Name from href or h2
    href = link.get('href', '')
    name = href.replace('/library/', '')
    
    # Description
    p = link.find('p', class_=lambda c: c and 'max-w' in c)
    if not p:
        p = link.find('p')
    desc = p.text.strip() if p else "No desc"
    
    print(f"Name: {name}")
    print(f"Desc: {desc}")
    print("---")
