import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

import pandas as pd
pd.options.plotting.backend = "plotly"

from . import ids

total_path = "data/co_emissions_total.csv"
per_capita_path = "data/co_emissions_per_capita.csv"
total_cumulative_path = "data/co_emissions_total_cumulative.csv"
per_capita_cumulative_path = "data/co_emissions_per_capita_cumulative.csv"

def render(app: Dash) -> html.Div:
    
    data = pd.read_csv("data/co_emissions_per_capita.csv")
    data = data.set_index("Year")
    
    selected_countries = ["United States","Finland",  "China"]

    filtered_data = data[selected_countries]
    
    fig = px.line(filtered_data, x=filtered_data.index, y=filtered_data.columns, title="CO2 emissions per capita",
                  labels={"value": "CO2 in tons", "variable": "Nations"})
    
    # Update layout to move x-axis labels to the right
    fig.update_layout(
        yaxis=dict(
            side="right"  # Move the y-axis labels to the right side as well
        )
    )

    return html.Div(dcc.Graph(figure=fig), id=ids.LINE_CHART)

    