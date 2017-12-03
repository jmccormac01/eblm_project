"""
A Flask implentation of the EBLM project
"""
# pylint: disable=invalid-name
from flask import Flask
app = Flask(__name__)
app.config.from_object('config')
import eblm.views
