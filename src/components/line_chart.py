import plotly.express as px
from dash import Dash, dcc, html, callback_context
from dash.dependencies import Input, Output

import pandas as pd
pd.options.plotting.backend = "plotly"

from . import ids

countries_path = "data/countries.csv"

total_path = "data/co_emissions_total.csv"
per_capita_path = "data/co_emissions_per_capita.csv"
total_cumulative_path = "data/co_emissions_total_cumulative.csv"
per_capita_cumulative_path = "data/co_emissions_per_capita_cumulative.csv"

def render(app: Dash) -> html.Div:
    
    # Initial figure setup, will update based on button clicks
    initial_data = pd.read_csv(per_capita_path)
    initial_data = initial_data.set_index("Year")
    default_countries = ["United States", "Finland", "China"]
    
    fig = px.line(
        initial_data[default_countries],
        x=initial_data.index,
        y=default_countries,
        title="CO2 emissions per capita",
        labels={"value": "CO2 in tons", "variable": "Nations"}
    )
    
    fig.update_layout(
        yaxis=dict(side="right")
    )

    graph = html.Div(dcc.Graph(figure=fig), id=ids.LINE_CHART)

    # Callback to update the chart based on button click
    @app.callback(
        Output(ids.LINE_CHART, "children"),
        [
            Input(ids.SELECT_TOTAL, "n_clicks"),
            Input(ids.SELECT_PER_CAPITA, "n_clicks"),
            Input(ids.SELECT_TOTAL_CUMULATIVE, "n_clicks"),
            Input(ids.SELECT_PER_CAPITA_CUMULATIVE, "n_clicks"),
            Input(ids.COUNTRY_DROPDOWN, "value")  # Dropdown selection as an input
        ]
    )
    def update_chart(n_total, n_per_capita, n_total_cumulative, n_per_capita_cumulative, selected_countries):
        
        # If no country is selected, display a message
        if not selected_countries:
            return html.Div("No country selected.", id=ids.LINE_CHART)

        
        # Determine which button was clicked
        ctx = callback_context
        if not ctx.triggered:
            return dcc.Graph(figure=fig)  # No button clicked yet

        # Default to per capita path if no button click
        data_path = per_capita_path
        title = "CO2 emissions per capita"

        button_id = ctx.triggered[0]["prop_id"].split(".")[0]
        if button_id == ids.SELECT_TOTAL:
            data_path = total_path
            title = "Total CO2 emissions"
        elif button_id == ids.SELECT_TOTAL_CUMULATIVE:
            data_path = total_cumulative_path
            title = "Total cumulative CO2 emissions"
        elif button_id == ids.SELECT_PER_CAPITA_CUMULATIVE:
            data_path = per_capita_cumulative_path
            title = "Per capita cumulative CO2 emissions"

        # Load data and filter by selected countries
        data = pd.read_csv(data_path)
        data = data.set_index("Year")
        
        # Filter only valid selected countries
        selected_countries = [country for country in selected_countries if country in data.columns]
        if not selected_countries:
            return html.Div("No valid country selected.", id=ids.LINE_CHART)

        filtered_data = data[selected_countries]

        # Update figure
        fig = px.line(
            filtered_data,
            x=filtered_data.index,
            y=filtered_data.columns,
            title=title,
            labels={"value": "CO2 in tons", "variable": "Nations"}
        )
        fig.update_layout(yaxis=dict(side="right"))

        return dcc.Graph(figure=fig)

    return graph

    