# Exercises to help you get started with Dash
# as stated here: https://github.com/Coding-with-Adam/Dash-by-Plotly/blob/master/Good_to_Know/Dash2.0/Exercises/Assignments.md
# -----------------------------------------

'''
Take the interactive-app.py file. Add a radioItems Dash Core Component to the layout after assigning the following colors to its options property: ['blue','red','green']. Incorporate the RadioItems component into the callback so the button/color chosen updates the color of the markdown text. Hint - the callback will have a total of 2 Outputs and 2 Inputs. To color the Markdown text in purple, its style property is written like this: dcc.Markdown(style={'color':'purple'})
'''

from dash import Dash, dcc, Input, Output
import dash_bootstrap_components as dbc


# Build your components
app = Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])
mytext = dcc.Markdown(children="", style={})
myinput = dbc.Input(value="# Hello world - Let's build web apps in Python!")
radio = dbc.RadioItems(['blue', 'red', 'green'])

# Customize your own Layout
app.layout = dbc.Container([mytext, myinput, radio])


# Callback allows components to interact
@app.callback(
    Output(mytext, component_property='children'),
    Output(mytext, component_property='style'),
    Input(radio, component_property='value'),
    Input(myinput, component_property='value')
)
# function arguments come from the component property of the Input
def update_title(color, user_input):
    print(color)
    print(user_input)
    # returned objects are assigned to the component property of the Output
    return user_input, {'color': color}


# Run app
if __name__ == "__main__":
    app.run_server(debug=True, port=8052)
