# Sixth_Lab
My sixth lab on python

Завдання
=========================================================================================================================================
1. Реалізувати REST-сервіс (операції GET/POST/PUT/DELETE) для одного з класу з лабораторної роботи 3 з використанням засобів мови Python:
Flask
Python 3.x
2. Реалізувати збереження об'єкту класу з лабораторної роботи 3 в базі даних з використанням наступного технологічного стеку 
SQLAlchemy-1.1.15
MySQL-5.7 / MySQL-8.0 (в залежності від того, яку базу даних було обрано в 8-й роботі)

To launch:
=========================================================================================================================================
1. Enter "git clone https://github.com/whoaam1/Sixth_Lab" in console
2. Create virtual environment being in folder of that project
3. Activate virtual environment 
4. Install flask_sqlalchemy, flask_marshmallow, marshmallow-sqlalchemy
5. Being in folder of that project create database: write in terminal "python" then ">>> from car_service import db >>> db.create_all()"
6. Run flask app
7. Go to the instrument of API testing, open "http://localhost:5000/cars" and test methods GET/POST/PUT/DELETE
