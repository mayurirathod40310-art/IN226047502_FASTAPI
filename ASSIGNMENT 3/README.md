# FastAPI E-Commerce API – Assignment 3

## Overview

This project is a simple **E-Commerce API built using FastAPI**.
It demonstrates REST API development including product management, filtering, comparison, auditing, and order placement.

The API simulates a small online store where users can view products, apply discounts, place orders, and manage product data.

---

## Technologies Used

* Python
* FastAPI
* Pydantic
* Uvicorn

---

## Features

### Product Management

* View all products
* Add new products
* Update product details
* Delete products
* Get a single product by ID

### Product Operations

* Filter products by category, price range, and stock status
* Compare two products by price
* Apply category-based discounts

### Product Audit

Provides insights such as:

* Total products
* Number of products in stock
* Out-of-stock product names
* Total stock value
* Most expensive product

### Order System

* Place orders for products
* View all placed orders

---

## API Endpoints

### Basic Routes

* `GET /` – Welcome message
* `GET /products` – Get all products

### Product Operations

* `GET /products/filter`
* `GET /products/compare`
* `POST /products`
* `PUT /products/{product_id}`
* `DELETE /products/{product_id}`
* `GET /products/{product_id}`

### Analysis

* `GET /products/audit`

### Bonus Feature

* `PUT /products/discount` – Apply discount to products by category

### Orders

* `POST /orders` – Place an order
* `GET /orders` – View all orders

---

## How to Run the Project

1. Install dependencies

```
pip install fastapi uvicorn
```

2. Run the server

```
uvicorn main:app --reload
```

3. Open API documentation

```
http://127.0.0.1:8000/docs
```

---

## Author

Mayuri Rathod
Computer Science & Engineering (Data Science)
