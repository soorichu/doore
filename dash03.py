import plotly 
plotly.tools.set_credentials_file(username='soori', api_key='z9uI3X4Ty8U33hrdPvv5')

import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

num_of_points = 20
random_array = np.random.random((num_of_points))

trace1 = go.Scatter(
	x = [j for j in range(len(random_array))],
	y = random_array,
	mode = 'markers',
	marker = dict(size=15, color=random_array, colorscale="Viridis"),
	name='Radom Array'
	)

py.iplot([trace1], filename='numpy-random')
