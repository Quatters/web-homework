from flask import Flask


app = Flask(__name__)


import controllers.index
import controllers.hello
import controllers.subject
import controllers.olympiad
