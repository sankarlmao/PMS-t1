# Simple Project Management System (PMS)

A minimal, easy-to-understand web-based Project Management System built with Flask and MySQL.

## Features
- Add and delete projects via a simple web interface
- Data stored in a MySQL database
- Clean, minimal codebase for easy learning and extension

## Requirements
- Python 3.x
- Flask
- mysql-connector-python
- MySQL server

## Setup Instructions

### 1. Install Python dependencies
```
pip install -r requirements.txt
```

### 2. Set up the MySQL database
- Start your MySQL server.
- Log in to MySQL and run:
```
CREATE DATABASE pms_db;
USE pms_db;
CREATE TABLE projects (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);
```
- Update the MySQL credentials in `app.py` if needed.

### 3. Run the application
```
python app.py
```

### 4. Use the application
- Open your browser and go to: http://localhost:5000
- Add new projects or delete existing ones.

## Project Structure
- `app.py` — Main Flask application
- `templates/index.html` — Web interface template
- `requirements.txt` — Python dependencies
- `.env.example` — Example environment variables for DB config

## Customization
- To add more features (like tasks, users, authentication), extend the database and Flask routes as needed.

## License
This project is provided for educational purposes and is open for extension.
