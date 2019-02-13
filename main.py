import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output, State
import datetime
import dash_table
from flask import Flask, jsonify, abort, make_response, request, url_for
from pages import files_page
from pages import db_page
from pages import Home_Page
import requests

print(dcc.__version__) # 0.6.0 or above is required
server = Flask(__name__)
app = dash.Dash(__name__, server=server)
app.css.append_css({'external_url': 'https://cdn.rawgit.com/plotly/dash-app-stylesheets/2d266c578d2a6e8850ebce48fdb52759b2aef506/stylesheet-oil-and-gas.css'})

app.config.suppress_callback_exceptions = True
