from shiny import App, render, ui
from shinywidgets import output_widget, render_widget 
import pandas as pd
import plotly.express as px

# Importacion de datos
datos = pd.read_csv(
    filepath_or_buffer = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados?formato=csv",
    sep = ";",
    decimal = ",",
    converters = {"data": lambda x: pd.to_datetime(x, format = "%d/%m/%Y")}
    ).query("data >= '2005-01-01'")


# Interfase de usuario ----
app_ui = ui.page_navbar(
    ui.nav_panel(
        "Gráficos",
        ui.layout_sidebar(
            ui.panel_sidebar("Barra lateral", width=2),
            ui.panel_main(
                ui.row(ui.column(12, ui.output_plot("grafico_estatico"))),
                ui.row(ui.column(12, output_widget("grafico_interactivo")))
                )
        )
        ),
    title = "Visualizacion de datos",
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
    @render_widget
    def grafico_interactivo():
        return px.line(data_frame = datos, y = "valor", x = "data")
         
    
# Dashboars shiny App
app = App(app_ui, server)
