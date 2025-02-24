import glob as glob
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import flask


server = flask.Flask(__name__)
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.SLATE,
                          dbc.themes.MATERIA, dbc.icons.FONT_AWESOME],
    server=server
)


app.title = "Beyond Abstracts"
title = app.title

main_content = dbc.Card(
    children=dbc.CardBody([
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col([
                                dbc.Card([
                                    dbc.CardBody([
                                        html.H5("ATS Assistant"),
                                        dcc.Input(
                                            id="left",
                                            type="url",
                                        ),
                                        dcc.Upload([
                                            'Drag and Drop or ',
                                            html.A('Upload your resume')
                                        ], id="upload-file",
                                            style={
                                            'width': '100%',
                                            'height': '100%',
                                            'lineHeight': '100%',
                                            'borderWidth': '100%',
                                            'borderStyle': 'dashed',
                                            'borderRadius': '1%',
                                            'textAlign': 'center'
                                        }),
                                    ]),
                                ], className="main-card"),
                            ], width=3, className=""),
                            dbc.Col([
                                dbc.Card([
                                    dbc.CardBody([
                                        html.H5("Resume Content"),
                                        dcc.Textarea(
                                            id="right",
                                            className="mb-3",
                                            style={"height": "80%"},
                                            value="",
                                        ),
                                    ]),
                                ], className="main-card"),], width=9, className=""),
                        ]),
                    ]),
                ]),
            ]),
        ]),
    ], style={"background-color": "#07141F"})
)


content = html.Div([html.H1(id='page-title', style={'padding-left': '1%', 'padding-top': '1%'}),
                    html.Div([html.Div([main_content], style={'padding': '1% !important', 'width': '100%'}),])],
                   className='app-content-div',
                   )


app.layout = html.Div(
    [
        # dcc.Store(id='timestamp', storage_type='memory', data=timestamp),
        dbc.Row([
            dbc.Col([
                html.Div(
                    [
                        dash.page_container,
                        main_content
                    ],
                    className="content",
                ),
            ], width=12)
        ],
            style={"background-color": "#07141F"})
    ])
