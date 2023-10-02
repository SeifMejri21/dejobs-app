import re
from pprint import pprint

from bs4 import BeautifulSoup
from requests import get

from dashboard.data_loader import DeJobsApiTester
from utils.helpers import open_html, save_html


class HtmlFinderService(object):
    @staticmethod
    def request_maker(url):
        html_content = None
        try:
            resp = get(url)
            if resp.status_code == 200:
                html_content = resp.content
            else:
                print(f"Error {resp.status_code} get request on: {url}")
        except Exception as e:
            print(e, url)
        return html_content

    def get_page_content(self, page_url, file_name="", save_it=True, print_it=False, env='local'):
        html_content = self.request_maker(url=page_url)
        if save_it and file_name and html_content:
            if env == 'local':
                file_path = f"database/hr_html/{file_name}.html"
            else:
                file_path = f"database/hr_html/{file_name}.html"
            save_html(html_content=html_content, file_path=file_path)
        if print_it and html_content:
            pprint(html_content)

    def get_page_content_for_multiple_companies(self, companies_info_list, save_it=True, print_it=False):
        i, leny = 0, len(companies_info_list)
        for c in companies_info_list:
            company_name, company_symbol, careers_page = c['name'], c['symbol'], c['careers_page']
            self.get_page_content(page_url=careers_page, file_name=company_symbol, save_it=save_it, print_it=print_it)
            i += 1
            print(f"{c['name']}, {i}/{leny} Done")

    def create_html_db(self, save_it=True, print_it=False):
        api = DeJobsApiTester()
        companies_info_list = api.import_not_parsed_companies_list()
        print(f"saving careers page html for {len(companies_info_list)} companies")
        self.get_page_content_for_multiple_companies(companies_info_list=companies_info_list, save_it=save_it,
                                                     print_it=print_it)

    @staticmethod
    def find_html(html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        for style in soup(['style', 'link']):
            style.extract()
        cleaned_html = str(soup)
        return cleaned_html

    def html_jobs_finder(self, company_symbol, matching_patters):
        matches = []
        open_file_path = f"C:database/hr_html/{company_symbol}.html"
        html_content = open_html(file_path=open_file_path)
        if html_content:
            html = self.find_html(html_content)
            # cleaned_html = self.find_html(html_content=html)
            for p in matching_patters:
                if re.search(p.lower(), str(html).lower()):
                    matches.append(p)
        return matches

    def html_jobs_finder_for_multiple_companies(self, companies_list=[], matching_patters=[], print_it=False):
        all_companies_matching_reports = []
        for c in companies_list:
            matches = self.html_jobs_finder(company_symbol=c['symbol'], matching_patters=matching_patters)
            matching_report = {"symbol": c['symbol'], "name": c['name'], "matching_pattern": matches,
                               "careers_page": c['careers_page'], "logo": c['logo'], "website": c['website']}
            if matches:
                all_companies_matching_reports.append(matching_report)
                if print_it:
                    pprint(matching_report)
                    print("******************************************************************************************")
        return all_companies_matching_reports

    def all_companies_patter_finder(self, custom_companies=[], to_match_pattern=[], print_it=True):
        if custom_companies:
            companies_info_list = custom_companies
        else:
            companies_info_list = ddl.get_careers_page_for_not_parsed()
        all_companies_matching_report = self.html_jobs_finder_for_multiple_companies(
            companies_list=companies_info_list,
            matching_patters=to_match_pattern, print_it=print_it)
        return all_companies_matching_report
