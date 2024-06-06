from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

# Flaskアプリケーションのインスタンス化
app = Flask(__name__)

# データベースのパス設定
db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'instance', 'data.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# インスタンスフォルダが存在しない場合は作成
if not os.path.exists(os.path.dirname(db_path)):
    os.makedirs(os.path.dirname(db_path))

# データベースファイルのパスを出力
print(f"Database file path: {db_path}")

# SQLAlchemyのインスタンス化
db = SQLAlchemy(app)

# データベースのモデル定義
class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

# アプリケーションコンテキスト内でデータベースを作成
with app.app_context():
    db.create_all()

# ルートの定義
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.form['content']
        new_data = Data(content=content)
        db.session.add(new_data)
        db.session.commit()
        return redirect(url_for('index'))
    all_data = Data.query.all()
    return render_template('index.html', data=all_data)

if __name__ == '__main__':
    app.run(debug=True)
