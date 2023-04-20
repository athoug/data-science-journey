# import libraries
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# initialize app
app = Dash(__name__, external_stylesheets=[dbc.themes.UNITED])

app.layout = html.Div([
    html.H1('Cool Buttons', className='text-center', style={
        'margin-top': '50px',
        'margin-bottom': '50px'
    }),
    dbc.Button('This button is dangerous', color='danger'),
    dbc.Button('This button not so much', color='warning'),
    dbc.Button('This button is harmful', color='info'),
],
    className='d-grid gap-2 col-6 mx-auto',
)

if __name__ == '__main__':
    app.run_server(debug=True)
