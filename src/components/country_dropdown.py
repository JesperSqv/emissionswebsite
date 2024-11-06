from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import pandas as pd
from . import ids

df_countries = pd.read_csv("data/countries.csv")

def render(app: Dash) -> html.Div:
    all_countries = df_countries["Country"].tolist()

    return html.Div(
        children=[
            html.H6("Nation"),
            dcc.Dropdown(
                id=ids.COUNTRY_DROPDOWN,
                options=[{"label": country, "value": country} for country in all_countries],
                value=["United States", "Finland",  "China"],
                multi=True,
            ),
        ]
    )