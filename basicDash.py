# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash()

app.layout = html.Div(style = {'backgroundColor':'gray'},
	children=[
		html.H1(children='Hello Dash', style={'color':'pink'}),	
		html.Div(children='Dash: Soori Application'),
		dcc.Graph(
			id='exgraph',
			figure={
				'data':[
						{'x':[1, 2, 3], 'y':[4, 1, 2], 'type':'line', 'name':'SF'},
						{'x':[1, 2, 3], 'y':[2, 4, 5], 'type':'line', 'name':u'Montréal'}
					],
				'layout':{'title': 'Dash Data', 'paper_bgcolor':'pink'}
			}
	)])

if __name__ == '__main__':
	app.run_server(port=8080)

