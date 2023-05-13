# Exercises to help you get started with Dash
# as stated here: https://github.com/Coding-with-Adam/Dash-by-Plotly/blob/master/Good_to_Know/Dash2.0/Exercises/Assignments.md
# -----------------------------------------

'''
Take the app-with-graph.py file. Add an empty Alert Dash Mantine Component to the layout between the markdown and the graph. Insert the Alert component as the second Output in the callback, with children as the component property. Modify the callback function so it returns this string, "The data for the bar graph is highly confidential." if user chooses a bar plot, and it returns this string, "The scatter plot is believed to have been first published in 1833" if user chooses a scatter plot.
'''

from dash import Dash, dcc, Input, Output
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import plotly.express as px

# incorporate data into app
df = px.data.medals_long()

# Build your components
app = Dash(__name__, external_stylesheets=[dbc.themes.COSMO])
mytitle = dcc.Markdown(children="App that analyzes Olympic Medals")
mygraph = dcc.Graph(figure={})
alert = dmc.Alert(children='')
dropdown = dcc.Dropdown(options=['Bar Plot', 'Scatter Plot'],
                        value='Bar Plot',  # initial value displayed when page first loads
                        clearable=False)

# Customize your own Layout
app.layout = dbc.Container([mytitle, dropdown, alert,  mygraph])

# Callback allows components to interact


@app.callback(
    Output(mygraph, component_property="figure"),
    Output(alert, component_property="children"),
    Output(alert, component_property="color"),
    Input(dropdown, component_property="value")
)
# function arguments come from the component property of the Input
def update_graph(user_input):
    if user_input == 'Bar Plot':
        fig = px.bar(data_frame=df, x='nation', y='count', color='medal')
        txt = 'The data for the bar graph is highly confidential.'
        color = 'red'
    elif user_input == 'Scatter Plot':
        fig = px.scatter(df, x='count', y='nation',
                         color='medal', symbol='medal')
        txt = 'The scatter plot is believed to have been first published in 1833'
        color = 'blue'
    # returned objects are assigned to the component property of the Output
    return fig, txt, color


# Run app
if __name__ == '__main__':
    app.run_server(debug=True, port=8053)
