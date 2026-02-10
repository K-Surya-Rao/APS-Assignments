from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/products",
    tags=["products"]
)

products= [
    {"id":1, "name":"Guitar", "Price":5000},
    {"id":2, "name": "Keyboard", "Price": 8000}
]

# @router.get("/")
# def get_products():
#     return [
#         {"id":1, "name":"Guitar", "Price":5000},
#         {"id":2, "name": "Keyboard", "Price": 8000}
    

@router.get("/")
def get_products():
    return{"products":products}

@router.get("/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return {"product": product}