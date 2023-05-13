# Exercises to help you get started with Dash
# as stated here: https://github.com/Coding-with-Adam/Dash-by-Plotly/blob/master/Good_to_Know/Dash2.0/Exercises/Assignments.md
# -----------------------------------------

# Replace the bar chart or choropleth map with a line chart. The x-axis representing the year, the y-axis representing the column_name, and color representing the States. See Plotly docs on the line chart. (When done, see the TEEN BIRTHS PER 1,000 trend in the graph.).


from dash import Dash, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

df = pd.read_csv(
    'https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Good_to_Know/Dash2.0/social_capital.csv')
print(df.head())


app = Dash(__name__, external_stylesheets=[dbc.themes.MATERIA])
title = dcc.Markdown(children='')
figure = dcc.Graph(figure={})
dropdown = dcc.Dropdown(options=df.columns.values[2:],
                        value='Cesarean Delivery Rate',
                        clearable=False)

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([title], style={'text-align': 'center'}, width=12)
    ], justify='center'),
    dbc.Row([
        dbc.Col([dropdown], width=3, style={'margin-top': 50}),
        dbc.Col([figure], width=9)
    ], justify='center')
], fluid=False)


@app.callback(
    Output(figure, component_property='figure'),
    Output(title, component_property='children'),
    Input(dropdown, component_property='value')
)
def update_graph(col_name):
    fig = px.line(df, x='YEAR', y=col_name, color='STATE')
    return fig, '# '+col_name


if __name__ == '__main__':
    app.run_server(debug=True, port=8054)
