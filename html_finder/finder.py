import re
from pprint import pprint

from bs4 import BeautifulSoup

from utils.helpers import open_html


class HtmlFinderService(object):
    @staticmethod
    def find_html(html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        for style in soup(['style', 'link']):
            style.extract()
        cleaned_html = str(soup)
        return cleaned_html

    def html_jobs_finder(self, company_symbol, matching_patters):
        matches = []
        open_file_path = f"C:/Users/Administrator/PycharmProjects/dejobs-fetcher/database/hr_html/{company_symbol}.html"
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
                               "careers_page": c['careers_page'], "logo": c['logo'], "website":c['website']}
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
