import sys

import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import html, dcc, Input, dash, Output

from dashboard.buttons import MyButtons
from dashboard.jobs_component import JobsComponent
from dashboard.data_loader import JsonDataLoader, JobsListFilter, DeJobsApiTester
from dashboard.static_components import SOCIALS, VERSION

bt = MyButtons()
jc = JobsComponent()
jdl = JsonDataLoader()
jlf = JobsListFilter()
dj_api = DeJobsApiTester()

start_jobs = dj_api.import_available_jobs(page=1, items=50)
all_locations, all_titles, all_companies = dj_api.load_jobs_filters()
jobs_count = dj_api.load_available_jobs_count()

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
    html.Div([html.H2("Elevate Your Crypto Career: 100x More Jobs, One Board")],
             style={"height": "100px", "text-align": "center", "text-color": "pink"}),
    html.Div([
        dbc.Row([
            dbc.Col([html.H6("Job Title"),
                     # dcc.Input(id="job_title", type="text", placeholder="Junior Data Engineer",
                     #             style={'marginRight': '1px'})
                     dcc.Dropdown(options=all_titles, multi=True, clearable=False,
                                  id='job_title')
                     ]),
            dbc.Col([html.H6("Company"),
                     dcc.Dropdown(options=all_companies, multi=True, id='company')]),
            dbc.Col([html.H6("Location"),
                     dcc.Dropdown(options=all_locations, multi=True, id='location')]),
        ]),
    ], style={"margin-left": "35px", "margin-right": "35px", "margin-top": "35px", "margin-bottom": "35px",
              "align": "center"}),
    # html.Hr(),
    html.Center(html.Div(id="filtered_jobs",
                         style={"margin-left": "55px", "margin-right": "55px", "margin-top": "55px",
                                "margin-bottom": "55px",
                                "align": "center", 'display': 'inline-block', 'width': '99%', }), ),
    # html.Center(bt.load_more_jobs_button()),
    # html.Hr(),
    html.Center(bt.prev_next()),
    SOCIALS,
    VERSION,
], style={"display": "flex", "flex-direction": "column", "margin-left": "25px", "margin-right": "25px",
          "margin-top": "25px", "margin-bottom": "25px", "align": "center"})  # , "maxWidth": "1350px"

app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.BOOTSTRAP],
                suppress_callback_exceptions=True,
                title="DeJobs.",
                update_title="DeJobs. | Loading...",
                assets_folder="assets",
                include_assets_files=True,
                )
app._favicon = "dejobs_icon.png"

server = app.server
app.layout = front_page_layout


@app.callback(
    Output(component_id='filtered_jobs', component_property='children'),
    Input(component_id='job_title', component_property='value'),
    Input(component_id='company', component_property='value'),
    Input(component_id='location', component_property='value'),
    Input(component_id='previous', component_property='n_clicks'),
    Input(component_id='next', component_property='n_clicks'),
)
def update_jobs_list(job_title, company, location, load_previous, load_next):
    page = load_next - load_previous + 1
    max_page = int(jobs_count/50)+1
    if page < 1:
        page = 1
    elif page > max_page:
        page = max_page
    print(load_previous, load_next, page)
    # filtered_jobs = jlf.jobs_list_filter(key="title", condition_values=job_title, all_jobz=all_jobz)
    # filtered_jobs = jlf.jobs_list_filter(key="company_name", condition_values=company, all_jobz=filtered_jobs)
    # filtered_jobs = jlf.jobs_list_filter(key="location", condition_values=location, all_jobz=filtered_jobs)
    filtered_jobs = dj_api.import_available_jobs(page=page, items=50)
    # filtered_jobs = list_flatter(filtered_jobs.append(new_jobs))
    filtered_jobs_cards = [jc.job_card_dynamic(job_title=c['title'], company_name=c['company_name'],
                                               company_logo=c['company_logo'], location=c['location'],
                                               job_url=c['apply_url'], website_url=c['company_website'])
                           for c in filtered_jobs]
    return filtered_jobs_cards


if __name__ == "__main__":
    if sys.platform == 'win32':
        app.run_server(debug=True, port=5000)
    else:
        app.run_server(debug=False)
