from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


# HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name_receive = request.form['name_give']
    order_num_receive = request.form['order_num_give']
    address_receive = request.form['address_give']
    phone_num_receive = request.form['phone_num_give']

    doc = {
        'name' : name_receive,
        'order num' : order_num_receive,
        'address' : address_receive,
        'phone num' : phone_num_receive
    }

    db.keyboardorder.insert_one(doc)

    return jsonify({'msg': '주문 성공적 완료!'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    orders = list(db.keyboardorder.find({}, {'_id': False}))
    return jsonify({'all_orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)