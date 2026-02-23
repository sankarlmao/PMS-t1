# Simple PMS (Project Management System)

## Features
- Minimal web interface for project management
- Add and delete projects
- Uses MySQL as backend database

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set up MySQL database:
   ```sql
   CREATE DATABASE pms_db;
   USE pms_db;
   CREATE TABLE projects (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(255) NOT NULL
   );
   ```
3. Update `app.py` with your MySQL password.
4. Run the app:
   ```bash
   python app.py
   ```

## Usage
- Open `http://localhost:5000` in your browser.
- Add or delete projects.
