# 🛍️ SPlus

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python\&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.x-092E20?logo=django\&logoColor=white)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite\&logoColor=white)
![Vercel](https://img.shields.io/badge/Deployed%20on-Vercel-000000?logo=vercel\&logoColor=white)

**SPlus** is a Django-based e-commerce web application developed as a practical project for building and managing an online store.

The project follows Django's modular architecture and includes separate applications for products, accounts, orders, contact, and the main website.

## 🌐 Live Demo

[View SPlus Live](https://splus-sigma.vercel.app/)

## ✨ Features

* 🛍️ Product catalog
* 📂 Product categories
* 🔎 Product detail pages
* 💰 Product pricing
* 📦 Inventory management
* 👤 User account module
* 🛒 Order module
* 📞 Contact section
* 🔐 Django Admin panel
* 📱 Responsive interface
* 🇮🇷 Persian user interface
* ☁️ Deployment on Vercel
* 🗄️ SQLite database

## 🛠️ Tech Stack

### Backend

* Python
* Django
* SQLite

### Frontend

* HTML5
* CSS3
* JavaScript
* Django Templates

### Deployment

* Vercel

## 📂 Project Structure

```text
splus/
│
├── splus_project/
│   │
│   ├── accounts/
│   ├── contact_module/
│   ├── home/
│   ├── orders/
│   ├── products/
│   ├── splus_project/
│   │
│   └── manage.py
│
├── .gitignore
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Brbodd/splus.git
cd splus/splus_project
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install django
```

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Run the development server

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

## 📦 Products

Products can contain information such as:

* Product name
* Category
* Product code
* Price
* Quantity
* Image
* Slug

Products can be managed through the Django Admin panel.

## 🔮 Future Improvements

Some planned improvements for the project:

* Complete authentication system
* Shopping cart
* Checkout system
* Order management
* Online payment integration
* Product search and filtering
* Wishlist functionality
* Customer dashboard
* PostgreSQL support
* REST API
* Automated testing
* Docker support

## 🎯 Purpose

This project was created to practice and demonstrate Django web development concepts including:

* Django application architecture
* Models and databases
* URL routing
* Views
* Templates
* Static files
* Product management
* Backend and frontend integration
* Web application deployment

## 👨‍💻 Author

**Barbod Zahedi**

GitHub: [@Brbodd](https://github.com/Brbodd)

## ⭐ Support

If you like this project, consider giving the repository a ⭐ on GitHub.
