# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

df = []
for i in range(1, 9):
	df.append(pd.read_excel('data/20'+str(i)+".xlsx", index="1차 지필"))
	

data = pd.concat(df)
data.sort_index()
print(data.agg({"이름":'count', '1차 지필':['sum', 'average'], 
	'2차 지필':['sum', 'average'], '수행':['sum', 'average']}))

data['sum'] = data['1차 지필']+data['2차 지필']+data['수행']

data.sort_values(by='sum')
print(data)

'''
data_student = []
for i in range(len(data)):
	temp = {}
	temp['id'] = data[i]['학번']
	temp['name'] = data[i]['이름']
	temp['test1'] = data[i]['1차 지필']
	temp['test2'] = data[i]['2차 지필']
	temp['project'] = data[i]['수행']



app = dash.Dash()

app.layout = html.Div([
	html.H1('Score Table')
	dcc.Dropdown(
			id='student-name',
			options=[

			]
		)


	])
	'''