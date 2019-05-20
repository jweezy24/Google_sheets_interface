from flask import Flask
from flask import request
from flask import jsonify
import google_utils as gutil

cache = gutil.cache_machine.load_data()
app = Flask(__name__)

@app.route('/q', methods = ['POST'])
def parse_query():
    pass
