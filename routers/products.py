from fastapi import APIRouter, HTTPException
import os
import csv

router = APIRouter(
    prefix="/products",
    tags=["products"]
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(BASE_DIR, "products.csv")

def load_products():
    products = []
    with open(CSV_PATH, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                "id": int(row["Id"]),
                "name": row["Product Name"],
                "description": str(row["Description"])
            })
    return products


# products= [
    # {"id":1, "name":"Guitar", "Price":5000},
    # {"id":2, "name": "Keyboard", "Price": 8000}
# ]

# @router.get("/")
# def get_products():
#     return [
#         {"id":1, "name":"Guitar", "Price":5000},
#         {"id":2, "name": "Keyboard", "Price": 8000}
    

@router.get("/")
def get_products():
    products = load_products()
    return{"products":products}


@router.get("/{product_id}")
def get_product(product_id: int):
        products = load_products()
        for product in products:
            if product["id"] == product_id:
                return {"product": product}
        raise HTTPException(status_code=404, detail={"error": "Product not found"})