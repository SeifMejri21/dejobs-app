from dash import html, Input, Output, dcc

from dashboard.app_builder import app
from dashboard.buttons import MyButtons
from dashboard.data_loader import JsonDataLoader, DeJobsApiTester
from dashboard.filters_components import FiltersComponents
from dashboard.jobs_component import JobsComponent
from dashboard.paginator import Paginator
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

html_finder = html.Div([

    fc.html_fetcher_input(),
    html.H4(id='matches_count'),
    dcc.Loading([
        html.Center(html.Div(id="matches",
                             style={"margin-left": "55px", "margin-right": "55px", "margin-top": "55px",
                                    "margin-bottom": "55px",
                                    "align": "center", 'display': 'inline-block', 'width': '99%', }), ),
    ])

], style={"display": "flex", "flex-direction": "column", "margin-left": "25px", "margin-right": "25px",
          "margin-top": "25px", "margin-bottom": "25px", "align": "center"})  # , "maxWidth": "1350px"


@app.callback(
    Output(component_id='matches', component_property='children'),
    Output(component_id='matches_count', component_property='children'),
    Input(component_id='keywords', component_property='value'),
)
def update_jobs_list(keywords_input):
    if keywords_input:
        keywords = keywords_input.split(',')
        keywords = [k.strip() for k in keywords if k.strip()]
        print("keywords_input: ", keywords_input)
        print("keywords: ", keywords)
        matches = finder.all_companies_patter_finder(custom_companies=not_parsed_companies_list,
                                                     to_match_pattern=keywords,
                                                     print_it=False)
        print("len(matches): ", len(matches))
        matches_divs = jc.matches_cards_positioner(matches, cards_per_row=4)
        matches_count = f"Matches found: {len(matches)}"
    else:
        matches_divs, matches_count = [], f"Matches found: 0"
    return matches_divs, matches_count
