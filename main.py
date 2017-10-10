from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html',password='',password_error='',verify='',verify_error='',email='',email_error='',username='',user_error='')

@app.route('/',methods=['POST'])
def validation():
    p = (request.form['password'])
    v = (request.form['verify'])
    e = (request.form['email'])
    u = (request.form['username'])
    password_error=''
    verify_error=''
    email_error=''
    user_error=''

    if not (len(p)>3) and (len(p)<20):
        password_error='pasword must be between 3 and 20 characters'
    if v != p:
        verify_error='passwords must match'
    if '.' not in email and ' ' not in email or '@' in email:
        email_error='invalid email'
    if not (len(u)>3) and (len(u)<20):
        user_error='username must be between 3 and 20 characters'

    if not password_error and not verify_error and not email_error and not user_error:
        return render_template('welcome.html',username=u)
    else:
        return render_template('index.html', username=u)



   

    if not user_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', username=u)
    else:
        return render_template('index.html',password='',password_error='',verify='',verify_error='',email='',email_error='',username='',user_error='')



app.run()