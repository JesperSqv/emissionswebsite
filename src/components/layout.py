from Dash import Dash, html

def create_layout(app: Dash) -> html.div:
    return html.Div(
        className="app-div"
        children=[
            html.H1(app.title),
            html.Hr,
        ]
    )