from dash import html
from dash_iconify import DashIconify


class MyButtons(object):
    @staticmethod
    def load_more_jobs_button():
        my_button = html.Button(['Load more jobs',
                                 DashIconify(icon="ion:add-circle-sharp", height=35, style={"color": "white"})
                                 ], id='load_more_jobs', n_clicks=0,
                                style={"text_color": "white", "background-color": "#FE1356", 'display': 'inline-block',
                                       'vertical-align': 'middle', "min-width": "200px",
                                       'height': "45px", "margin-top": "0px", "margin-left": "5px"})
        return my_button

    @staticmethod
    def prev_next():
        prev_next = html.Div(
            [html.Button([DashIconify(icon="uil:angle-double-left", height=30, style={"color": "white"})
                          ], id='previous', n_clicks=0,
                         # style={"background-color": "#FE1356", "height": "70px", "width": "180px"})
                         style={"text_color": "white", "background-color": "#FE1356",
                                'display': 'inline-block',
                                'vertical-align': 'middle', "min-width": "60px",
                                'height': "37px", "margin-top": "0px", "margin-left": "5px"}),
             html.Button([DashIconify(icon="uil:angle-double-right", height=30, style={"color": "white"})
                          ], id='next', n_clicks=0,
                         # style={"background-color": "#FE1356", "height": "70px", "width": "180px"})
                         style={"text_color": "white", "background-color": "#FE1356",
                                'display': 'inline-block',
                                'vertical-align': 'middle', "min-width": "60px",
                                'height': "37px", "margin-top": "0px", "margin-left": "5px"})
             ])
        return prev_next
