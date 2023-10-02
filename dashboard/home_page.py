import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import html, dcc

from dashboard.static_components import SOCIALS, VERSION, GOOGLE_ANALYICS
from utils.helpers import set_env

font_size = '1.325rem'
if set_env() == 'prod':
    comp = html.Script(children=[GOOGLE_ANALYICS], id='google-analytics-script')
else:
    comp = html.Div([])

home_page = html.Div([
    html.Div([
        comp,
        html.A(
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
        )]),
    html.Div([html.H2("Elevate Your Crypto Career: 100x More Jobs, One Board")],
             style={"height": "100px", "text-align": "center", "text-color": "pink",
                    "font-family": "Segoe, sans-serif"}),
    html.Center(
        dbc.Nav(
            [
                dbc.NavLink("Board", href="/board", active="exact", style={'font-size': font_size}),
                dbc.NavLink("Search", href="/search", active="exact", style={'font-size': font_size}),
            ],
            pills=True,
            fill=True,
        )
    ),
    dcc.Location(id='chosen_tab'),
    html.Div(children=[], id='returned_tab'),
    SOCIALS,
    VERSION,
], style={"display": "flex", "flex-direction": "column", "margin-left": "25px", "margin-right": "25px",
          "margin-top": "25px", "margin-bottom": "25px", "align": "center"})  # , "maxWidth": "1350px"
