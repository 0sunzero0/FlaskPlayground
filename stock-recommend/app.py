from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbStock
collection = db.codes


# HTML 화면 보여주기
@app.route('/')
def test():
    return render_template('index.html')

@app.route('/base/codes', methods=['GET'])
def view_group():
    group = collection.distinct("group")
    return jsonify({'result': 'success', 'group': group})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)