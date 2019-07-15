import os
import hashlib
import logging
import json
from datetime import datetime
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request, json, jsonify, abort, make_response



app = Flask(__name__,template_folder="/app-run/api/templates")
app.config['TEMPLATES_AUTO_RELOAD'] = True 
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
db.init_app(app)


# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    domain:port/

    :return:        the rendered template 'index.html'
    """
    return render_template('index.html')

@app.route("/stats/", methods=["GET","POST"], strict_slashes=False )
def stats():
    resultproxy = db.engine.execute("SELECT count(is_mutant) as count ,(CASE WHEN is_mutant = 1 THEN 'count_mutant_dna' ELSE  'count_human_dna'  END) as type FROM test_base.stats group by is_mutant;")
    print(resultproxy)
    data = {}
    d, a = {}, []
    for rowproxy in resultproxy:
        # rowproxy.items() returns an array like [(key0, value0), (key1, value1)]
        for column, value in rowproxy.items():
            # build up the dictionary
            print(' %s %s'%(column,value))
            d = {**d, **{column: value}}
        #a.append(d)
        data[d['type']] = d['count']
    data['ratio'] = data['count_mutant_dna']/data['count_human_dna']
    print(data)
    return json.dumps(data)



