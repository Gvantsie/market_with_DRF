# Marketplace with Django REST Framework
## Overview

This project is a RESTful API built with Django REST Framework for managing products in an online marketplace. 
It provides endpoints for listing products, retrieving product details, creating new products, updating existing
products, and deleting products. The API supports pagination to efficiently handle large datasets and includes optional
authentication and authorization mechanisms for securing endpoints.

## What is REST?

REST (Representational State Transfer) is an architectural style for designing networked applications. It defines a set 
of constraints and principles for creating scalable and maintainable web services. RESTful APIs (or REST APIs) adhere 
to these principles and allow clients to interact with server resources using 
standard HTTP methods (GET, POST, PUT, DELETE).

## Key Features

- **CRUD Operations**: Create, Read, Update, and Delete operations for products.
- **API Endpoints**: Provides endpoints for listing products, retrieving product details, creating new products, 
- updating existing products, and deleting products.
- **Serialization**: Serializes data between Python objects and JSON for communication with clients.
- **Pagination**: Supports pagination to efficiently handle large datasets.
- **Authentication**: Optionally includes authentication and authorization mechanisms for securing endpoints.

## Installation and Usage

1. Clone the repository:

   ```bash
   https://github.com/Gvantsie/market_with_DRF.git
   ```
2. Create a virtual environment:

   ```bash
   python -m venv env
   ```
3. Activate the virtual environment:

   ```bash
   source env/bin/activate
   ```
4. Install the dependencies:

   ```bash
    pip install -r requirements.txt
    ```
5. Apply the database migrations:

   ```bash
   python manage.py migrate
   ```
6. Create a superuser:

   ```bash
    python manage.py createsuperuser
    ```
7. Run the development server:
    
   ```bash
   python manage.py runserver
   ```
8. Open the API in your browser:

   ```
    http://localhost:8000/
    ```
   
9. Access the admin interface:

   ```
    http://localhost:8000/admin/
    ```
   
## API Endpoints

The API provides the following endpoints for managing products:

- `/products/`: List all products.
- `/products/<id>/`: Retrieve a product by ID.
- `/products/create/`: Create a new product.
- `/products/update/<id>/`: Update an existing product by ID.
- `/products/delete/<id>/`: Delete a product by ID.
- `/products/search/<id>`: Search for products by ID.

## Conclusion

This project demonstrates how to build a RESTful API with Django REST Framework for managing products 
in an online marketplace.

>>Gvantsa