from dash import Dash, html

import pandas as pd

from . import line_chart

def create_layout(app: Dash) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            line_chart.render(app),
        ],
    )