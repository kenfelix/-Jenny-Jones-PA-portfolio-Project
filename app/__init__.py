from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = '594114819130c83ca2c7e0ff'

from app import home_view, user_view
    