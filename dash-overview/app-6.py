# import libraries
from dash import Dash, dcc, html, callback, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# initialize app
app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

# layout setup
app.layout = html.Div([
    dbc.Col([
        html.H1('Cool Buttons',
                className='text-center text-white bg-danger my-4', style={
                    "borderRadius": "20px"}),
        dbc.Button('This button is dangerous', color='danger'),
        dbc.Button('This button not so much', color='warning'),
        dbc.Button('This button is harmful', color='info'),
    ],
        width={'size': 3, 'offset': 0, 'order': 0}
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True)
