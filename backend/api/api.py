from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
import json

router = APIRouter()


@router.get("/all_products", response_class=JSONResponse)
async def all_prods():
    with open('backend/result_product.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    return JSONResponse(content=data, media_type="application/json", headers={
        "Content-Type": "application/json; charset=utf-8"}, status_code=200)


@router.get('/products/{product_name}', response_class=JSONResponse)
async def prod(product_name: str):

    with open('backend/result_product.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    product = data.get(product_name)

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return JSONResponse(content=product, media_type="application/json", headers={
        "Content-Type": "application/json; charset=utf-8"}, status_code=200)


@router.get('/products/{product_name}/{product_field}', response_class=JSONResponse)
async def prod_value(product_name: str, product_field: str):

    with open('backend/result_product.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    product = data.get(product_name)

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    field_value = product.get(product_field)

    if field_value is None:
        raise HTTPException(status_code=404, detail="Field not found")

    return JSONResponse(content={product_field: field_value}, media_type="application/json", headers={
        "Content-Type": "application/json; charset=utf-8"}, status_code=200)


