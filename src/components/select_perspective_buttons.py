import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from . import ids

def render(app: Dash) -> html.Div:

    buttons = html.Div(
        style={
        'display': 'flex',
        'justify-content': 'center',      # Center horizontally
        'align-items': 'center',          # Center vertically
        'height': '15vh',                
        },
        children=[
            html.Div(
                style={'display': 'flex', 'justify-content': 'space-between', 'width': '400px'},  # Adjust width as needed
                    children=[
                        html.Button('Total emissions', id=ids.SELECT_TOTAL, n_clicks=0),
                        html.Button('Per capita emissions', id=ids.SELECT_PER_CAPITA, n_clicks=0),
                        html.Button('Total cumulative emissions', id=ids.SELECT_TOTAL_CUMULATIVE, n_clicks=0),
                        html.Button('Per capita cumulative emissions', id=ids.SELECT_PER_CAPITA_CUMULATIVE, n_clicks=0),
                    ]
            )
        ]
    )

    return buttons