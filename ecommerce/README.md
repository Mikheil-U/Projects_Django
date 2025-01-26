# Django E-Commerce Website

## Overview

This is a feature-rich e-commerce website built using Django. The platform allows users to browse products, add them to a shopping cart, and complete purchases. It also supports user registration, authentication, email verification, and order tracking. The admin panel is used for managing products, categories, and orders. The website is designed to ensure an efficient and secure shopping experience.

![image](https://github.com/user-attachments/assets/dee5f208-d52b-40eb-8c82-3293a172eca3)



## Features

### General Features
- **User Registration & Authentication**: Users can register, log in, and log out. New accounts require email verification for activation.
- **Product Browsing**: Users can browse products by category or view detailed information about a specific product.
- **Shopping Cart**: Add, update, and delete items from the shopping cart using AJAX for a seamless user experience.
- **Order Management**: Users can place orders, manage shipping addresses, and track order statuses.
- **Payment**: Integration of a checkout process and payment success/failure handling.
- **Admin Panel**: Admins can manage products, categories, users, and orders.

### Authentication Features
- Email verification system using Django's token generator.
- Profile management and account deletion functionalities.
- Dashboard for authenticated users.

### Payment and Shipping
- Authenticated users can save shipping addresses for faster checkout.
- Guest users can complete orders without creating an account.
- Orders and their items are logged for easy tracking.

## Installation

1. Clone the repository:
```
   git clone https://github.com/Mikheil-U/Projects_Django.git
   cd ecommerce
```
2. Create a virtual environment and install dependencies:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
3. Apply Migrations: 
```
python manage.py makemigrations
python manage.py migrate
```
4. Run the development server:
```
python manage.py runserver
```
5. Open the website in your browser at http://127.0.0.1:8000.

## File Structure
### Key Directories
* ecommerce/account/: Handles user authentication, registration, profile management, and email verification.
* ecommerce/payment/: Manages the checkout process, order creation, and payment status handling.
* ecommerce/shopping_cart/: Manages the shopping cart operations, including adding, updating, and deleting items.
* ecommerce/store/: Handles product browsing, category filtering, and displaying product details.

![image](https://github.com/user-attachments/assets/5dbde05c-9759-4811-882f-eecadb75ace2)
![image](https://github.com/user-attachments/assets/9a55e3d9-2fcc-49bb-95fb-934d60688c0d)
![image](https://github.com/user-attachments/assets/88d19629-fd7f-4570-bac3-74eb6b9a666d)
![image](https://github.com/user-attachments/assets/280cff38-a251-4719-a8e8-f8543769c83c)





















