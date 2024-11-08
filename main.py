import os
from dash import Dash, html
from dash_bootstrap_components.themes import BOOTSTRAP

from src.components.layout import create_layout

def main() -> None:
    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = "Emission data"
    app.layout = create_layout(app)
    
    # Get the port from environment variables, defaulting to 8050 if not set
    port = int(os.environ.get("PORT", 8050))
    
    # Run the app on host 0.0.0.0 to make it accessible externally
    app.run_server(host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()