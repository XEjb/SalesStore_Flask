from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# БД - Таблицы - Записи
# Таблица:
# id     title     price    isActivate
# 1      some      100      True
# 2      some2     200      False
# 3      some3     40       True
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=True)
    isActivate = db.Column(db.Boolean, default=True)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/create', methods=['POST', 'GET'])
def create():
    return render_template('create.html')


if __name__ == "__main__":
    app.run(debug=True)