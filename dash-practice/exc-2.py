# Exercises to help you get started with Dash
# as stated here: https://github.com/Coding-with-Adam/Dash-by-Plotly/blob/master/Good_to_Know/Dash2.0/Exercises/Assignments.md
# -----------------------------------------

# Modify the app so it plots a bar graph instead of the choropleth graph. The x-axis should represent states while the y-axis should represent the column_name from the dropdown. See Plotly docs on the bar chart.

from dash import Dash, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

df = pd.read_csv(
    'https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Good_to_Know/Dash2.0/social_capital.csv')
print(df.head())

app = Dash(__name__, external_stylesheets=[dbc.themes.COSMO])
title = dcc.Markdown(children='')
graph = dcc.Graph(figure={})
dropdown = dcc.Dropdown(
    options=df.columns.values[2:],
    value='Cesarean Delivery Rate',
    clearable=False
)

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([title], width=12)
    ], justify='center', style={'text-align': 'center'}),
    dbc.Row([
        dbc.Col([dropdown], width=3, style={'margin-top': 50}),
        dbc.Col([graph], width=9)
    ], justify='center')
], fluid=False)


@app.callback(
    Output(graph, component_property='figure'),
    Output(title, component_property='children'),
    Input(dropdown, component_property='value')
)
def graph_update(col_name):
    fig = px.bar(df, x='STATE', y=col_name, color='YEAR')

    return fig, '# ' + col_name


if __name__ == '__main__':
    app.run_server(debug=True, port=8053)
