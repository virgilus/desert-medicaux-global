import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

import numpy as np
import pandas as pd



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

df = pd.read_csv('departements_et_regions.csv',
                                sep=',',
                                header='infer',
                                quotechar='"',
                                encoding='UTF-8',)



taux_par_hab_specialites = ['population', 'indice', 'generaliste_habitant', 'infirmiers_habitant',
       'hopital_habitant', 'ambulance_habitant', 'analyse_medicale_habitant',
       'autre_habitant', 'autre_specialiste_habitant', 'chirurgien_habitant',
       'dentiste_habitant', 'organe_habitant', 'radiologue_habitant',
       'reeducateur_podologue_habitant',]


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    html.H2(children='Dashboard - Déserts Médicaux'),
    html.Div([

        html.Div([

            dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value': i} for i in taux_par_hab_specialites],
                
            ),
 
        ],
        style={'width': '48%', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown(
                id='yaxis-column',
                options=[{'label': i, 'value': i} for i in taux_par_hab_specialites],
                
            ),
   
        ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),

    dcc.Graph(id='indicator-graphic'),

    dcc.Graph(
            id='bar-chart',
            figure={
                'data': [
                    {'x': df['nom_dept'], 'y': df['indice'], 'type': 'bar', 'name': 'Indice'},
                   
                ],
                'layout': {
                    'title': 'Histogrammes des indices'
                }
            }
        ),
    

  

])

@app.callback(
    Output('indicator-graphic', 'figure'),
    [Input('xaxis-column', 'value'),
     Input('yaxis-column', 'value'),])

def update_graph(xaxis_column_name, yaxis_column_name):

    return {
        'data': [go.Scatter(
            x=df[df['nom_region'] == i][xaxis_column_name],
            y=df[df['nom_region'] == i][yaxis_column_name],
            text=df['nom_dept'],
            mode='markers',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            },
            name=i
         ) for i in df['nom_region'].unique()
        
        
        ],
        'layout': go.Layout(
            xaxis={
                'title': xaxis_column_name,
                
            },
            yaxis={
                'title': yaxis_column_name,
                
            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }


if __name__ == '__main__':
    app.run_server(debug=True)