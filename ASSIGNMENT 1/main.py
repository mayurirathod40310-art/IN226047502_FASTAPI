from fastapi import FastAPI

app = FastAPI()

# Product List
products = [
    {"id": 1, "name": "Wireless Mouse", "price": 599, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Notebook", "price": 49, "category": "Stationery", "in_stock": True},
    {"id": 3, "name": "Pen Set", "price": 99, "category": "Stationery", "in_stock": False},
    {"id": 4, "name": "USB Cable", "price": 199, "category": "Electronics", "in_stock": True},

    # Q1 Added Products
    {"id": 5, "name": "Laptop Stand", "price": 899, "category": "Electronics", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 2499, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 1499, "category": "Electronics", "in_stock": False},
]


# Home
@app.get("/")
def home():
    return {"message": "FastAPI is working"}


# Q1 Products list
@app.get("/products")
def get_products():
    return {
        "products": products,
        "total": len(products)
    }


# Q2 Category filter
@app.get("/products/category/{category_name}")
def get_products_by_category(category_name: str):

    filtered = [
        product for product in products
        if product["category"].lower() == category_name.lower()
    ]

    if not filtered:
        return {"error": "No products found in this category"}

    return {"products": filtered}


# Q3 In-stock products
@app.get("/products/instock")
def get_instock_products():

    instock = [
        product for product in products
        if product["in_stock"] == True
    ]

    return {
        "in_stock_products": instock,
        "count": len(instock)
    }


# Q4 Store summary
@app.get("/store/summary")
def store_summary():

    total_products = len(products)

    instock = len([p for p in products if p["in_stock"]])
    outstock = total_products - instock

    categories = list(set([p["category"] for p in products]))

    return {
        "store_name": "My E-commerce Store",
        "total_products": total_products,
        "in_stock": instock,
        "out_of_stock": outstock,
        "categories": categories
    }


# Q5 Search products
@app.get("/products/search/{keyword}")
def search_products(keyword: str):

    result = [
        product for product in products
        if keyword.lower() in product["name"].lower()
    ]

    if not result:
        return {"message": "No products matched your search"}

    return {
        "matched_products": result,
        "count": len(result)
    }


# ⭐ Bonus
@app.get("/products/deals")
def product_deals():

    cheapest = min(products, key=lambda x: x["price"])
    expensive = max(products, key=lambda x: x["price"])

    return {
        "best_deal": cheapest,
        "premium_pick": expensive
    }
