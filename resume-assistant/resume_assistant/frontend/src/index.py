import glob as glob
import dash
import dash_bootstrap_components as dbc
from dash import callback, no_update, dcc, html, Input, Output, State
import flask
from waitress import serve

from resume_assistant.application.dataset.upload import upload_to_gcs

from . import app as home_app


server = flask.Flask(__name__)

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.SLATE,
                          dbc.themes.MATERIA, dbc.icons.FONT_AWESOME],
    server=server
)


index_page = home_app.content

app.title = "ATS Assistant"
app_states = html.Div([
    dcc.Store(id='node-questions', data=[]),
])


app.layout = dbc.Row([
    app_states,
    dcc.Location(id='url', refresh=False),
    dbc.Col([
        dbc.Row([

        ])
    ], width=12, id='page-content'),
])

page_2_layout = html.Div([
    html.H1('Page 2'),
    dcc.RadioItems(['Orange', 'Blue', 'Red'], 'Orange', id='page-2-radios'),
    html.Div(id='page-2-content'),
    html.Br(),
    dcc.Link('Go to Page 1', href='/page-1'),
    html.Br(),
    dcc.Link('Go back to home', href='/')
])


@callback(Output('page-content', 'children'), Input('url', 'pathname'))
def display_page(pathname):
    print("pathname", pathname)
    if pathname == '/home':
        return index_page
    elif pathname == "/page2":
        return page_2_layout
    else:
        return index_page


@app.callback(
    Output('middle', 'value'),
    Input('upload-file', 'contents'),
    State('upload-file', 'filename'),
)
def save_uploaded_file(file_content, filename):

    ctx = dash.callback_context
    if filename and "upload-file" in ctx.triggered[0]["prop_id"]:
        print("filename", filename)
        public_url = upload_to_gcs(filename, file_content)

        return public_url


PORT = str(8066)

if __name__ == '__main__':
    print("start")
    serve(app.server, host='0.0.0.0', port=PORT,
          channel_timeout=500, threads=8)
