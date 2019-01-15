# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html

#앞의 dash03에서 math 대신에 numpy를 이용하여 좀더 촘촘한 그래프를 그려 보자. 
import numpy as np


app = dash.Dash()
x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = x * x
y3 = np.cos(x)

app.layout = html.Div(children=[
		html.H1(children=u"Numpy Dash 그래프"),
		dcc.Graph(
			id = 'myGraph',
			figure = {
				'data':[{'x':x, 'y':y1, 'type':'line', 'name':'sin'}, 
						{'x':x, 'y':y2, 'type':'line', 'name':'x*x'}, 
						{'x':x, 'y':y3, 'type':'line', 'name':'cos'}
					],
				'layout':{'title':'Numpy Dash Graph'}

			}
		)
		]

	)

if __name__=='__main__':
	app.run_server(debug=True, port=8030)