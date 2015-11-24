# Python Markdown Wiki for Heroku [![Build Status](https://travis-ci.org/shinvee/python-markdown-wiki.svg)](https://travis-ci.org/shinvee/python-markdown-wiki) [![Coverage Status](https://coveralls.io/repos/shinvee/python-markdown-wiki/badge.svg?branch=master&service=github)](https://coveralls.io/github/shinvee/python-markdown-wiki?branch=master)

This is an [Wiki][2] that can use [Markdown][3] and supports [Heroku][1].

# How to Use
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

or

    $ git clone git@github.com:shinvee/python-markdown-wiki.git
    $ heroku create NAME
    $ git push heroku master
    $ heroku run python create_db.py

# Features
 - [Bootstrap][4] based User Interface
 - [Markdown][3] Support
 - `[[Topic]]` will be changed to `[Topic](/Topic)`

  [1]: http://heroku.com/
  [2]: http://en.wikipedia.org/wiki/Wiki
  [3]: http://daringfireball.net/projects/markdown/
  [4]: http://getbootstrap.com/
