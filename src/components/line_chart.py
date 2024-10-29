import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

import pandas as pd
pd.options.plotting.backend = "plotly"

from . import ids


def render(app: Dash) -> html.Div:
    
    data = pd.read_csv("data/co_emissions_per_capita.csv")
    selected_countries = ["United States","Finland",  "China"]
    filtered_data = data[selected_countries]

    fig = filtered_data.plot()

    return html.Div(dcc.Graph(figure=fig), id=ids.LINE_CHART)

    