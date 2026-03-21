from fastapi import FastAPI, Response
from pydantic import BaseModel, Field

app = FastAPI()

# ------------------ DATA ------------------
menu = [
    {"id": 1, "name": "Margherita Pizza", "price": 250, "category": "Pizza", "is_available": True},
    {"id": 2, "name": "Veg Burger", "price": 120, "category": "Burger", "is_available": True},
    {"id": 3, "name": "Cold Coffee", "price": 90, "category": "Drink", "is_available": True},
    {"id": 4, "name": "Chocolate Cake", "price": 180, "category": "Dessert", "is_available": False},
    {"id": 5, "name": "Cheese Pizza", "price": 300, "category": "Pizza", "is_available": True},
    {"id": 6, "name": "French Fries", "price": 100, "category": "Burger", "is_available": True}
]

orders = []
order_counter = 1
cart = []

# ------------------ MODELS ------------------
class OrderRequest(BaseModel):
    customer_name: str = Field(..., min_length=2)
    item_id: int = Field(..., gt=0)
    quantity: int = Field(..., gt=0, le=20)
    delivery_address: str = Field(..., min_length=10)
    order_type: str = "delivery"

class NewMenuItem(BaseModel):
    name: str = Field(..., min_length=2)
    price: int = Field(..., gt=0)
    category: str = Field(..., min_length=2)
    is_available: bool = True

class CartItem(BaseModel):
    item_id: int = Field(..., gt=0)
    quantity: int = Field(..., gt=0, le=20)

# ------------------ HELPERS ------------------
def find_menu_item(item_id: int):
    return next((item for item in menu if item["id"] == item_id), None)

def calculate_bill(price: int, quantity: int, order_type: str):
    total = price * quantity
    if order_type == "delivery":
        total += 30
    return total

def filter_menu_logic(category=None, max_price=None, is_available=None):
    return [
        item for item in menu
        if (category is None or item["category"].lower() == category.lower()) and
           (max_price is None or item["price"] <= max_price) and
           (is_available is None or item["is_available"] == is_available)
    ]

def find_cart_item(item_id: int):
    return next((c for c in cart if c["item_id"] == item_id), None)

def search_menu(keyword: str):
    keyword = keyword.lower()
    return [
        item for item in menu
        if keyword in item["name"].lower() or keyword in item["category"].lower()
    ]

# ------------------ HOME ------------------
@app.get("/")
def home():
    return {"message": "Welcome to QuickBite Food Delivery"}

# ------------------ MENU APIs ------------------
@app.get("/menu")
def get_menu():
    return {"total_items": len(menu), "menu": menu}

@app.get("/menu/summary")
def summary():
    return {
        "total_items": len(menu),
        "available_items": sum(1 for i in menu if i["is_available"]),
        "unavailable_items": sum(1 for i in menu if not i["is_available"]),
        "categories": list(set(i["category"] for i in menu))
    }

@app.get("/menu/filter")
def filter_menu(category: str = None, max_price: int = None, is_available: bool = None):
    result = filter_menu_logic(category, max_price, is_available)
    return {"total_items": len(result), "menu": result}

@app.get("/menu/search")
def menu_search(keyword: str):
    result = search_menu(keyword)
    if not result:
        return {"message": f"No items found for '{keyword}'"}
    return {"total_found": len(result), "menu": result}

@app.get("/menu/sort")
def sort_menu(sort_by: str = "price", order: str = "asc"):
    if sort_by not in ["price", "name", "category"]:
        return {"error": "Invalid sort_by"}
    if order not in ["asc", "desc"]:
        return {"error": "Invalid order"}

    return {
        "menu": sorted(menu, key=lambda x: x[sort_by], reverse=(order == "desc"))
    }

@app.get("/menu/page")
def paginate(page: int = 1, limit: int = 3):
    if page < 1 or limit < 1 or limit > 10:
        return {"error": "Invalid page or limit"}

    start = (page - 1) * limit
    return {
        "page": page,
        "limit": limit,
        "total_items": len(menu),
        "total_pages": (len(menu) + limit - 1) // limit,
        "menu": menu[start:start+limit]
    }

# ✅ Q20 SMART BROWSE
@app.get("/menu/browse")
def browse_menu(
    keyword: str = None,
    sort_by: str = "price",
    order: str = "asc",
    page: int = 1,
    limit: int = 4
):
    data = menu

    # FILTER
    if keyword:
        keyword_lower = keyword.lower()
        data = [
            item for item in data
            if keyword_lower in item["name"].lower()
            or keyword_lower in item["category"].lower()
        ]

    # SORT
    if sort_by not in ["price", "name", "category"]:
        return {"error": "Invalid sort_by"}
    if order not in ["asc", "desc"]:
        return {"error": "Invalid order"}

    data = sorted(data, key=lambda x: x[sort_by], reverse=(order == "desc"))

    # PAGINATION
    if page < 1 or limit < 1 or limit > 10:
        return {"error": "Invalid page or limit"}

    total_items = len(data)
    total_pages = (total_items + limit - 1) // limit

    start = (page - 1) * limit

    return {
        "page": page,
        "limit": limit,
        "total_items": total_items,
        "total_pages": total_pages,
        "menu": data[start:start+limit]
    }

# ------------------ MENU CRUD ------------------
@app.post("/menu")
def add_item(item: NewMenuItem, response: Response):
    for i in menu:
        if i["name"].strip().lower() == item.name.strip().lower():
            return {"error": "Item already exists"}

    new_item = {
        "id": max(i["id"] for i in menu) + 1,
        "name": item.name.strip(),
        "price": item.price,
        "category": item.category,
        "is_available": item.is_available
    }
    menu.append(new_item)
    response.status_code = 201
    return new_item

@app.put("/menu/{item_id}")
def update(item_id: int, price: int = None, is_available: bool = None):
    item = find_menu_item(item_id)
    if not item:
        return {"error": "Item not found"}
    if price is not None:
        item["price"] = price
    if is_available is not None:
        item["is_available"] = is_available
    return item

@app.delete("/menu/{item_id}")
def delete(item_id: int):
    item = find_menu_item(item_id)
    if not item:
        return {"error": "Item not found"}
    menu.remove(item)
    return {"message": "Deleted", "item": item["name"]}

# ❗ ALWAYS LAST
@app.get("/menu/{item_id}")
def get_item(item_id: int):
    item = find_menu_item(item_id)
    return item if item else {"error": "Item not found"}

# ------------------ ORDERS ------------------
@app.get("/orders")
def get_orders():
    return {"total_orders": len(orders), "orders": orders}

@app.get("/orders/search")
def search_orders(customer_name: str):
    result = [o for o in orders if customer_name.lower() in o["customer_name"].lower()]
    if not result:
        return {"message": f"No orders found for '{customer_name}'"}
    return {"total_found": len(result), "orders": result}

@app.get("/orders/sort")
def sort_orders(order: str = "asc"):
    if order not in ["asc", "desc"]:
        return {"error": "Invalid order"}
    return {
        "orders": sorted(orders, key=lambda x: x["total_price"], reverse=(order == "desc"))
    }

@app.post("/orders")
def place_order(order: OrderRequest):
    global order_counter
    item = find_menu_item(order.item_id)
    if not item:
        return {"error": "Item not found"}
    if not item["is_available"]:
        return {"error": "Unavailable"}

    new_order = {
        "order_id": order_counter,
        "customer_name": order.customer_name,
        "item_name": item["name"],
        "quantity": order.quantity,
        "total_price": calculate_bill(item["price"], order.quantity, order.order_type),
        "order_type": order.order_type,
        "delivery_address": order.delivery_address
    }

    orders.append(new_order)
    order_counter += 1
    return new_order

# ------------------ CART ------------------
@app.post("/cart/add")
def add_cart(c: CartItem):
    item = find_menu_item(c.item_id)
    if not item or not item["is_available"]:
        return {"error": "Invalid item"}

    existing = find_cart_item(c.item_id)
    if existing:
        existing["quantity"] += c.quantity
    else:
        cart.append({"item_id": c.item_id, "quantity": c.quantity})

    return find_cart_item(c.item_id)

@app.get("/cart")
def view_cart():
    total = 0
    items = []
    for c in cart:
        item = find_menu_item(c["item_id"])
        if item:
            price = item["price"] * c["quantity"]
            total += price
            items.append({
                "item_name": item["name"],
                "quantity": c["quantity"],
                "total_price": price
            })
    return {"cart_items": items, "grand_total": total}

@app.post("/cart/checkout")
def checkout(customer_name: str, delivery_address: str):
    global order_counter
    if not cart:
        return {"error": "Cart empty"}

    placed = []
    total = 0

    for c in cart:
        item = find_menu_item(c["item_id"])
        price = calculate_bill(item["price"], c["quantity"], "delivery")
        total += price

        order = {
            "order_id": order_counter,
            "customer_name": customer_name,
            "item_name": item["name"],
            "quantity": c["quantity"],
            "total_price": price,
            "order_type": "delivery",
            "delivery_address": delivery_address
        }

        orders.append(order)
        placed.append(order)
        order_counter += 1

    cart.clear()
    return {"placed_orders": placed, "grand_total": total}
