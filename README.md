# Multi-Vendor Inventory Management System

## 📌 Overview
This project is a Django-based system that integrates multiple vendor data sources and maintains a centralized inventory system.

---

## 🎯 Features
- Fetch data from 3 vendor APIs (simulated)
- Normalize different data formats into a common structure
- Store and manage inventory in a centralized database
- REST APIs for syncing and viewing data
- Search and filter products
- Low stock alert system
- Dashboard with inventory statistics

---

## 🧩 Vendor Data Formats

### Vendor A
- id, title, price, inventory

### Vendor B
- product_id, name, cost, stock

### Vendor C
- sku, product_name, price, qty

---

## 🔄 Data Normalization
All vendor data is converted into:
- product_id
- vendor_name
- product_name
- price
- stock

---

## 🗄️ Database Design
- Vendor
- Product
- Inventory (links Vendor & Product)

---

## 🚀 APIs

### Sync Data

GET /api/sync/


### Get Products

GET /api/products/


### Search Products

GET /api/products/?name=laptop


### Filter by Vendor

GET /api/products/vendor/Vendor A/


### Add Inventory

POST /api/add/


---

## 🛠️ Tech Stack
- Python
- Django
- Django REST Framework
- MySQL

---

## ⚙️ Setup Instructions

1. Clone repository:

git clone https://github.com/hemanthkr28/multi-vendor-inventory-system.git


2. Install dependencies:

pip install -r requirements.txt


3. Configure database in settings.py

4. Run migrations:

python manage.py makemigrations
python manage.py migrate


5. Run server:

python manage.py runserver


---

## 📊 Dashboard Features
- Total Products
- Total Vendors
- Total Stock
- Low Stock Alerts

---

## 📸 Screenshots
https://drive.google.com/file/d/1E-YVrsRMN0wIMgm4-Qo79z7H6hMGgiDH/view?usp=sharing

---

## 🧠 Author
Hemanth K R
