# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
import math


app = dash.Dash()
x = [i for i in range(10)]
y1 = [math.sin(i) for i in x]
y2 = [i*i for i in x]
y3 = [math.cos(i) for i in x]

app.layout = html.Div(children=[
		html.H1(children=u"Dash 그래프"),
		dcc.Graph(
			id = 'myGraph',
			figure = {
				'data':[{'x':x, 'y':y1, 'type':'line', 'name':'sin'}, 
						{'x':x, 'y':y2, 'type':'line', 'name':'x*x'}, 
						{'x':x, 'y':y3, 'type':'line', 'name':'cos'}
					],
				'layout':{'title':'Dash Graph'}

			}
		)
		]

	)

if __name__=='__main__':
	app.run_server(debug=True, port=8020)