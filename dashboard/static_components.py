import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify

VERSION = html.H6("V1.0")

SOCIALS = dmc.Affix(
    dmc.Stack(
        [
            dmc.ActionIcon(
                html.A(
                    DashIconify(icon="mdi:github", width=25),
                    href="https://github.com/SeifMejri21/dejobs",
                    target="_blank",
                    style={"color": "black"},
                ),
            ),
            dmc.ActionIcon(
                html.A(
                    DashIconify(icon="mdi:linkedin", width=25),
                    href="https://www.linkedin.com/in/seif-eddine-mejri-5436b5195/",
                    target="_blank",
                    style={"color": "#0B65C2"},
                ),
            ),
        ],
        spacing="sm",
    ),
    position={"top": 20, "right": 10},
)


GOOGLE_ANALYICS = """<!DOCTYPE html>
<html>
    <head>
<!-- Google tag (gtag.js) -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-V7B2RT94WN"></script>
        <script>
          window.dataLayer = window.dataLayer || [];
          function gtag(){dataLayer.push(arguments);}
          gtag('js', new Date());
        
          gtag('config', 'G-V7B2RT94WN');
        </script>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
"""