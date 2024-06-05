from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz
import os

app = Flask(__name__)

# プロジェクトのルートディレクトリ内のパスを使用
db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'blog.db')
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    body = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(pytz.timezone("Asia/Tokyo")))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create")
def create():
    return render_template("create.html")

if __name__ == '__main__':
    app.run(debug=True)
