from flask import Flask, redirect, render_template, request, url_for
from flask_mysqldb import MySQL

# init main app
app = Flask(__name__)
# datebase config
app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'meet11'

# init mysql
mysql = MySQL(app)

@app.route('/form')
def form():
    return render_template('signup.html')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'GET':
        return "Login via the login Form"
    
    elif request.method == 'POST':
        name = request.form['name']
        address = request.form['Address']
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO data1 VALUES (%s, %s)', (name, address))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('home'))

@app.route('/home')
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM data1")
    data= cur.fetchall()
    cur.close()
    return render_template('home.html', data1=data)
    
app.run(host='localhost', port=50000)