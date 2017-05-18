from flask import Flask
from flask import request,render_template
app=Flask(__name__)

@app.route('/',methods=['GET'])
def signin_form():
    return render_template('signin_form.html')

@app.route('/',methods=['POST'])
def signin():
    username=request.form['username']
    password=request.form['password']
    if username=='admin' and password=='1234':
        return render_template('signin_ok.html',username=username)
    return render_template('signin_form.html',message='wrong username or password')
if __name__ =='__main__':
    app.run()
