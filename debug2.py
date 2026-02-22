import requests
from bs4 import BeautifulSoup

def test_url(url):
    print(f"Testing {url}")
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    print(f"Status: {response.status_code}")
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.select('a[href^="/library/"]')
    print(f"Found {len(links)} links")
    if links:
        print(f"First link href: {links[0].get('href')}")
    print("-" * 20)

test_url('https://ollama.com/library?q=mistral')
test_url('https://ollama.com/search?q=mistral')
test_url('https://ollama.com/library')
