import requests
from bs4 import BeautifulSoup
import re
import json

url = 'https://www.mcdonalds.com/ua/uk-ua/eat/fullmenu.html'

response = requests.get(url)

result_product = {}

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    links = soup.find_all('a', {'class': 'cmp-category__item-link'})
    api = 'https://www.mcdonalds.com/dnaapp/itemDetails?country=UA&language=uk&showLiveData=true&item='

    for link in links:

        id_ = link['href']
        http = re.search(r'\d+', id_).group()
        product = api + http
        result = requests.get(product)

        if result.status_code == 200:

            data = json.loads(result.text)

            try:
                name_product = data['item']['item_name']

            except KeyError:
                name_product = ''

            try:
                description = data['item']['description']
            except KeyError:
                description = {}

            try:
                nutrient = data['item']['nutrient_facts']['nutrient']
            except KeyError:
                nutrient = {}

            product_nutrient = {}

            product_nutrient['Загальна інформація'] = description

            for el in nutrient:
                product_nutrient[el['name']] = el['value']

        result_product[name_product] = product_nutrient

    if result_product:
        with open('result_product.json', 'w', encoding='utf-8') as file:
            json.dump(result_product, file, indent=4, ensure_ascii=False)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
