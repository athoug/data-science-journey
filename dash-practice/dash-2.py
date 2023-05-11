# If you prefer to run the code online instead of on your computer click:
# https://github.com/Coding-with-Adam/Dash-by-Plotly#execute-code-in-browser

from dash import Dash, dcc, Input, Output  # pip install dash
# pip install dash-bootstrap-components
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd                       # pip install pandas

# incorporate data into app
# Source - https://www.cdc.gov/nchs/pressroom/stats_of_the_states.htm
df = pd.read_csv(
    "https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Good_to_Know/Dash2.0/social_capital.csv")
print(df.head())

# Build your components
app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])
mytitle = dcc.Markdown(children="")
mygraph = dcc.Graph(figure={})
dropdown = dcc.Dropdown(options=df.columns.values[2:],
                        value="Cesarean Delivery Rate",  # initial value displayed when page first loads
                        clearable=False)

# Customize your own Layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([mytitle], width=6)
    ], justify='center'),
    dbc.Row([
        dbc.Col([mygraph], width=12)
    ]),
    dbc.Row([
        dbc.Col([dropdown], width=6)
    ], justify='center')
], fluid=False)

# Callback allows components to interact


@app.callback(
    Output(mygraph, component_property='figure'),
    Output(mytitle, component_property='children'),
    Input(dropdown, component_property='value')
)
# function arguments come from the component property of the Input
def update_graph(column_name):
    print(column_name)
    print(type(column_name))
    # https: // plotly.com/python/choropleth-maps/
    fig = px.choropleth(
        data_frame=df,
        locations='STATE',
        locationmode='USA-states',
        scope='usa',
        height=600,
        color=column_name,
        animation_frame='YEAR')

    # returned objects are assigned to the component property of the Output
    return fig, '# '+column_name


# Run app
if __name__ == '__main__':
    app.run_server(debug=True, port=8054)
