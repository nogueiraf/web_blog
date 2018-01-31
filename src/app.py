from src.common.database import Database
from src.models.user import User
from src.models.ssh import Ssh


from flask import Flask, render_template, request, session, make_response

app = Flask(__name__)  # '__main__'
app.secret_key = "jose"


@app.route('/')
def home_template():
    return render_template('login.html')


@app.route('/login')
def login_template():
    return render_template('login.html')


@app.route('/register')
def register_template():
    return render_template('register.html')


@app.before_first_request
def initialize_database():
    Database.initialize()


@app.route('/auth/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']

    if User.login_valid(email, password):
        User.login(email)
    else:
        session['email'] = None

    return render_template("profile.html", email=session['email'])


@app.route('/auth/register', methods=['POST'])
def register_user():
    email = request.form['email']
    password = request.form['password']

    User.register(email, password)

    return render_template("profile.html", email=session['email'])


@app.route('/ftp')
def ftp_template():
    return render_template("folder.html")


@app.route('/auth/folder', methods=["POST"])
def folders():
    connection = Ssh("179.124.44.5", "root", "D!5c0v3ry")

    mode = request.form['mode']
    start = request.form['start']
    end = request.form['end']

    if mode == 'canais':
        connection.canais(start)
        return render_template("response.html")
    elif mode == 'venda':
        connection.venda(start, end)
        return render_template("response.html")
    else:
        return "invalid"


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5995, debug=True)
