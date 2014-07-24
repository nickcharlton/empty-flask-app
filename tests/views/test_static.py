# -*- coding: utf-8 -*-

from flask.ext.testing import TestCase

from example import app, db


class ExampleViewsTestCase(TestCase):
    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        app.config['TESTING'] = True

        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_index(self):
        response = self.client.get('/')

        self.assert_200(response)
        self.assert_template_used('static/index.html')
        assert '<p>Hello World!</p>' in response.data
