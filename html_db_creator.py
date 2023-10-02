from html_finder.finder import HtmlFinderService

finder_service = HtmlFinderService()

save_it = True
print_it = False


finder_service.create_html_db(save_it=save_it, print_it=print_it)