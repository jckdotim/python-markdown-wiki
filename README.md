# Python Markdown Wiki for Heroku
![ci workflow](https://github.com/jckdotim/python-markdown-wiki/actions/workflows/main.yml/badge.svg) [![codecov](https://codecov.io/github/jckdotim/python-markdown-wiki/branch/master/graph/badge.svg?token=2Qm2KC9w6J)](https://codecov.io/github/jckdotim/python-markdown-wiki)

This is an [Wiki][2] that can use [Markdown][3] and supports [Heroku][1].

# How to Use

## Use button

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Deploy using CLI

    $ git clone git@github.com:jckdotim/python-markdown-wiki.git
    $ heroku create NAME
    $ git push heroku master
    $ heroku run python cli.py createdb

# Features
 - [Bootstrap][4]-based User Interface
 - [Markdown][3] Support
 - `[[Topic]]` will be changed to `[Topic](/Topic)`

  [1]: http://heroku.com/
  [2]: http://en.wikipedia.org/wiki/Wiki
  [3]: http://daringfireball.net/projects/markdown/
  [4]: http://getbootstrap.com/
