# Tengo que instalar:
    # pip install --upgrade pip wheel
    # pip install shiny shinywidgets plotly itables shinyswatch plotnine openpyxl scikit-misc
    # pip install python-bcb        banco central do Brasil
# y la extension de shiny para python...


# Importa bibliotecas
from pathlib import Path

from shiny import App, render, ui
from shinywidgets import output_widget, render_widget 
from itables.shiny import DT
from plotnine.data import economics
from bcb import currency

import plotnine as p9
import pandas as pd
import plotly.express as px
import shinyswatch

# here = Path(__file__).parent


# Importacion de datos
datos = pd.read_csv(
    filepath_or_buffer = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados?formato=csv",
    sep = ";",
    decimal = ",",
    converters = {"data": lambda x: pd.to_datetime(x, format = "%d/%m/%Y")}
    ).query("data >= '2005-01-01'").assign(variac_pct = lambda x: ((x.valor / x.valor.shift(1))-1)*100)

datos_mincyt = pd.read_excel("/workspaces/myncit_dash/dinamica/www/BD_PFI23.xlsx")


datos_economics = economics
datos_economics.columns[1:len(datos_economics)]
datos_economics.columns.tolist()[1:len(datos_economics)]

# Interfase de usuario ----
app_ui = ui.page_navbar(
    shinyswatch.theme.cerulean(),
    ui.nav_panel(
        "Gráficos",
        ui.layout_sidebar(
            ui.panel_sidebar(
                ui.input_select(
                    id = "boton_variable",
                    label = ui.tags.strong("Seleccione una variable:"),
                    choices = datos_economics.columns.tolist()[1:len(datos_economics)],
                    selected = datos_economics.columns.tolist()[1]
                )
            ),
                
            ui.panel_main(
                "Panel de contenido principal",
                ui.row(
                    ui.column(4, "Línea 1, Gráfico estático", ui.output_plot("grafico_estatico"), style = "background-color: red;"),
                    ui.column(4, "Línea 1, Gráfico interactivo", output_widget("grafico_interactivo"), style = "background-color: blue;"),
                    ui.column(4, "Línea 1, Gráfico REACTIVO", ui.output_plot("grafico_reactivo"), style = "background-color: brown;")
                    ),
                ui.row(
                     ui.column(4, "Línea 2, Tábla estática", ui.output_table("tabla_estatica"), style = "background-color: yellow;"),
                     ui.column(4, "Línea 2, Tábla interactiva", ui.HTML(DT(datos.tail(10))), style = "background-color: red;"),
                     ui.column(4, "Línea 2, Tábla REACTIVA", ui.output_data_frame("tabla_reactiva"), style = "background-color: green;"),
                     ),
                style = "background-color: gray;"
                )
        )
        ),
    ui.nav_panel(
        "Monedas",
        ui.layout_sidebar(
            ui.panel_sidebar(
                ui.input_select(
                    id = "moneda",
                    label = "Moneda:",
                    choices = currency.get_currency_list().symbol.sort_values().tolist()[2:]
                )
            ),
            ui.panel_mail()
     
     ),






    ui.nav_control(ui.a("MINCyT", href = "https://www.argentina.gob.ar/ciencia")),
    ui.nav_menu(
        "Más",
        ui.nav_control(ui.a("Financiamiento", href = "https://www.argentina.gob.ar/ciencia/financiamiento")),
        ui.nav_control(ui.a("Publicaciones", href = "https://www.argentina.gob.ar/ciencia/publicaciones-cyt"))
        ),
    title = ui.row(
        ui.column(3, ui.img(src = "Mincyt.png")),
        ui.column(9, "PFI 2023")
    ),
    bg = "blue",
    inverse = True
)


# Servidor ---
def server(input, output, session):
    @output
    @render.plot
    def grafico_estatico():
        return datos.plot(y = "valor", x = "data", kind  = "line")
    
    @output
    @render_widget # type: ignore
    def grafico_interactivo():
        return px.line(data_frame= datos, y = "valor", x = "data")
 
    @output
    @render.table
    def tabla_estatica():
        return datos.tail(10)
    
    @output
    @render.plot
    def grafico_reactivo():
        return (
            p9.ggplot(datos_economics) +
            p9.aes(x = "date", y = "unemploy") +
            p9.geom_point() +
            p9.geom_smooth(method ="loess", se = True)
        ) 

    @output
    @render.data_frame
    def tabla_reactiva():
        return (
            datos_economics
            .assign(date = lambda x: x.date.astype(str))
            .filter(items = ["date", "unemploy"], axis = "columns")
        )


# Dashboars shiny App
www_dir = Path(__file__).parent / "www"
app = App(app_ui, server, static_assets=www_dir)
