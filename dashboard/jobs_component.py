import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify

from utils.helpers import chunkify


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

    @staticmethod
    def custom_search_component(company_logo, company_name, careers_page, website_url, matches):
        str_matches = ""
        for m in matches:
            str_matches += m + ", "
        if str_matches:
            str_matches = str_matches[:-2]
        card = dbc.Card(
            [
                html.A([dbc.CardImg(src=company_logo, top=True, style={"width": "160px"})], href=website_url,
                       target="_blank"),
                dbc.CardBody(
                    [
                        html.H4(company_name, className="card-title"),
                        html.P("Matche(s): " + str_matches, className="card-text", ),
                        dbc.Button("Go to careers Page", href=careers_page,
                                   target='_blank', color="primary"),
                    ]
                ),
            ], outline=True,
            style={"width": "18rem"},
        )
        return card

    def matches_cards_positioner(self, matches_list, cards_per_row=5):
        rows_contents = chunkify(matches_list, chunk_size=cards_per_row)
        matches_cards = []
        for rc in rows_contents:
            row = []
            for c in rc:
                row.append(dbc.Col([self.custom_search_component(company_logo=c["logo"],
                                                                 company_name=c['name'],
                                                                 careers_page=c['careers_page'],
                                                                 website_url=c['website'],
                                                                 matches=c['matching_pattern'])]))
            matches_cards.append(dbc.Row(row))
        return matches_cards

