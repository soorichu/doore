import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
		html.H1("DASH 프로그램"),
		html.P("편리하게 데이터를 시각화할 수 있습니다.")

	])

app.run_server(port=8000)