# Python Markdown Wiki for Heroku
---

[Heroku]에서 바로 올려서 쓸 수 있는 Markdown [Wiki]가 필요해서 만들어보았습니다.

별 기능 없지만 차차 추가하겠습니다. 필요한 기능은 이슈에 올려주시거나 Pull Request 보내주세요.

# How to Use
----
    $ git clone git@github.com:shinvee/python-markdown-wiki.git
    $ heroku create NAME --stack cedar
    $ git push heroku master
    $ heroku run python create_db.py

  [Heroku]: http://heroku.com/
  [Wiki]: http://en.wikipedia.org/wiki/Wiki
