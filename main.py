from dash import Dash, html
from dash_bootstrap_components.themes import BOOTSTRAP

def main() -> None:
    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = "Emission data"
    app.layout = html.Div()
    app.run()


if __name__ == "__main__":
    main()