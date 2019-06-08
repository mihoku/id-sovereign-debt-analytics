import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv(
    'lender_clusters.csv')

markdown_text = '''
### Notes 
Pembagian *lender* ke dalam 5 kluster berdasarkan hasil analisis menggunakan *elbow method*. 
Pada **kluster 1**, akan didapati *lender* dengan frekuensi pemberian pinjaman kepada pemerintah RI di bawah 70 kali dan besaran nilai komitmen pinjaman rata-rata di bawah USD 1,6 Miliar.
**Kluster 2** diperuntukkan bagi *lender* dengan frekuensi pinjaman kepada pemerintah RI yang juga rendah yakni di bawah 90 kali, namun dengan besaran nilai komitmen pinjaman rata-rata yang sangat tinggi yakni minimal USD 6,4 Miliar. Bank BUMN dalam negeri yakni Bank Mandiri, BNI, dan BRI masuk dalam kluster ini. 
Sementara itu, **kluster 4** adalah *lender* dengan frekuensi pinjaman kepada pemerintah RI yang cukup sering, yaitu 355 komitmen pinjaman ke atas. ada 4 *lender* yang masuk kluster ini, yakni IBRD, JICA, ADB, dan KfW.
Dan **kluster 5 diperuntukkan bagi *lender* dengan frekuensi pinjaman cukup tinggi yakni antara 80-218 komitmen pinjaman dan besaran nilai komitmen pinjaman rata-rata antara USD 8,07 juta hingga 235 miliar. USAID dan OECD masuk dalam kluster ini. 

'''

app.layout = html.Div([
    html.H1('Indonesia Sovereign Debt Analytics'),
    html.Div([
        html.P('Clusters of Sovereign Debt Lenders')
    ]),
    dcc.Graph(
        id='lender-clusters',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['Kluster'] == i]['LOAN_COUNT'],
                    y=df[df['Kluster'] == i]['LOG_LOAN_AVERAGE_AMT_USD'],
                    text=df[df['Kluster'] == i]['LENDER_NAME'],
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