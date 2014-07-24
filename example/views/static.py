# -*- coding: utf-8 -*-

from flask import Blueprint

static = Blueprint('static', __name__)


@static.route('/')
def home():
    return "Hello World."
