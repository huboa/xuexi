from flask import Flask,render_template,request,redirect,session

app = Flask('xxxx',template_folder="templates")
app.secret_key = 'as923lrjks9d8fwlkxlduf'

def wapper(func):
    def inner(*args,**kwargs):
        return func(*args,**kwargs)
    return inner


def wapper(func):
    def inner(*args,**kwargs):
        return func(*args,**kwargs)
    return inner



@app.route('/xxxx',methods=['GET'])
def xxxx():
    user_info = session.get('user_info')
    if not user_info:
        return redirect('/login')

    return render_template('index.html')


@app.route('/order',methods=['GET'])
def order():
    user_info = session.get('user_info')
    if not user_info:
        return redirect('/login')

    return render_template('index.html')

@app.route('/index',methods=['GET'])
def index():
    user_info = session.get('user_info')
    if not user_info:
        return redirect('/login')

    return render_template('index.html')


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        if user == 'alex' and pwd == '123':
            session['user_info'] = user
            return redirect('/index')
        # return render_template('login.html',msg = "用户名或密码错误",x =  123)
        return render_template('login.html',**{'msg':'用户名或密码错误'})

if __name__ == '__main__':
    app.run()
