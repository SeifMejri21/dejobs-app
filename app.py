import sys

from dash import Input, Output

from dashboard.app_builder import app
from dashboard.board import board
from dashboard.home_page import home_page
from dashboard.html_finder import html_finder


server = app.server
app.layout = home_page


@app.callback(
    Output('returned_tab', 'children'),
    Input("chosen_tab", "pathname")
)
def update_jobs_list(path_name):
    print(f"path_name: {path_name}")
    if path_name == "/board":
        return board
    elif path_name == "/search":
        return html_finder
    else:
        return board


if __name__ == "__main__":
    if sys.platform == 'win32':
        app.run_server(debug=True, port=5000)
    else:
        app.run_server(debug=False)
