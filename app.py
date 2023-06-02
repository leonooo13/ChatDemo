from flask import Flask,request
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def xxxx():
    if request.method == 'GET':
        
        return "hi"

if __name__ == '__main__':
    app.run(host='0.0.0.0')