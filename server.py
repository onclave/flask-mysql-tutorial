from flask import Flask, redirect, url_for, request, render_template
from flaskext.mysql import MySQL

app = Flask(__name__, template_folder = 'template')
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'sajib6667'
app.config['MYSQL_DATABASE_DB'] = 'tutorial'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
app.config['MYSQL_DATABASE_PORT'] = 3307

mysql.init_app(app)
connection = mysql.connect()

@app.route('/')
def serve_index():
    return 'serve index'

@app.route('/home')
def serve_home():
    return 'serve home'

@app.route('/user/<name>')
def serve_profile(name):
    return render_template('hello.html', name = name)

@app.route('/post/<int:post_id>/')
def serve_post(post_id):
    return 'This is post ' + str(post_id)

@app.route('/posts/<int:post_id>/')
def serve_post_redirect(post_id):
    return redirect(url_for('serve_post', post_id = post_id))

@app.route('/login/')
def serve_login():
    return render_template('/login.html')

@app.route('/home/')
def serve_home_template():
    return render_template('/home.html')

@app.route('/login/success/')
def serve_login_success():
    return 'login success'

@app.route('/login/failure/')
def serve_login_failure():
    return 'login failure'

@app.route('/login/auth/', methods = ['POST', 'GET'])
def auth_login():
    
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        if username == 'sajib' and password == 'password':
            return redirect(url_for('serve_login_success'))
        else:
            return redirect(url_for('serve_login_failure'))

@app.route('/certificate/<name>/<int:marks>/', methods = ['GET'])
def serve_certificate(name, marks):
    return render_template('certificate.html', name = name, marks = marks)

@app.route('/routine')
def serve_routine():
    routine = { 'Physics': '10:00 am', 'Computer': '11:30 am', 'English': '2:30 pm' }
    return render_template('routine.html', routine = routine)

@app.route('/insert')
def insert_db():

    cursor = get_cursor()

    cursor.execute("insert into ex1(col1, col2) values (%s, %s)", (26, "xyz"))
    connection.commit()
    cursor.close()

    return "success"

@app.route('/select')
def select_db():

    cursor = get_cursor()

    cursor.execute("select * from ex1")
    data = cursor.fetchall()
    cursor.close()

    return render_template('db_select.html', data = data)

def get_cursor():
    global connection
    return connection.cursor()

if __name__ == '__main__':
    app.run(port = 8080, debug = True)