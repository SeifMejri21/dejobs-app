from utils.helpers import read_json


class JsonDataLoader(object):
    @staticmethod
    def load_jobs():
        all_jobz = read_json("all_jobz")
        return all_jobz

    @staticmethod
    def load_filters_lists(all_jobz):
        all_locations = sorted(list(set([c['location'] for c in all_jobz])))
        all_titles = sorted(list(set([c['title'] for c in all_jobz])))
        all_companies = sorted(list(set([c['company'] for c in all_jobz])))
        return all_locations, all_titles, all_companies


class JobsListFilter(object):
    @staticmethod
    def jobs_list_filter(key, condition_values, all_jobz):
        if condition_values:
            filtered_jobz = [jb for jb in all_jobz if jb[key] in condition_values]
        else:
            filtered_jobz = all_jobz
        # print("len(all_jobz): ", len(all_jobz))
        # print("len(filtered_jobz):", len(filtered_jobz))
        return filtered_jobz
