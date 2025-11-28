import re
import requests
from bs4 import BeautifulSoup

def extract_product_info(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.find('span', {'id': 'productTitle'})
    price = soup.find('span', {'class': 'a-price-whole'})

    return {
        'title': title.text.strip() if title else 'Producto desconocido',
        'price': price.text.strip() if price else 'Sin precio'
    }
