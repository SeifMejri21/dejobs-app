import re

import dash_bootstrap_components as dbc
from dash import html, dcc


class FiltersComponents(object):
    @staticmethod
    def jobs_list_filter(key, condition_values, all_jobz):
        if condition_values:
            filtered_jobz = [jb for jb in all_jobz if jb[key] in condition_values]
        else:
            filtered_jobz = all_jobz

        return filtered_jobz

    @staticmethod
    def dropdown_filter(all_titles, all_companies, all_locations):
        filters = html.Div([
            dbc.Row([
                dbc.Col([html.H6("Job Title"),
                         dcc.Dropdown(options=all_titles, multi=True, clearable=False,
                                      id='job_title')
                         ]),
                dbc.Col([html.H6("Company"),
                         dcc.Dropdown(options=all_companies, multi=True, id='company')]),
                dbc.Col([html.H6("Location"),
                         dcc.Dropdown(options=all_locations, multi=True, id='location')]),
            ]),
        ], style={"margin-left": "35px", "margin-right": "35px", "margin-top": "35px", "margin-bottom": "35px",
                  "align": "center"})
        return filters

    @staticmethod
    def regex_based_filter(data, key, value):
        filtered_data = []
        splitted_value = value.split(' ')
        leny = len(splitted_value)
        for d in data:
            splitted_data = d[key].split(' ')
            matched = []
            for sd in splitted_data:
                sd_lower = sd.lower()
                for sv in splitted_value:
                    sv_lower = sv.lower()
                    if re.search(sv_lower, sd_lower):
                        # if re.search(sd_lower, sv_lower):
                        matched.append(sv_lower)
            if len(matched) == leny:
                filtered_data.append(d)
        return filtered_data

    def regex_mega_filter(self, all_jobs, job_title, company, location):
        if job_title:
            filtered_jobs = self.regex_based_filter(all_jobs, "title", job_title)
            if company:
                filtered_jobs = self.regex_based_filter(filtered_jobs, "company_name", company)
            if location:
                filtered_jobs = self.regex_based_filter(filtered_jobs, "location", location)
        else:
            if company:
                filtered_jobs = self.regex_based_filter(all_jobs, "company_name", company)
                if location:
                    filtered_jobs = self.regex_based_filter(filtered_jobs, "location", location)

            else:
                if location:
                    filtered_jobs = self.regex_based_filter(all_jobs, "location", location)
                else:
                    filtered_jobs = all_jobs
        return filtered_jobs

    @staticmethod
    def input_keyword_filter():
        filters = html.Div([
            dbc.Row([
                dbc.Col([html.H6("Job Title"),
                         dcc.Input(placeholder="Data Engineer", type='text', id='job_title', debounce=True)]),
                dbc.Col([html.H6("Company"),
                         dcc.Input(placeholder="Binance", type='text', id='company', debounce=True)]),
                dbc.Col([html.H6("Location"),
                         dcc.Input(placeholder="Tunis", type='text', id='location', debounce=True)]),
            ]),
        ], style={"margin-left": "35px", "margin-right": "35px", "margin-top": "35px", "margin-bottom": "35px",
                  "align": "center"})
        return filters

    @staticmethod
    def html_fetcher_input():
        filters = html.Div([
            dbc.Row([html.H6("Enter keywords, separate them by comma: a','"),
                     dcc.Input(placeholder="Data Engineer", type='text', id='keywords', debounce=True,
                               style={"height": "30px", "width": "250px"}
                               )]),
        ], style={"margin-left": "35px", "margin-right": "35px", "margin-top": "35px", "margin-bottom": "35px",
                  "align": "center"})
        return filters

    @staticmethod
    def matches_component(matches_list):
        matches = []
        for m in matches_list:
            matches.append(html.Div([html.H4(f"{m['name']} matched with: {m['matching_pattern']}"),
                                    dcc.Link(children="Open Careers Page", href=m["careers_page"],target="_blank"),
                                    html.Hr()]))
        return matches
