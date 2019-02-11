import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

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
                             html.A(html.Button('Next',id='data-btn',style={'text-align':'left','margin-left':'89.6%'}),href='/'),

                           ]),
                            html.Div([
                            html.Div([dcc.Dropdown(id='typ-file',options=[{'label':'Csv','value':'csv'},
                                                                          {'label':'Pickle','value':'pkl'},
                                                                          {'label':'Json','value':'json'},
                                                                         {'label':'Excel','value':'xls'}],value='op-li',placeholder='Select file type',
                                                                         style={'margin-left':'1.5%','margin-top':'2.0%','width':'27.0%'})

                                               ],),
                                               html.Div([dcc.Upload(id='brow-fi',children=html.A(html.Button(['Browse']),),),],style={'margin-left':'45.0%'}),
                                               html.Div(html.Label('Or',style={'margin-left':'47.5%','margin-top':'2%'}),),
                                               html.Div([dcc.Upload(id='Drag-Drop',children=html.Div(['Drag & Drop']),),],
                                                            style={'border':'solid',
                                                                  'height':'400px',
                                                                  'margin-left':'1.5%',
                                                                  'margin-right':'1.5%',
                                                                  'text-align':'center',
                                                                  'margin-top':'10%'}),

                                                   ],style={'border':'solid',
                                                             'height':'800px'}),

                         ]),
                 ]),id='files-source-content',
)
