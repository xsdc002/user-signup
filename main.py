from flask import Flask, redirect, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def validation():
    password = (request.form['password'])
    verify = (request.form['verify'])
    email = (request.form['email'])
    username = (request.form['username'])
    password_error = ''
    verify_error = ''
    email_error = ''
    username_error = ''

    #password tests
    if len(password) < 3:
        password_error = 'Password must be greater than 3 characters'
    elif len(password) > 20:
        password_error = 'Password must be less than 20 characters'

    elif ' ' in password:
        password_error = 'Password cannot contain any spaces'
    


    #verify tests
    if len(verify) < 3:
        verify_error = 'verify must be greater than 3 characters'
    elif len(verify) > 20:
        verify_error = 'verify must be greater than 20 characters'
    elif verify != password:
        verify_error = 'passwords do not match'
    elif ' ' in verify:
        verify_error = 'verify cannot contain any spaces'

    #email tests
   
    if len(email) > 0:
        if ' ' in email: 
            email_error = 'invalid email, email cannot contain any spaces'
        elif email.count('@') > 1 in email:
            email_error = 'invalid email'
        elif email.count('.') < 1 in email:
            email_error = 'invalid email'
        elif ' ' in email:
            email_error = 'invalid email, email cannot contain spaces'

    #username tests
    if len(username) < 3:
        username_error = 'username must be greater than 3 characters'
    elif len(username) > 20:
        username_error = 'username must be greater than 20 characters'
    elif ' ' in username:
        username_error = 'invalid username, email cannot contain any spaces'

   
    
    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', username=username)
    else:
        return render_template('index.html', password_error=password_error, verify_error=verify_error, email=email, email_error=email_error, username=username, username_error=username_error)


if __name__ == "__main__":
    app.run()
