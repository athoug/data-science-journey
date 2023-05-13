# Exercises to help you get started with Dash
# as stated here: https://github.com/Coding-with-Adam/Dash-by-Plotly/blob/master/Good_to_Know/Dash2.0/Exercises/Assignments.md
# -----------------------------------------
# Customize the layout so the dropdown and the choropleth graph are next to each other on the page. The total width

# imports
from dash import Dash, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

# data
df = pd.read_csv(
    'https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Good_to_Know/Dash2.0/social_capital.csv')
print(df.head())

# indicate app
app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])

# components
mytitle = dcc.Markdown(children='')
mygraph = dcc.Graph(figure={})
dropdown = dcc.Dropdown(options=df.columns.values[2:],
                        value='Cesarean Delivery Rate',
                        clearable=False
                        )

# layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([mytitle], width=12)
    ], justify='center', style={'text-align': 'center'}),
    dbc.Row([
        dbc.Col([dropdown], width=3),
        dbc.Col([mygraph], width=9),
    ], justify='center', align='center')
], fluid=False)

# callbacks


@app.callback(
    Output(mygraph, component_property='figure'),
    Output(mytitle, component_property='children'),
    Input(dropdown, component_property='value')
)
def graph_update(user_option):
    fig = px.choropleth(data_frame=df,
                        locations='STATE',
                        locationmode='USA-states',
                        scope='usa',
                        height=600,
                        color=user_option,
                        animation_frame='YEAR')
    return fig, '# ' + user_option


# run app
if __name__ == '__main__':
    app.run_server(debug=True, port=8052)
