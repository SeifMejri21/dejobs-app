import random
import sys

import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import html, Input, dash, Output, dcc

from dashboard.buttons import MyButtons
from dashboard.data_loader import JsonDataLoader, DeJobsApiTester
from dashboard.filters_components import FiltersComponents
from dashboard.jobs_component import JobsComponent
from dashboard.paginator import Paginator
from dashboard.static_components import SOCIALS, VERSION, GOOGLE_ANALYICS
from html_finder.finder import HtmlFinderService
from utils.helpers import set_env

bt = MyButtons()
jc = JobsComponent()
fc = FiltersComponents()
pg = Paginator()
jdl = JsonDataLoader()

finder = HtmlFinderService()

dj_api = DeJobsApiTester(test_env=set_env())
# dj_api = DeJobsApiTester(test_env='local')

not_parsed_companies_list = dj_api.import_not_parsed_companies_list()

front_page_layout = html.Div([
    html.Div([
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
             style={"height": "100px", "text-align": "center", "text-color": "pink"}),
    fc.html_fetcher_input(),
    html.H4(id='matches_count'),
    html.Center(html.Div(id="matches",
                             style={"margin-left": "55px", "margin-right": "55px", "margin-top": "55px",
                                    "margin-bottom": "55px",
                                    "align": "center", 'display': 'inline-block', 'width': '99%', }), ),


    SOCIALS,
    VERSION,
], style={"display": "flex", "flex-direction": "column", "margin-left": "25px", "margin-right": "25px",
          "margin-top": "25px", "margin-bottom": "25px", "align": "center"})  # , "maxWidth": "1350px"

app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.BOOTSTRAP],  # index_string=google_analytics_script,
                suppress_callback_exceptions=True,
                title="DeJobs.",
                update_title="DeJobs. | Loading...",
                assets_folder="assets",
                include_assets_files=True,
                )
app._favicon = "dejobs_icon.png"

server = app.server
app.layout = front_page_layout


# app.index_string = GOOGLE_ANALYICS

@app.callback(
    Output(component_id='matches', component_property='children'),
    Output(component_id='matches_count', component_property='children'),
    Input(component_id='keywords', component_property='value'),
)
def update_jobs_list(keywords_input):
    if keywords_input:
        keywords = keywords_input.split(',')
        matches = finder.all_companies_patter_finder(custom_companies=not_parsed_companies_list, to_match_pattern=keywords,
                                                     print_it=False)
        matches_divs = fc.matches_component(matches)
        matches_count = f"Matches found: {len(matches)}"
    else:
        matches_divs, matches_count = [], f"Matches found: 0"
    return matches_divs, matches_count


if __name__ == "__main__":
    if sys.platform == 'win32':
        app.run_server(debug=True, port=5000)
    else:
        app.run_server(debug=False)
