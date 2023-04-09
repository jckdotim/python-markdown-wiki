import os

from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_gfm import Markdown
from werkzeug.routing import BaseConverter
from sqlalchemy.sql import func
from sqlalchemy import inspect


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL",
    "sqlite:////tmp/python_markdown_wiki_local.db"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


def create_tables_if_not_exists():
    with app.app_context():
        engine = db.get_engine()
        inspector = inspect(engine)
        if "topic" not in inspector.get_table_names():
            db.create_all()


create_tables_if_not_exists()

markdown = Markdown(app)


class Topic(db.Model):
    name = db.Column(db.String(32), primary_key=True)
    body = db.Column(db.Text, nullable=True, default='')
    modified_at = db.Column(db.DateTime, nullable=False,
                            server_default=func.now(), onupdate=func.now())
    created_at = db.Column(db.DateTime, nullable=False,
                           server_default=func.now())

    @property
    def backlinks(self):
        return Topic.query.filter(
            Topic.body.like(f'%[[{self.name}]]%')
        )

    @classmethod
    def find(cls, name):
        topic = cls.query.get(name)
        if not topic:
            topic = cls(name, None)
            db.session.add(topic)
            db.session.commit()
        return topic

    def __init__(self, name, body):
        self.name = name
        self.body = body

    def __repr__(self):
        return f'<Topic {self.name}>'


class TopicConverter(BaseConverter):
    def to_python(self, value):
        return Topic.find(value)

    def to_url(self, value):
        return value.name


app.url_map.converters['Topic'] = TopicConverter


@app.template_filter('parse_link')
def parse_link(body):
    import re
    for word in re.findall(r"\[\[([^\]]+)\]\]", body):
        body = body.replace(u'[[{0}]]'.format(word),
                            u'[{0}](/{0})'.format(word))
    return body


@app.route("/")
def index():
    if 'topic' in request.args:
        return redirect(
            url_for('topic', topic=Topic.find(request.args['topic']))
        )
    return redirect(url_for('topic', topic=Topic.find('README')))


@app.route("/<Topic:topic>", methods=["GET", "POST"])
def topic(topic):
    if request.method == 'GET':
        return render_template('base.html', topic=topic)
    else:
        topic.body = request.values.get('body')
        db.session.commit()
        return redirect(url_for('topic', topic=topic))


@app.route("/<Topic:topic>/backlinks")
def backlinks(topic):
    return render_template('backlinks.html', topic=topic)


@app.route("/<Topic:topic>/keynote")
def keynote(topic):
    return render_template('keynote.html', topic=topic)


@app.route("/<Topic:topic>/edit")
def edit(topic):
    return render_template('edit.html', topic=topic)


@app.route('/images', methods=['POST'])
def upload_image():
    result = None
    if 'file' in request.files:
        upload_result = upload(request.files['file'])
        result = cloudinary_url(upload_result['public_id'])[0]
    return jsonify(filename=result)


@app.template_filter('env')
def env(s):
    return os.environ.get(s)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
