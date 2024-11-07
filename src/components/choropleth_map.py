import plotly.express as px
from dash import Dash, dcc, html, callback_context
from dash.dependencies import Input, Output

import pandas as pd
pd.options.plotting.backend = "plotly"

from . import ids

countries_path = "data/countries.csv"

total_path = "data/co_emissions_total_map.csv"
per_capita_path = "data/co_emissions_per_capita_map.csv"
total_cumulative_path = "data/co_emissions_total_cumulative_map.csv"
per_capita_cumulative_path = "data/co_emissions_per_capita_cumulative_map.csv"

def render(app: Dash) -> html.Div:
    map = html.Div([
        html.H1("CO2 Emissions by Country"),
        # Div for displaying the choropleth map
        html.Div(id=ids.CHOROPLETH_MAP)
    ])

    # Callback to update the map based on button clicks
    @app.callback(
        Output(ids.CHOROPLETH_MAP, "children"),
        [
            Input(ids.SELECT_TOTAL, "n_clicks"),
            Input(ids.SELECT_PER_CAPITA, "n_clicks"),
            Input(ids.SELECT_TOTAL_CUMULATIVE, "n_clicks"),
            Input(ids.SELECT_PER_CAPITA_CUMULATIVE, "n_clicks"),
        ]
    )
    def update_map(n_total, n_per_capita, n_total_cumulative, n_per_capita_cumulative):
        # Determine which button was clicked
        ctx = callback_context
        if not ctx.triggered:
            return html.Div("Select a dataset to display the map.")
        
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]
        
        # Choose the data file path based on the button clicked
        if button_id == ids.SELECT_TOTAL:
            data_path = total_path
            title = "Total CO2 emissions by Country"
            column = "CO2 total"
        elif button_id == ids.SELECT_PER_CAPITA:
            data_path = per_capita_path
            title = "CO2 emissions per capita by Country"
            column = "CO2 per capita"
        elif button_id == ids.SELECT_TOTAL_CUMULATIVE:
            data_path = total_cumulative_path
            title = "Total cumulative CO2 emissions by Country"
            column = "CO2 total cumulative"
        elif button_id == ids.SELECT_PER_CAPITA_CUMULATIVE:
            data_path = per_capita_cumulative_path
            title = "Per capita cumulative CO2 emissions by Country"
            column = "CO2 per capita cumulative"
        
        # Load the selected data
        data = pd.read_csv(data_path)

        # Define the desired order with '1800' first
        desired_year_order = ['1800'] + sorted([year for year in data['year'].unique() if year != '1800'])
        
        # Assuming the data has columns like "iso_alpha" for country codes and "emissions" for values
        fig = px.choropleth(
            data,
            locations="Code",
            color=column,  # Replace with the column name for emissions in your data
            hover_name="country",  # Replace with country name column if necessary
            projection="natural earth",
            animation_frame="year",
            category_orders={'year': desired_year_order},
            title=title
        )
        
        return dcc.Graph(figure=fig)

    return map