from utils.helpers import chunkify


class Paginator(object):
    @staticmethod
    def paginator(jobs_list, page, items_per_age=50):
        chunked_jobs_list = chunkify(jobs_list, chunk_size=items_per_age)
        return chunked_jobs_list[page]
