# Import libraries
import pandas as pd
from dash import dcc, Dash, html
import plotly.express as px
import dash_bootstrap_components as dbc


# initializing teh app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# setting up the page layout with dash bootstrap component
first_page = [
    dbc.Row([
        dbc.Col(
            html.H1('First Column in first Row', className='text-center')
        )
    ]),
]

# assigning the pages to the app layout
app.layout = html.Div(id='page-content', children=first_page)


# starting the app
if __name__ == '__main__':
    app.run_server(debug=True, port=2001)
