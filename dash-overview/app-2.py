# importing libraries 
from dash import Dash, dcc, html
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.express as px

# initilizing the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# building the app  layout 
first_page = [
    dbc.Row([
     dbc.Col([
      html.H1('Site heading', className='text-center')
    ])
  ]),
  dbc.Row([
    dbc.Col([
    html.H3('header 3'),
    html.Div(children='first div'),
    html.Hr(),
    ],
    width={'size':3, 'offset':2, 'order': 1},
    ),

    dbc.Col([
    html.H3('h3 header', className='text-end'),
    html.Div(children='second div'),
    html.Hr(),
    ],
    width={'size': 3, 'offset': 2, 'order': 0}
    ),
  ])
]

# assigning the layout to the page
app.layout = html.Div(id='page-content', children=first_page)

if __name__ == '__main__':
    app.run_server(debug=True, port=2001)

