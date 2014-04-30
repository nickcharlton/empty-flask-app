# -*- coding: utf-8 -*-

from flask.ext.testing import TestCase

from app import app, db


class AppTestCase(TestCase):
    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        app.config['TESTING'] = True

        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_not_found_error_handler(self):
        response = self.client.get('/404')

        self.assert_404(response)
        self.assert_template_used('404.html')
        assert '<h1>Page Not Found</h1>' in response.data
