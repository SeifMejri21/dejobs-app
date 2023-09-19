import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import html, dcc, Input, dash
from dash_iconify import DashIconify

from dashboard.data_loader import JsonDataLoader, JobsListFilter

jdl = JsonDataLoader()
jdf = JobsListFilter()

all_jobz = jdl.load_jobs()
all_locations, all_titles, all_companies = jdl.load_filters_lists(all_jobz)


def job_card():
    card = dbc.Card(
        [
            dbc.Row(
                [
                    dbc.Col(
                        dbc.CardImg(
                            src="https://assets-global.website-files.com/6364e65656ab107e465325d2/637aeee74d38a6e43415e6b3_vq8xBrkijMAgDZQi0-rEeQIceQhL2PwuO9vYWSU5OQ0.png",
                            className="img-fluid rounded-start", style={"width": "75px"}
                        ),
                        className="col-md-2", style={'marginTop': '5px', 'marginBottom': '5px',
                                                     'marginRight': '5px', 'marginLeft': '10px', }
                    ),
                    dbc.Col(
                        dbc.CardBody(
                            dbc.Row([
                                dbc.Col([html.H4("Data Engineer", className="card-title"),
                                         html.Small(
                                             "Los Angeles",
                                             className="card-text text-muted",
                                             style={'marginTop': '100px', }
                                         ), ],
                                        className="col-md-8"),
                                dbc.Col(html.P("Opensea", className="card-text"),
                                        className="col-md-4", style={"color": "#272626"})
                            ])
                        ),
                        className="col-md-7",
                    ),
                    dbc.Col(
                        dmc.Button(
                            dmc.Anchor("Apply here",
                                       href="https://jobs.ashbyhq.com/OpenSea/66dd92c8-5075-45fb-81f9-8e43a053211a",
                                       target="_blank", style={"textDecoration": "none", "color": "white", }, ),
                            fullWidth=False,
                            rightIcon=html.A(DashIconify(icon="material-symbols:open-in-new",
                                                         style={  # "background-color": "white",
                                                             "color": "white"}
                                                         ),
                                             href="https://jobs.ashbyhq.com/OpenSea/66dd92c8-5075-45fb-81f9-8e43a053211a",
                                             target="_blank"),
                            size="md",
                            style={"background-color": "#FE1356", "height": "50px", "weight": "100px"}
                        ),
                        className="col-md-2",
                    ),
                ],
                className="g-0 d-flex align-items-center",
            )
        ],
        className="mb-3",
        style={"maxWidth": "1100px", "maxHeight": "120px", "background-color": "#DFDFDF"},
    )
    return card


def job_card_dynamic(job_title, company_logo, company_name, location, job_url):
    card = dbc.Card(
        [
            dbc.Row(
                [
                    dbc.Col(
                        dbc.CardImg(
                            src=company_logo,
                            className="img-fluid rounded-start", style={"width": "75px"}
                        ),
                        className="col-md-2", style={'marginTop': '5px', 'marginBottom': '5px',
                                                     'marginRight': '5px', 'marginLeft': '10px', }
                    ),
                    dbc.Col(
                        dbc.CardBody(
                            dbc.Row([
                                dbc.Col([html.H4(job_title, className="card-title"),
                                         html.Small(
                                             location,
                                             className="card-text text-muted",
                                             style={'marginTop': '100px', }
                                         ), ],
                                        className="col-md-8"),
                                dbc.Col(html.P(company_name, className="card-text"),
                                        className="col-md-4", style={"color": "#272626"})
                            ])
                        ),
                        className="col-md-7",
                    ),
                    dbc.Col(
                        dmc.Button(
                            dmc.Anchor("Apply here",
                                       href=job_url,
                                       target="_blank", style={"textDecoration": "none", "color": "white", }, ),
                            fullWidth=False,
                            rightIcon=html.A(DashIconify(icon="material-symbols:open-in-new",
                                                         style={  # "background-color": "white",
                                                             "color": "white"}
                                                         ),
                                             href="job_url",
                                             target="_blank"),
                            size="md",
                            style={"background-color": "#FE1356", "height": "50px", "weight": "100px"}
                        ),
                        className="col-md-2",
                    ),
                ],
                className="g-0 d-flex align-items-center",
            )
        ],
        className="mb-3",
        style={"maxWidth": "1100px", "maxHeight": "120px", "background-color": "#DFDFDF"},
    )
    return card


socials = dmc.Affix(
    dmc.Stack(
        [
            dmc.ActionIcon(
                html.A(
                    DashIconify(icon="mdi:github", width=25),
                    href="https://github.com/SeifMejri21/dejobs",
                    target="_blank",
                    style={"color": "black"},
                ),
            ),
            dmc.ActionIcon(
                html.A(
                    DashIconify(icon="mdi:linkedin", width=25),
                    href="https://www.linkedin.com/in/seif-eddine-mejri-5436b5195/",
                    target="_blank",
                    style={"color": "#0B65C2"},
                ),
            ),
        ],
        spacing="sm",
    ),
    position={"top": 20, "right": 10},
)

version = html.H6("V1.0")
all_jobs_cards = [job_card_dynamic(job_title=c['title'], company_name=c['company'], company_logo=c['company_logo'],
                                    location=c['location'], job_url=c['url']) for c in all_jobz]

front_page_layout = html.Div([
    html.Div(html.A(
        dmc.Image(
            src="https://i.postimg.cc/90fzNFxT/logo.png",
            alt="DeJobs. Logo",
            width=160,
            m=20,
            caption="The best web3 job board",
        ),
        href="https://github.com/SeifMejri21/dejobs",
        target="_blank",
        style={"textDecoration": "none"},
    )),
    html.Div([html.H2("DeJobs. your #1 web3 jobs board")], style={"height": "100px",
                                                                  "text-align": "center"}),
    html.Div([
        dbc.Row([
            dbc.Col([html.H6("Job Title"),
                     # dcc.Input(id="job_title", type="text", placeholder="Junior Data Engineer",
                     #             style={'marginRight': '1px'})
                     dcc.Dropdown(options=all_titles, multi=True, id='job_title')
                     ]),
            dbc.Col([html.H6("Company"),
                     dcc.Dropdown(options=all_companies, multi=True, id='company')]),
            dbc.Col([html.H6("Location"),
                     dcc.Dropdown(options=all_locations, multi=True, id='location')]),
            # dbc.Col(dcc.Checklist(
            #     [{"label": html.Div(['Remote'], style={'color': 'MediumTurqoise', 'font-size': 20}),
            #       "value": "Remote", }, ], value=['Remote'],
            #     labelStyle={"display": "flex", "align-items": "center"},
            # )),
        ]),
    ], style={"margin-left": "35px", "margin-right": "35px", "margin-top": "35px", "margin-bottom": "35px",
              "align": "center"}),
    html.Div(
        # [ job_card4(), ],
        all_jobs_cards,
        style={"margin-left": "55px", "margin-right": "55px", "margin-top": "55px", "margin-bottom": "55px",
               "align": "center", 'display': 'inline-block', 'width': '99%', }),
    socials,
    version,
], style={"margin-left": "25px", "margin-right": "25px", "margin-top": "25px", "margin-bottom": "25px",
          "align": "center"})

app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.BOOTSTRAP],
                suppress_callback_exceptions=True,
                title="DeJobs.",
                update_title="DeJobs. | Loading...",
                assets_folder="assets",
                include_assets_files=True,
                )
server = app.server
app.layout = front_page_layout


@app.callback(
    Input(component_id='job_title', component_property='value'),
    Input(component_id='company', component_property='value'),
    Input(component_id='location', component_property='value'),
    # Output(component_id='data_table1', component_property='data'),
)
def update_jobs_list(job_title, company, location):
    print(job_title, company, location)
    # return all_jobs_cards


if __name__ == "__main__":
    app.run_server(debug=True, port=5000)
