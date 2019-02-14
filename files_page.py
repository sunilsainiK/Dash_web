import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import base64
import io
import pandas as  pd
import dash_table
import datetime
import requests
import json
from main import app, server
files_page_layout = html.Div(
                       html.Div([
                         html.Div([html.H1(children='Industrial Event Log Analysis',style={
                                                                                   'padding-left': '2.0%',
                                                                                   'padding-right': '2.0%',
                                                                                   'border':'solid',
                                                                                   'background-color':'DodgerBlue',
                                                                                   'text-align':'center'                                                                                  }
                      ),
                           html.Div([
                              html.H2(children='Source Files',style={'padding-left': '2.0%',
                                                                'padding-right': '2.0%',
                                                                 'margin-top':'2%',
                                                                 'border':'solid',
                                                                 'background-color':'DodgerBlue',
                                                                 'text-align':'center'
                                                                                }),

                             html.A(html.Button('Back',id='b-btn',style={'text-align':'left'}),href='/'),
                             html.A(html.Button('Next',id='data-btn',style={'text-align':'left','margin-left':'89.6%'},type='submit',formAction='post'),href='/api_call'),

                               ]),html.Hr(),


                           html.Div([
                            html.Div([dcc.Dropdown(id='typ-file',options=[{'label':'Csv','value':'csv'},
                                                                         {'label':'Pickle','value':'pkl'},
                                                                         {'label':'Json','value':'json'},
                                                                        {'label':'Excel','value':'xls'}],value='op-li',placeholder='Select file type',
                                                                        style={'margin-left':'1.5%','margin-top':'2.0%','width':'27.0%'})

                                   ],),
                                    html.Div([dcc.Upload(id='upload-data',children=html.Div([(html.Button('Upload File'))],style={'margin-left':'45.0%'})),
                                          html.Hr(),
                                          html.Hr(),
                                          html.Hr(),
                                                dcc.Upload(['Drag and Drop or ',html.A('Select a File')],
                                                    style={'width': '100%',
                                                          'height': '60px',
                                                          'lineHeight': '60px',
                                                          'borderWidth': '1px',
                                                          'borderStyle': 'dashed',
                                                          'borderRadius': '5px',
                                                          'textAlign': 'center'}),html.Div(id='output-data-upload'),
                                                          ]),

                               ],style={'border':'solid',
                                         'height':'600px'}),

                         ]),
                 ]),id='files-source-content',
)


@app.callback(Output('output-data-upload', 'children'),
              [Input('upload-data', 'contents')],
              [State('upload-data', 'filename'),
               State('upload-data', 'last_modified')])

def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_names is not None:
        content_type, content_string = list_of_contents.split(',')
        global df
        data = base64.b64decode(content_string)
        df = pd.read_csv(io.StringIO(data.decode('utf-8')))

        return ([list_of_names,list_of_dates])


@server.route("/data_to_flask",methods=['GET'])
def pp():
    return (df.to_json(orient='records'))
