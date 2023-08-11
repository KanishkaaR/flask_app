from flask import Flask,render_template

app = Flask(__name__)
#decorator
@app.route("/")
def hello_world():
    number=24
    return render_template("index.html",number=number)
if __name__=="__main__":
    app.run(debug=True)