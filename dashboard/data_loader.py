import requests as req

from utils.helpers import read_json, set_env


class JsonDataLoader(object):
    @staticmethod
    def load_jobs():
        all_jobz = read_json("all_jobz")
        return all_jobz

    @staticmethod
    def load_filters_lists(all_jobz):
        all_locations = sorted(list(set([c['location'] for c in all_jobz])))
        all_titles = sorted(list(set([c['title'] for c in all_jobz])))
        all_companies = sorted(list(set([c['company_name'] for c in all_jobz])))
        return all_locations, all_titles, all_companies


class JobsListFilter(object):
    @staticmethod
    def jobs_list_filter(key, condition_values, all_jobz):
        if condition_values:
            filtered_jobz = [jb for jb in all_jobz if jb[key] in condition_values]
        else:
            filtered_jobz = all_jobz

        return filtered_jobz


class DeJobsApiTester(object):
    def __init__(self, test_env=set_env()):
        """
        test_env: (str), 'local' or 'prod'
        """
        self.test_env = test_env
        self.local_base = "http://127.0.0.1:8000/"
        self.prod_base = "https://dejobs-backend.onrender.com/"

    @staticmethod
    def request_builder(request_type, url, data={}):
        if request_type in ["GET", "get", "Get"]:
            resp = req.get(url)
            if resp.status_code == 200:
                data = resp.json()
            else:
                data = 200
                print(f"'GET' request ERROR: {resp.status_code} on  {url}")
        elif request_type in ["POST", "post", "Post"]:
            resp = req.post(url, json=data)
            if resp.status_code != 200:
                print(f"'POST' request ERROR: {resp.status_code} on  {url}")
        return data

    def url_builder(self, route):
        if self.test_env == "prod":
            url = self.prod_base + route
        elif self.test_env == "local":
            url = self.local_base + route
        else:
            url = self.local_base + route
        return url

    def import_companies_list(self):
        url = self.url_builder("companies")
        companies_list = self.request_builder("GET", url)
        return companies_list

    def import_available_jobs(self):
        url = self.url_builder("jobs/available")
        companies_list = self.request_builder("GET", url)
        return companies_list

# dat = DeJobsApiTester(test_env="prod")
# companies_list = dat.import_companies_list()
# pprint(companies_list[:5])
# print("len(companies_list): ", len(companies_list))
