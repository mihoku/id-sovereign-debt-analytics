import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv(
    'ea_clusters.csv')

markdown_text = '''
### Notes 
Pembagian *executing agency* ke dalam 4 kluster berdasarkan hasil analisis menggunakan *elbow method*. 

'''

app.layout = html.Div([
    html.H1('Indonesia Sovereign Debt Analytics'),
    html.Div([
        html.P('Clusters of Sovereign Debt Executing Agency')
    ]),
    dcc.Graph(
        id='ea-clusters',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['Kluster'] == i]['LOAN_COUNT'],
                    y=df[df['Kluster'] == i]['LOG_LOAN_AVG_AMT'],
                    text=df[df['Kluster'] == i]['EA_NAME'],
                    mode='markers',
                    opacity=0.8,
                    marker={
                        'size': 14,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.Kluster.unique()
            ],
            'layout': go.Layout(
                xaxis={'title': 'Count of Loan Commitments'},
                yaxis={'title': 'Average Loan Amount (Log)'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    ),
    dcc.Markdown(children=markdown_text)
])

if __name__ == '__main__':
    app.run_server()