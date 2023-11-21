import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify as icon
from utils import id_dict

footer_icon_with = 30
footer_icon_color = '#A519C7'

header = dmc.Paper(
className = 'header',
shadow='xs',
children =[
    dmc.Grid(
        gutter="xl",
        children=[
            dmc.Col(
                span=2,
                children=[
                    html.Div(
                        style = {'display': 'flex'},
                        children = [
                            dmc.Button(
                                          
                                                variant="transparent",
                                                id="SideBarBurger",
                                                leftIcon= icon(icon="iconamoon:menu-burger-horizontal", width=30),
                                                rightIcon= dmc.Image(src="/assets/masa_logo.svg", width=70, ml = '-18px' ),
                                                
                                            ),

                 
                        ]       
                    )
                ]
            ),

            dmc.Col(
                span=2, offset=8,
               
                children=[
                    html.Div(       
                        dmc.ActionIcon(
                            id = 'theme_switcher',
                            style = {'float': 'right'},
                            n_clicks=0, 
                            variant= "transparent",
                         
                            children = [
                                icon(icon="ic:baseline-light-mode", width=40, color='gold')
                            ]
                        )
                    )
                ]
            )
        ]  
    )
])

