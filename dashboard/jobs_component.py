import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify


class JobsComponent(object):
    @staticmethod
    def job_card_dynamic(job_title, company_logo, company_name, location, job_url, website_url):
        card = dbc.Card(
            [
                dbc.Row(
                    [
                        dbc.Col(html.A([dbc.CardImg(
                            src=company_logo,
                            className="img-fluid rounded-start", style={"width": "75px"}
                        )], href=website_url, target="_blank")
                            ,
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
                                                 href=job_url,
                                                 target="_blank"),
                                size="md",
                                style={"background-color": "#FE1356", "height": "55px", "width": "150px"}
                            ),
                            className="col-md-2",
                        ),
                    ],
                    className="g-0 d-flex align-items-center",
                )
            ],
            className="mb-3",
            style={"maxWidth": "1150px", "maxHeight": "120px", "background-color": "#DFDFDF"},
        )
        return card
