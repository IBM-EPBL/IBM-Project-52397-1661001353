from flask import *
app = Flask(__name__)
@app.route('/')
def setcookie():
    res = make_response("cookie is inserted")
    res.set_cookie('Flask','framework')
    return res

if __name__ =='__main__':
    app.run(debug=True)
    