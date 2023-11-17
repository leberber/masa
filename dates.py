

# print(pprint.pformat( shop_card('product_name', 'product_code', 'product_price',  'product_quantity', 'image_path')))
from dash import Dash, dcc, html, Input, Output, State, ALL,  MATCH, callback, ctx, no_update,   clientside_callback, ClientsideFunction
from dash_iconify import DashIconify as icon
import dash_mantine_components as dmc
# import pprint
from appshell import  header


# from pages.shop import  shop

app = Dash(
    __name__,
    # suppress_callback_exceptions=True,
    external_stylesheets=[
        "https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;900&display=swap"
    ],   
)


# server = app.server






sideBarMenu = html.Div(
    [
        dmc.Drawer(
            closeButtonProps = {'size':'30px',  'color':'dark'},
            title="Drawer Example",
            id="sideBarMenu",
            padding="md",
            zIndex=10000,
            children = [
                  dmc.NavLink(
                      id = 'action-icon',
            label="Home",
            icon=icon(icon="bi:house-door-fill"),
        ),
            ]
        ),
    ]
)

app.layout = html.Div(
    children=[  
        dmc.MantineProvider(
            id = 'theme',
            withGlobalStyles=True,
            children=[
                html.Div(
                    children = [
                        header,
                               
sideBarMenu,
dmc.Text(id="action-output"),
                    ]
                )
            ]
        ) 
    ]
)



clientside_callback(
    ClientsideFunction(
        namespace='clientside',
        function_name='theme_switcher'
    ),
    Output("theme", "theme"),
    Output("theme_switcher", "children"),
    Input("theme_switcher", "n_clicks"),
)





clientside_callback(
    """
    function toggleMenu(n_clicks) {
    console.log(n_clicks)
    return true
        
    }
    """,
    Output("sideBarMenu", "opened"),
    Input("SideBarBurger", "n_clicks"),
    prevent_initial_call=True,
)
 





if __name__ == "__main__":
    app.run_server(debug=True, host='0.0.0.0', port=8050 )

