# FastAPI Product API

A simple REST API built using **FastAPI** as part of an internship assignment.
This project demonstrates how to create API endpoints to retrieve and filter product data.

## Project Overview

The API provides multiple endpoints to access product information such as viewing all products, filtering by category, checking in-stock items, searching products, and viewing store statistics.

## Repository Structure

ASSIGNMENT 1/

* main.py – FastAPI application with all API endpoints
* Q1_Output.png – Output screenshot for Question 1
* Q2_Output.png – Output screenshot for Question 2
* Q3_Output.png – Output screenshot for Question 3
* Q4_Output.png – Output screenshot for Question 4
* Q5_Output.png – Output screenshot for Question 5
* Bonus_Output.png – Output screenshot for the bonus task

## How to Run the Project

1. Install dependencies

```
pip install fastapi uvicorn
```

2. Start the server

```
python -m uvicorn main:app --reload
```

3. Open API documentation

```
http://127.0.0.1:8000/docs
```

## API Endpoints

* `/` – Home
* `/products` – Get all products
* `/products/category/{category_name}` – Filter by category
* `/products/instock` – View in-stock products
* `/products/search/{keyword}` – Search products
* `/products/deals` – Special deals
* `/store/summary` – Store summary

## Tech Stack

* Python
* FastAPI
* Uvicorn
