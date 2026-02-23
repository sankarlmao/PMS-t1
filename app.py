from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Configure MySQL connection
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='your_mysql_password',
    database='pms_db'
)
cursor = conn.cursor()

@app.route('/')
def index():
    cursor.execute('SELECT * FROM projects')
    projects = cursor.fetchall()
    return render_template('index.html', projects=projects)

@app.route('/add', methods=['POST'])
def add_project():
    name = request.form['name']
    cursor.execute('INSERT INTO projects (name) VALUES (%s)', (name,))
    conn.commit()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete_project(id):
    cursor.execute('DELETE FROM projects WHERE id=%s', (id,))
    conn.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
