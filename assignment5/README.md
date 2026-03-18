#  FastAPI E-commerce API — Assignment 5 (Day 6)

##  Overview

This project is built using **FastAPI** and demonstrates three essential API features used in real-world applications:

*  Search
*  Sorting
*  Pagination

Additionally, advanced endpoints combine all these features into a single API.

---

## ⚙️ Tech Stack

* Python
* FastAPI
* Uvicorn
* Pydantic

---

##  How to Run the Project

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

##  Available Endpoints

###  Search

* `GET /products/search?keyword=...`
  Search products by name (case-insensitive)

* `GET /orders/search?customer_name=...`
  Search orders by customer name

---

###  Sorting

* `GET /products/sort?sort_by=price&order=asc`
  Sort products by:
* price (asc/desc)
* name (asc/desc)

---

###  Pagination

* `GET /products/page?page=1&limit=2`
  Paginate products list

* `GET /orders/page?page=1&limit=3`  (Bonus)
  Paginate orders list

---

###  Advanced Features

####  Sort by Category

* `GET /products/sort-by-category`
  Sorts products by:

1. Category (A → Z)
2. Price within category (low → high)

---

####  Combined API (Search + Sort + Pagination)

* `GET /products/browse`

Supports:

* keyword (search)
* sort_by (price/name)
* order (asc/desc)
* page
* limit

---

##  Example Test Cases

### Search

* `?keyword=mouse` → 1 result
* `?keyword=MOUSE` → same result (case-insensitive)
* `?keyword=laptop` → No products found

---

### Sort

* Price Asc → Pen Set (₹49)
* Price Desc → USB Hub (₹799)
* Name Asc → Notebook → Pen Set → USB Hub → Wireless Mouse

---

### Pagination

* Page 1 → First 2 products
* Page 2 → Next 2 products
* Page 3 → Empty list

---

##  Key Concepts Learned

* Query parameters in FastAPI
* Data filtering using list comprehension
* Sorting using `sorted()` with lambda
* Pagination logic using slicing
* Combining multiple operations in one API

---

##  Important Notes

* Orders are stored in memory → reset on server restart
* Must create orders using `POST /orders` before testing search or pagination on orders

---

##  Conclusion

This assignment demonstrates how real-world APIs handle large datasets efficiently using search, sorting, and pagination. The combined endpoint simulates how modern e-commerce platforms work.

---

## ✨ Author

Mayuri Rathod
