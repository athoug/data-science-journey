# This link takes you to the example page of Dash Bootstrap component
# https://dash-bootstrap-components.opensource.faculty.ai/examples/simple-sidebar/page-1

# import libraries
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SLATE])

# styles dictionary setup
# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    'position': 'fixed',
    'top': 0,
    'left': 0,
    'right': 0,
    'bottom': 0,
    'width': '16rem',
    'padding': '2rem 1rem',
    'background-color': 'rgba(120, 120, 120, 0.4)',
}
# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    'margin-left': '18rem',
    'margin-right': '2rem',
    'padding': '2rem 1rem',
}

# create the second page graph
df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

fig = px.scatter(df, x='gdp per capita',
                 y='life expectancy', size='population', color='continent',
                 hover_name='country', log_x=True, size_max=60, template='plotly_dark')
fig.update_layout(
    paper_bgcolor="#272b30",
    plot_bgcolor="#272b30"
)

# setting up the pages and sidebar layouts
home_page = html.Div([
    html.H1('Cool Buttons', className='text-center', style={
        'margin-top': '50px',
        'margin-bottom': '50px',
    }),
    dbc.Button('This button is dangerous', color='danger'),
    dbc.Button('This button not so much', color='warning'),
    dbc.Button('This button is harmless', color='info'),
],
    className='d-grid gap-4 col-4 mx-auto'
)

sidebar = html.Div([
    html.H2('Sidebar', className='display-4'),
    html.Hr(),
    html.P('A simple sidebar layout with navigation links', className='lead'),
    dbc.Nav([
        dbc.NavLink('Home', href='/', active='exact'),
        dbc.NavLink('Second', href='/second', active='exact'),
    ],
        vertical=True,
        pills=True,
    ),
],
    style=SIDEBAR_STYLE,
)

second_page = html.Div([
    html.H1('Second Page', className='text-center', style={
        'margin-top': '50px',
        'margin-bottom': '50px',
    }),
    dcc.Graph(id='life-exp-vs-gdp-graph', figure=fig),
])

content = html.Div(id='page-content', children=[], style=CONTENT_STYLE)

# applying the layouts to the app
app.layout = html.Div([
    dcc.Location(id='url'),
    content,
    sidebar,
])


@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname'))
def render_page_content(pathname):
    if pathname == '/':
        return home_page
    elif pathname == '/second':
        return second_page
    return html.Div([
        html.H4('404: Not found', className='text-danger'),
        html.Hr(),
        html.P(f'The pathname {pathname} was not recognized...')
    ],
        className='p-3 bg-dark rounded-3'
    )

    # run the server
if __name__ == '__main__':
    app.run_server(debug=True)
