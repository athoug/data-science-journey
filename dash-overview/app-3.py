# importing libraries
import pandas as pd
from dash import Dash, dcc, html, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px

# setup a data frame
df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

# initialize app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# app layout
app.layout = html.Div([
    html.H1(children='Population throughout the years by country',
            style={'textAlign': 'center'}),
    dcc.Dropdown(df.country.unique(), 'Saudi Arabia', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])

# setup the callback


@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
# graph update method
def update_graph(value):
    dff = df[df.country == value]
    return px.line(dff, x='year', y='pop')


# run the server
if __name__ == '__main__':
    app.run_server(debug=True, port=2001)
