# Empty Flask App

[![Build Status](https://travis-ci.org/nickcharlton/empty-flask-app.svg?branch=master)](https://travis-ci.org/nickcharlton/empty-flask-app)

This is an empty [Flask][] app, using [Blueprints][], [SQLAlchemy][] and
[WTForms][] which is designed to provide the beginnings of a moderately
complex Flask project.

It's designed to spin a nice balance between integration and modularity between
Blueprints, `static.py` is included to show this off. Typically, this would be
used for simple pages.

It's based around the "functional" example from [Robert Picard][]'s
[Explore Flask][] book (which I [kickstarted][]), but it's also taken
inspiration from [Armin Ronacher][]'s [Large App How To][]. And has example
tests.

## Structure

```
.
├── config.py
├── example
│   ├── __init__.py
│   ├── static
│   ├── templates
│   └── views
│       ├── __init__.py
│       └── static.py
├── requirements.txt
└── run.py
```

Models would go inside the `example` package as `models.py`, similarly
something like a group of [Celery][] tasks would go in `tasks.py` alongside it.

## Testing

There's an included test module which sits alongside the `app` module called
`tests`. It's assumed that you'll use [nose][] for your tests. It also has
support for [Travis CI][], too.

The example tests are structured to follow the test of the project, with a
package for each project directory. So, you'd typically have a test file for
every file in the `views/` directory and then another package containing tests
for your `utils/` directory, for example.

Running tests is as simple as:

```sh
nosetests
```

In the root of the project. The flags of `-v` and `-s` will tell you which
tests are being run, and the stdout of each test, respectively.

Both the [Flask docs][] and the included [Flask-Testing][] package provide
good explanations of structuring your tests.

## Author

Copyright (c) Nick Charlton <nick@nickcharlton.net>. MIT Licensed.

[Flask]: http://flask.pocoo.org/
[Blueprints]: http://flask.pocoo.org/docs/blueprints/
[SQLAlchemy]: http://www.sqlalchemy.org/
[WTForms]: http://wtforms.readthedocs.org/en/latest/
[Robert Picard]: http://robert.io/
[Explore Flask]: http://exploreflask.com/
[kickstarted]: https://www.kickstarter.com/projects/1223051718/practical-flask-book-project
[Armin Ronacher]: https://github.com/mitsuhiko
[Large App How To]: https://github.com/mitsuhiko/flask/wiki/Large-app-how-to
[Celery]: http://www.celeryproject.org/
[nose]: https://nose.readthedocs.org/en/latest/
[Travis CI]: https://travis-ci.org/
[Flask docs]: http://flask.pocoo.org/docs/testing/
[Flask-Testing]: https://pythonhosted.org/Flask-Testing/
