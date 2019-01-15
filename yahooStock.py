import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from pandas_datareader import data as web
from datetime import datetime as dt
import pandas as pd

data = pd.read_csv("stocks.csv", sep=",", dtype="unicode", names=['value', 'label'])

stock_options = []
for i in range(len(data['label'])):
	stock_options.append({'label': data['label'][i], 'value': data['value'][i]})

app = dash.Dash()

app.layout = html.Div([
    html.H1('Yahoo Stock Ticker'),
    dcc.Dropdown(
        id='my-dropdown',
        options= stock_options,
        value = 'KREF'
    ),
    dcc.Graph(id='my-graph')
])

@app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
def update_graph(selected_dropdown_value):
    df = web.DataReader(
        selected_dropdown_value, data_source='yahoo',
        start=dt(2018, 1, 1), end=dt.now())
    return {
        'data': [{
            'x': df.index,
            'y': df.Close
        }]
    }

if __name__ == '__main__':
    app.run_server(port=8000)