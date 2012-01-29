import os
from flask import Flask, render_template, redirect, url_for, request
from flaskext.sqlalchemy import SQLAlchemy
from flaskext.markdown import Markdown
import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL", "sqlite:///env/local.db")
db = SQLAlchemy(app)
markdown = Markdown(app)

class Topic(db.Model):
    name = db.Column(db.String(32), primary_key=True)
    body = db.Column(db.Text, nullable=True, default=u"")
    modified_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())

    @classmethod
    def find(cls, name):
        topic = Topic.query.get(name)
        if topic is None:
            topic = Topic(name, None)
            db.session.add(topic)
            db.session.commit()
        return topic

    def __init__(self, name, body):
        self.name = name
        self.body = body
    
    def __repr__(self):
        return '<Topic {0}>'.format(self.name)

@app.template_filter('parse_link')
def parse_link(body):
    import re
    for word in re.findall(r"\[\[([^\]]+)\]\]", body):
        body = body.replace(u'[[{0}]]'.format(word), u'[{0}](/{0})'.format(word))
    return body

@app.route("/")
def index():
    name = request.values.get('name')
    if name is None:
        name = 'README'
    return redirect(url_for('topic', name=name))

@app.route("/<string:name>", methods=["GET", "POST"])
def topic(name):
    topic = Topic.find(name)
    if request.method == 'GET':
        return render_template('base.html', topic=topic)
    else:
        topic.body = request.values.get('body')
        db.session.commit()
        return redirect(url_for('topic', name=name))
       

@app.route("/<string:name>/edit")
def edit(name):
    topic = Topic.find(name)
    return render_template('edit.html', topic=topic)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
