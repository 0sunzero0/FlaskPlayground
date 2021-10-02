from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
from datetime import datetime
from bson import ObjectId

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client.dbBoard


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/save', methods=['POST'])
def save_post():
    title_receive = request.form['title_give']
    content_receive = request.form['content_give']
    current_time = datetime.now()

    doc = {'title': title_receive, 'content': content_receive,
           'reg_date': current_time}
    db.articles.insert_one(doc)
    return jsonify({'result': "success", 'msg': "게시글 작성 완료!"})

@app.route('/show', methods=['GET'])
def get_post():
    doc = list(db.articles.find({}).sort('reg_date', 1))
    for one_post in doc:
       one_post["_id"] = str(one_post["_id"])
    return jsonify({"result": "success", "articles": doc})


@app.route('/delete', methods=['DELETE'])
def delete_post():
    id_receive = request.form['id_give']
    db.articles.delete_one({'_id': ObjectId(id_receive)})
    return jsonify({"result": "success", 'msg': 'til 삭제 완료!'})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
