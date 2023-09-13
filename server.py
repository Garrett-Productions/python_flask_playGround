from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Garrett!'

@app.route('/play')
def play():
    return render_template("index.html")

@app.route('/play/<int:num>')
def playNum(num):
    return render_template("index.html", num = num)

@app.route('/play/<int:num>/<string:color>')
def playAlot(num, color):
    return render_template("index.html", num = num, color = color)

if __name__=="__main__":
    app.run(debug=True, port = 5001)
