# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash App'),

    html.Div(className='row', children=[

        html.Div(className='row', children='''
            Dash: A web application framework for Python.
        '''),

        dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [1, 2, 3], 'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [3, 2, 1], 'type': 'bar', 'name': u'Montréal'},
                ],
                'layout': {
                    'title': 'Dash Data Visualization'
                }
            }
        )
    ]),
    html.Div(className='row', children=[

        html.Div(className='row', children='''
        Dash: A web application framework for Python.
    '''),

        dcc.Graph(
            id='example-graph2',
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [2,4, 6], 'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [4, 1, 3], 'type': 'bar', 'name': u'Montréal'},
                ],
                'layout': {
                    'title': 'Dash Data Visualization'
                }
            }
        )
    ]),
    html.Div(className='row', children=[

        html.Div(className='row', children='''
    Dash: A web application framework for Python.
'''),

        dcc.Graph(
            id='example-graph3',
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [2, 5, 4], 'type': 'line', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [5, 2, 6], 'type': 'bar', 'name': u'Montréal'},
                ],
                'layout': {
                    'title': 'Dash Data Visualization'
                }
            }
        )
    ])

])

if __name__ == '__main__':
    app.run_server(debug=True)