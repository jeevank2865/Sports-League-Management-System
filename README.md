# 🏆 Sports League Management System

## Project Description
The **Sports League Management System** is a role-based web application developed using **Django** and **Python** to manage sports leagues and tournaments efficiently.

The system provides **multiple user panels**—Guest, Captain, Referee, and Admin—each with specific permissions and responsibilities. It enables seamless management of tournaments, teams, players, matches, and points tables through a secure and structured platform.

This project is suitable for **college projects**, **placements**, and **real-world sports event management systems**.

---

## Table of Contents
- [Overview](#overview)
- [User Roles & Panels](#user-roles--panels)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Database Design](#database-design)
- [Modules](#modules)
- [Results](#results)
- [Future Enhancements](#future-enhancements)

---

## Overview
The Sports League Management System automates the process of organizing and managing sports leagues.  
It follows **Django’s MVT architecture**, ensuring scalability, maintainability, and secure role-based access.

The system supports:
- Multiple user roles
- Match scheduling and result tracking
- Automatic points table calculation
- Centralized league administration

---

## User Roles & Panels

### 👤 Guest Panel
- View tournaments and leagues
- View teams and match schedules
- View points tables and standings
- Read-only access (no modifications)

### 🧢 Captain Panel
- View assigned team details
- View match schedules
- View team players
- Track team performance and standings

### 🧑‍⚖️ Referee Panel
- View assigned matches
- Update match results
- Enter scores and outcomes
- Ensure fair and accurate result management

### 🔐 Admin Panel
- Create and manage tournaments
- Add and manage teams and players
- Assign captains and referees
- Schedule matches
- Approve and update results
- Manage users and permissions
- View and control all system data

---

## Features
- Role-based authentication and authorization
- Tournament and league management
- Team and player registration
- Match scheduling
- Result entry and validation
- Automatic points table generation
- Secure admin dashboard
- Relational database support
- Deployment-ready configuration

---

## System Architecture
The system follows **Django MVT (Model–View–Template)** architecture:

- **Model** – Defines database structure and relationships
- **View** – Handles business logic and role-based access
- **Template** – Renders user interfaces for different panels

---

## Technologies Used
- **Backend:** Python, Django  
- **Frontend:** HTML, CSS, Django Templates  
- **Database:** SQLite / MySQL  
- **Authentication:** Django Auth  
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

## Database Design
The system uses a relational database with the following entities:
	•	Users
	•	Roles
	•	Sports
	•	Tournaments
	•	Teams
	•	Players
	•	Matches
	•	Points Table

Foreign key relationships ensure data consistency and integrity.

## Modules
•	User Authentication & Role Management
	•	Tournament Management
	•	Team Management
	•	Player Management
	•	Match Scheduling
	•	Result Management
	•	Points Table Calculation
## Results
The Sports League Management System successfully provides:
	•	Secure multi-role access
	•	Accurate match and result tracking
	•	Automatic standings generation
	•	Scalable and maintainable architecture

## Future Enhancements
•	Live score updates
	•	Public API integration
	•	Player statistics and analytics
	•	Notification system
	•	Mobile application support

