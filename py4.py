# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
	[	html.Label(),
		dcc.Dropdown(),

		html.Label(),
		dcc.Dropdown(),


		html.Label(),
		dcc.RadioItems(),

		html.Label(),
		dcc.CheckList(),

		html.Label(),
		dcc.Input(),

		html.Label(),
		dcc.Slider(),
	], style={'columnCount': 2}
)

if __name__ == "__main__":
	app.run_server(port=8040)