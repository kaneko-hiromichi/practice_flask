from flask import Flask,render_template



app = Flask(__name__)

bullets = []

[bullets.append(f"箇条書き{n}")  for n in range(1,11)]

@app.route("/japan")
def hello():
    return render_template("hello.html" , bullets=bullets)