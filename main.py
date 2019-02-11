import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from pages import index
from pages import files_page
from pages import db_page
from pages import Home_Page

print(dcc.__version__) # 0.6.0 or above is required

app = dash.Dash()
app.css.append_css({'external_url': 'https://cdn.rawgit.com/plotly/dash-app-stylesheets/2d266c578d2a6e8850ebce48fdb52759b2aef506/stylesheet-oil-and-gas.css'})

app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# Page File_page callback
@app.callback(dash.dependencies.Output('files-source-content', 'children'),
              [dash.dependencies.Input('csv-btn', 'value')])


# Page 2
@app.callback(Output('page-2-content', 'children'),
              [Input('page-2-radios', 'value')])


# Index Page callback
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/files_page':
        return files_page.files_page_layout
    elif pathname == '/db_page':
        return db_page.db_page_layout
    else:
        return Home_Page.HomePage_layout




if __name__ == '__main__':
    app.run_server()
