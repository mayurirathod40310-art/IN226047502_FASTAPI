# FastAPI Assignment 4 – Shopping Cart System

## Overview

This assignment implements a **simple E-commerce Shopping Cart API** using FastAPI.
It allows users to view products, add items to a cart, update quantities, remove items, and complete checkout.

## Features

* View available products
* Add products to cart
* Update product quantity in cart
* Remove product from cart
* View cart summary and grand total
* Checkout cart and convert items into orders
* Error handling (invalid product, out-of-stock product, empty cart checkout)

## Technologies Used

* Python
* FastAPI
* Uvicorn
* Swagger UI (for API testing)

## API Endpoints

### Products

* `GET /products` → View all products
* `GET /products/{product_id}` → Get product by ID
* `POST /products` → Add new product
* `PUT /products/{product_id}` → Update product
* `DELETE /products/{product_id}` → Delete product
* `GET /products/filter` → Filter products
* `GET /products/compare` → Compare two products

### Orders

* `POST /orders` → Place an order
* `GET /orders` → View all orders

### Cart System

* `POST /cart/add` → Add product to cart
* `GET /cart` → View cart items
* `DELETE /cart/{product_id}` → Remove item from cart
* `POST /cart/checkout` → Checkout cart and create orders

## Error Handling

The API handles common errors such as:

* Product not found
* Product out of stock
* Invalid quantity
* Checkout with empty cart

Example error response:

{
"error": "Cart is empty — add items first"
}

## Screenshots

Screenshots of API requests and responses are included in this folder as proof of successful execution.

## Author

Mayuri Rathod
Computer Science & Engineering (Data Science)
