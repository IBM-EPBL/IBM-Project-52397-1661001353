from flask import*
import ibm_db
import re

app=Flask(__name__)

app.secret_key = 'a'

conn=ibm_db.connect("DATABASE=bludb;=;PORT=32536;SECURIHOSTNAMETY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=nbc49111;PWD=NfHOkug6Kyn7Fgjj",'','')

@app.route('/')
def homer():
    return render_template('login.html')

@app.route('/backlogin')
def backlogin():
    return render_template('login.html')

@app.route('/login',methods =['GET', 'POST'])
def login():
    global userid
    msg = ''

    if request.method == 'POST' :
        username = request.form['username']
        password = request.form['password']
        sql = "SELECT * FROM login WHERE username =? AND password=?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt,1,username)
        ibm_db.bind_param(stmt,2,password)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        print (account)
        if account:
            session['loggedin'] = True
            session['id'] = account['USERNAME']
            userid=  account['USERNAME']
            session['username'] = account['USERNAME']
            msg = 'Logged in successfully !'
            
            msg = 'Logged in successfully !'
            return render_template('dashboard.html', msg = msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg = msg)

@app.route('/register', methods =['GET', 'POST'])
def registet():
    msg = ''
    if request.method == 'POST' :
        username = request.form['username']
        email = request.form['email']
        phone_num = request.form['phone_num']
        password = request.form['confirm_password']
        sql = "SELECT * FROM login WHERE username =?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt,1,username)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        print(account)
        if account:
            msg = 'Account already exists !'
            return render_template('login.html', msg = msg)
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'name must contain only characters and numbers !'
        elif not re.match(r'[0-9]+', phone_num):
            msg = 'phone number must contain only numbers !'
        else:
            insert_sql = "INSERT INTO user_details VALUES (?, ?, ?, ?)"
            prep_stmt = ibm_db.prepare(conn, insert_sql)
            ibm_db.bind_param(prep_stmt, 1, username)
            ibm_db.bind_param(prep_stmt, 2, email)
            ibm_db.bind_param(prep_stmt, 3, phone_num)
            ibm_db.bind_param(prep_stmt, 4, password)
            ibm_db.execute(prep_stmt)

            insert_sql_1 = "INSERT INTO login VALUES (?, ?)"
            prep_stmt_1 = ibm_db.prepare(conn, insert_sql_1)
            ibm_db.bind_param(prep_stmt_1, 1, username)
            ibm_db.bind_param(prep_stmt_1, 2, password)
            ibm_db.execute(prep_stmt_1)
            msg = 'You have successfully registered !'
            return render_template('login.html', msg = msg)
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
        return render_template('register.html', msg = msg)
    return render_template('register.html', msg = msg)    
    
if __name__=='__main__':
    app.run(host='0.0.0.0')