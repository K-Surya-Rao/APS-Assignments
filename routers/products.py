from fastapi import APIRouter

router = APIRouter(
    prefix="/products",
    tags=["products"]
)


@router.get("/")
def get_products():
    return [
        {"id":1, "name":"Guitar", "Price":5000},
        {"id":2, "name": "Keyboard", "Price": 8000}
    ]