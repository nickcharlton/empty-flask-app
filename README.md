# Empty Flask App

This is an empty [Flask][] app, using [Blueprints][], [SQLAlchemy][] and [WTForms][]
which is designed to provide the beginnings of a moderately complex Flask project.

This structure allows you to share the configuration, database and so on with the
packages which make up each Blueprint. The included `app/example` directory shows
how to do this.

It's partly based around [Armin Ronacher][]'s [Large App How To][].

## Structure

For the main part of the app:

```
config.py
run.py
shell.py
app/__init__.py
app/constants.py
app/static/js/
app/static/css/
app/static/img/
app/templates/404.html
app/templates/500.html
app/templates/base.html
```

For each Blueprint (replacing `example` in each case):

```
app/example/__init__.py
app/example/views.py
app/example/forms.py
app/example/models.py
app/example/constants.py
app/example/decorators.py
app/templates/example/
```

## Author

Copyright (c) Nick Charlton <nick@nickcharlton.net>. MIT Licensed.

[Flask]: http://flask.pocoo.org/
[Blueprints]: http://flask.pocoo.org/docs/blueprints/
[SQLAlchemy]: http://www.sqlalchemy.org/
[WTForms]: http://wtforms.readthedocs.org/en/latest/
[Armin Ronacher]: https://github.com/mitsuhiko
[Large App How To]: https://github.com/mitsuhiko/flask/wiki/Large-app-how-to
