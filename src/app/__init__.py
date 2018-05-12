import os
from flask import Flask, render_template, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
import config

# Configure Flask app
app = Flask(__name__, static_url_path='/static')
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Database
db = SQLAlchemy(app)

# Import + Register Blueprints
# from app.TODO import TODO as TODO # pylint: disable=C0413
# app.register_blueprint(TODO)

# React Catch All Paths
@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')

@app.route('/about', methods=['GET'])
def about_path():
  return render_template('about.html')

@app.route('/<path:path>', methods=['GET'])
def any_root_path(path):
  return render_template('index.html')

# HTTP error handling
@app.errorhandler(404)
def not_found(error):
  return render_template('404.html'), 404
