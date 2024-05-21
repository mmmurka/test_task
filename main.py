from fastapi import FastAPI
import json
from fastapi.responses import JSONResponse


app = FastAPI()


class CustomJSONResponse(JSONResponse):
    async def render(self, content: any) -> bytes:
        return json.dumps(
            content,
            ensure_ascii=False,
            indent=4,
            separators=(',', ': ')
        ).encode('utf-8')


@app.get("/all_products")
async def all_prods():
    with open('result_product.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


@app.get('/products/{product_name}')
async def prod(name_product):
    with open('result_product.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data[name_product]


@app.get('/products/{product_name}/{product_field')
async def prod_value(name_product, product_nutrient):
    with open('result_product.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data[name_product][product_nutrient]
