 ## QuickBite Food Delivery API (FastAPI Project)

 # Project Description

QuickBite is a RESTful API built using **FastAPI** that simulates a food delivery system.
It allows users to view menu items, place orders, manage a cart, and perform advanced operations like filtering, searching, sorting, and pagination.

---

## Features

###  Menu Management

* View all menu items
* Get item by ID
* Add new item
* Update item (price/availability)
* Delete item
* Menu summary (available/unavailable/categories)

###  Advanced Menu Features

* Filter menu (category, price, availability)
* Search menu (keyword)
* Sort menu (price/name/category)
* Pagination
* Smart browsing (combined search + sort + pagination)

###  Orders

* Place order
* View all orders
* Search orders by customer name
* Sort orders by total price

###  Cart System

* Add items to cart
* View cart
* Checkout cart (creates orders + grand total)

---

##  Tech Stack

* Python
* FastAPI
* Pydantic
* Uvicorn

---

##  How to Run

1. Install dependencies:

```bash
pip install fastapi uvicorn
```

2. Run the server:

```bash
uvicorn main:app --reload
```

3. Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

##  API Endpoints

###  Basic

* `GET /` → Home

###  Menu

* `GET /menu`
* `GET /menu/{item_id}`
* `POST /menu`
* `PUT /menu/{item_id}`
* `DELETE /menu/{item_id}`
* `GET /menu/summary`

###  Advanced Menu

* `GET /menu/filter`
* `GET /menu/search`
* `GET /menu/sort`
* `GET /menu/page`
* `GET /menu/browse`  (Combined Feature)

###  Orders

* `GET /orders`
* `POST /orders`
* `GET /orders/search`
* `GET /orders/sort`

###  Cart

* `POST /cart/add`
* `GET /cart`
* `POST /cart/checkout`

---

##  Testing

All endpoints were tested using **FastAPI Swagger UI**.
Screenshots of outputs are included as per assignment requirements.

---

##  Learning Outcomes

* Built REST APIs using FastAPI
* Implemented CRUD operations
* Applied filtering, searching, sorting, pagination
* Managed real-world logic (cart & orders)
* Understood API validation using Pydantic

---

##  Author

Mayuri Rathod (CSE - Data Science)

---

##  Conclusion

This project demonstrates a complete backend system for a food delivery application using FastAPI with clean structure and scalable features.
