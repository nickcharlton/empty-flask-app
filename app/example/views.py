# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

from app import db

mod = Blueprint('example', __name__)


@mod.route('/')
def index():
    return render_template("example/index.html")
