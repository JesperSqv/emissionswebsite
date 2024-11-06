from dash import Dash, html

import pandas as pd

from . import line_chart, select_perspective_buttons, country_dropdown

def create_layout(app: Dash) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            select_perspective_buttons.render(app),
            line_chart.render(app),
            country_dropdown.render(app),
        ],
    )