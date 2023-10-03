import random

from dash import html, Input, Output, dcc

from dashboard.app_builder import app
from dashboard.buttons import MyButtons
from dashboard.data_loader import JsonDataLoader, DeJobsApiTester
from dashboard.filters_components import FiltersComponents
from dashboard.jobs_component import JobsComponent
from dashboard.paginator import Paginator
from utils.helpers import set_env

bt = MyButtons()
jc = JobsComponent()
fc = FiltersComponents()
pg = Paginator()
jdl = JsonDataLoader()

dj_api = DeJobsApiTester(test_env=set_env())
# dj_api = DeJobsApiTester(test_env='prod')

all_jobs = dj_api.import_all_available_jobs()
if type(all_jobs) == list:
    random.shuffle(all_jobs)
else:
    all_jobs = []
all_locations, all_titles, all_companies = dj_api.load_jobs_filters()
jobs_count = dj_api.load_available_jobs_count()

not_parsed_companies_list = dj_api.import_not_parsed_companies_list()

board = html.Div([
    fc.input_keyword_filter(),
    html.H5(id='jobs_found'),
    dcc.Loading([
        html.Center(html.Div(id="filtered_jobs",
                             style={"margin-left": "55px", "margin-right": "55px", "margin-top": "55px",
                                    "margin-bottom": "55px",
                                    "align": "center", 'display': 'inline-block', 'width': '99%', }), ),
        html.Center(bt.prev_next()),
    ])
], style={"display": "flex", "flex-direction": "column", "margin-left": "25px", "margin-right": "25px",
          "margin-top": "25px", "margin-bottom": "25px", "align": "center"})

# , "maxWidth": "1350px"

with open('dashboard/assets/google_analytics.hmtl', 'r') as f:
    google_analytics_script = f.read()


@app.callback(
    Output(component_id='filtered_jobs', component_property='children'),
    Output(component_id='jobs_found', component_property='children'),
    Input(component_id='job_title', component_property='value'),
    Input(component_id='company', component_property='value'),
    Input(component_id='location', component_property='value'),
    Input(component_id='previous', component_property='n_clicks'),
    Input(component_id='next', component_property='n_clicks'),
)
def update_jobs_list(job_title, company, location, load_previous, load_next):
    print(job_title, company, location)
    filtered_jobs = fc.regex_mega_filter(all_jobs, job_title, company, location)
    leny = len(filtered_jobs)
    print("filtered jobs", leny)

    items_per_page = 50
    page = load_next - load_previous
    max_page = int(len(filtered_jobs) / items_per_page)
    if page < 0:
        page = 0
    elif page > max_page:
        page = max_page
    print(f"items_per_page: {items_per_page}, page: {page}, max_page: {max_page}, jobs: {len(filtered_jobs)}")

    filtered_jobs = pg.paginator(filtered_jobs, page=page, items_per_age=items_per_page)
    # random.shuffle(filtered_jobs)
    filtered_jobs_cards = [jc.job_card_dynamic(job_title=c['title'], company_name=c['company_name'],
                                               company_logo=c['company_logo'], location=c['location'],
                                               job_url=c['apply_url'], website_url=c['company_website'])
                           for c in filtered_jobs]
    return filtered_jobs_cards, f"Jobs found: {leny}"
