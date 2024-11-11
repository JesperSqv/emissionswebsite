import os
from dash import Dash, html
from dash_bootstrap_components.themes import BOOTSTRAP

from src.components.layout import create_layout

app = Dash(__name__, external_stylesheets=[BOOTSTRAP])

server = app.server

app.title = "Emission data"
app.layout = create_layout(app)

if __name__ == '__main__':
    app.run(debug=False)