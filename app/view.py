from app import app, utils
from flask import render_template

@app.route("/")
def home():
    data = utils.get_color_list()
    return render_template('index.html', color_list=data)