import sql
from flask import Flask,request,render_template,redirect,make_response
app = Flask(__name__)

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username=request.form["username"]
        passwd=request.form["passwd"]
        # SQL处理
        sql_query = "SELECT * FROM user WHERE user_name = ? AND password = ?"
        name_passwd=(username,passwd)
        res=sql.select(sql_query,name_passwd)
        print(res)
        if res:
            # 设置cookies
            rsp=make_response(redirect('/'))
            rsp.set_cookie('username',username,max_age=3600)# ,kw stored,max_age after 3600 second,it will be invaild
            return rsp
        else:
            message="账号或密码不对，请重新输入或者注册"
            return render_template('login.html',message=message)
    else:
        return render_template('login.html')
@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='GET':
        username=request.cookies.get("username")
        if username:
            return render_template('index.html',username=username)
        else:
            return redirect('/login')
    if request.method=="POST":
        message=request.form["message"]
        print(message)
        answer=message
        return render_template('index.html',answer=answer)
if __name__ == '__main__':
    app.run(host='0.0.0.0')