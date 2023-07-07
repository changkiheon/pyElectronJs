from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_marshmallow import Marshmallow


app = Flask(__name__)

#------!!!Update sqlite path!!!------
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/chang/Documents/GitHub/pyEletronJS/flask.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
ma = Marshmallow(app)


class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.Text())
    date = db.Column(db.DateTime, default = datetime.datetime.now)

    def __init__(self, title, body):
        self.title = title
        self.body = body


class ArticleSchema(ma.Schema):
    class Meta:
        fields = ('id','title','body','date')

article_schema = ArticleSchema()
article_schemas = ArticleSchema(many=True)



#Get All Articles from table Articles
@app.route('/get', methods = ['GET'])
def get_articles():
    all_articles = Articles.query.all()
    results = article_schemas.dump(all_articles)
    return jsonify(results)

#Get Article by ID
@app.route('/get/<id>', methods=['GET'])
def get_article(id):
    article = Articles.query.get(id)
    if article:
        return article_schema.jsonify(article)
    else:
        return jsonify({'error': 'Article not found'})


#Add Article on Table
@app.route('/add', methods = ['POST'])
def add_article():
    title = request.json['title']
    body = request.json['body']

    articles = Articles(title, body)
    db.session.add(articles)
    db.session.commit()
    return article_schema.jsonify(articles)


#Update Article by ID
@app.route('/update/<id>', methods=['PUT'])
def update_article(id):
    article = Articles.query.get(id)

    title = request.json['title']
    body = request.json['body']
    
    article.title = title
    article.body = body

    db.session.commit()
    return article_schema.jsonify(article)

#Delete Article by ID
@app.route('/delete/<id>', methods=['DELETE'])
def article_delete(id):
    article = Articles.query.get(id)
    db.session.delete(article)
    db.session.commit()

    return article_schema.jsonify(article)






if __name__ == "__main__":
    app.run(debug=True)