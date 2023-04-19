# import libraries
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# setting up the data and labels for dropdown
df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
dd_labels = [{'label': df.year.unique()[i], 'value': df.year.unique()[i]}
             for i in range(df.year.unique().shape[0])]


# setting up the page layout
page_layout = [
    dbc.Row([
        dbc.Col([
            html.H1('Callback Example', className='text-center mb-3, p-3')
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.H3('Select a year', className='text-center'),
            dcc.Dropdown(
                id='year-dropdown',
                options=dd_labels,
                value=df['year'].max(),
                clearable=False,
            )
        ],
            width={'size': 4, 'offset': 1, 'order': 0}
        ),
        dbc.Col([
            html.H3('Cool chart column', className='text-center'),
            dcc.Graph(id='graph-with-dropdown'),
        ],
            width={'size': 6, 'offset': 1, 'order': 0}
        )
    ]),
]

# setup the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div(page_layout)


# setting up the interactivity with callbacks
@app.callback(
    Output('graph-with-dropdown', 'figure'),
    Input('year-dropdown', 'value')
)
def update_figure(selected_year):
    filtered_df = df[df.year == int(selected_year)]
    fig = px.scatter(filtered_df, x='gdpPercap', y='lifeExp', size='pop',
                     color='continent', hover_name='country', log_x=True, size_max=55)
    return fig


# running the app
if __name__ == '__main__':
    app.run_server(debug=True)
