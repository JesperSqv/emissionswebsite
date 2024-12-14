[Visit the App](https://emissionswebsite.onrender.com)

# Emission Data Visualization App

## Overview

This project is a Dash-based web application for visualizing CO2 emissions data. Users can explore emissions data through interactive line charts and choropleth maps. The app is styled with Bootstrap and provides an intuitive user experience for selecting datasets and countries.

## Features

- Interactive line charts for CO2 emissions.
- View data in four perspectives:
  - Total CO2 emissions
  - CO2 emissions per capita
  - Total cumulative CO2 emissions
  - Cumulative CO2 emissions per capita
- Choropleth maps for visualizing emissions data across countries.
- Dropdown for selecting specific countries.
- Buttons for switching between different datasets.
- Responsive design with Bootstrap styling.

## Directory Structure

```
.
├── Dockerfile                # Docker configuration for containerization
├── README.md                # Documentation for the project
├── app.py                   # Main entry point for the Dash application
├── assets/
│   └── style.css            # Custom CSS styles
├── data/                    # CSV files with emissions data
│   ├── co_emissions_per_capita.csv
│   ├── co_emissions_total.csv
│   ├── countries.csv
│   └── ...
├── requirements.txt         # Python dependencies
└── src/
    └── components/          # Dash components
        ├── choropleth_map.py
        ├── country_dropdown.py
        ├── ids.py
        ├── layout.py
        ├── line_chart.py
        └── select_perspective_buttons.py
```

## Setup and Usage

### Prerequisites

- Docker installed on your system.

### Run with Docker

1. Build the Docker image:

   ```bash
   docker build -t emission-app .
   ```

2. Run the Docker container:

   ```bash
   docker run -p 8000:8000 emission-app
   ```

3. Open the app in your browser at `http://localhost:8000`.

### Development Setup

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application locally:

   ```bash
   python app.py
   ```

5. Open the app in your browser at `http://localhost:8050`.

## Key Components

- **`app.py`**: Initializes the Dash app and sets up the layout.
- **`src/components/`**:
  - `choropleth_map.py`: Handles the choropleth map functionality.
  - `line_chart.py`: Creates interactive line charts.
  - `country_dropdown.py`: Dropdown for country selection.
  - `select_perspective_buttons.py`: Buttons to toggle between datasets.
  - `layout.py`: Combines components into the app layout.
  - `ids.py`: Centralized IDs for components.

## Data Sources

The data used in this project comes from the following sources:

- Hannah Ritchie, Max Roser, and Pablo Rosado (2022) - "Energy". Published online at OurWorldinData.org. Retrieved from: [https://ourworldindata.org/energy](https://ourworldindata.org/energy) [Online Resource]
- HYDE (2023); Gapminder (2022); UN WPP (2024) – with major processing by Our World in Data. "Population" [dataset]. PBL Netherlands Environmental Assessment Agency, "History Database of the Global Environment 3.3"; Gapminder, "Population v7"; United Nations, "World Population Prospects"; Gapminder, "Systema Globalis" [original data]. Retrieved September 27, 2024, from [https://ourworldindata.org/grapher/population](https://ourworldindata.org/grapher/population)
- Hannah Ritchie and Max Roser (2020) - "CO₂ emissions" Published online at OurWorldinData.org. Retrieved from: [https://ourworldindata.org/co2-emissions](https://ourworldindata.org/co2-emissions) [Online Resource]

The cumulative CO2 emissions are calculated using the equation:

$$\text{CO2 cumulative year } x = \sum_{y= \text{start year}}^{x} \text{CO2 year } y$$

And for the cumulative CO2 per capita:

$$\text{CO2 cumulative per capita year } x = \frac{\text{CO2 cumulative year } x} {\text{population year } x}$$

The `data/` directory contains data for the plot and the map.

## License

This project is licensed under the MIT License. See `LICENSE` for details.

## Acknowledgments

- [Dash](https://dash.plotly.com/) for the web framework.
- [Plotly](https://plotly.com/) for interactive visualizations.
- [Bootstrap](https://getbootstrap.com/) for styling.


