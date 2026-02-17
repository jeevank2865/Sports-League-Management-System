# 🏆 Sports League Management System

## Project Description
The **Sports League Management System** is a web-based application developed using **Django** and **Python** to manage sports leagues efficiently.  
It provides a centralized platform to organize tournaments, manage teams and players, schedule matches, record results, and automatically generate points tables.

The system uses **Django Admin** for secure and structured data management and supports relational databases such as **SQLite** and **MySQL**.  
This project is ideal for **academic projects**, **event organizers**, and **real-world sports league management**.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Database Design](#database-design)
- [Modules](#modules)
- [Results](#results)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

---

## Overview
The Sports League Management System simplifies the end-to-end management of sports tournaments by automating administrative tasks such as match scheduling, result tracking, and leaderboard generation.

The application follows Django’s **MVT (Model–View–Template)** architecture, ensuring scalability, security, and maintainability.

---

## Features
- Tournament creation and management  
- Team registration and management  
- Player management  
- Match scheduling  
- Match result entry  
- Automatic points table generation  
- Secure admin authentication  
- Relational database support  
- Deployment-ready configuration  

---

## System Architecture
The system follows the **Django MVT architecture**:

- **Model** – Defines database schemas and relationships  
- **View** – Handles business logic and request processing  
- **Template** – Renders user interfaces  

---

## Technologies Used
- **Backend:** Python, Django  
- **Database:** SQLite / MySQL  
- **Frontend:** Django Admin, HTML, CSS  
- **Deployment:** PythonAnywhere  
- **Version Control:** Git, GitHub  

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/sports-league-management-system.git
   cd Sports-League-Management-System

2.	Create and activate a virtual environment:
	  ```bash
      python -m venv venv
    source venv/bin/activate   # macOS/Linux
    venv\Scripts\activate      # Windows
3.  Install dependencies:
    ```bash
    pip install -r requirements.txt

4.	Apply database migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    
5.	Create an admin user:
    ```bash
    python manage.py createsuperuser

6.	Run the development server:
    ```bash
    python manage.py runserver

  

