from shiny import App, render, ui
import pandas as pd

# Interfase de usuario ----
app_ui = ui.page_navbar(
    ui.nav_panel(
        "Gráficos",
        ui.layout_sidebar(
            ui.panel_sidebar("Barra lateral", width=2),
            ui.panel_main(
                "Panel de contenido principal",
                ui.row(
                    ui.column(4, "Línea 1, Columna A", style = "background-color: red;"),
                    ui.column(4, "Línea 1, Columna B", style = "background-color: blue;"),
                    ui.column(4, "Línea 1, Columna C", style = "background-color: brown;")
                    ),
                ui.row(
                     ui.column(4, "Línea 2, Columna A", style = "background-color: yellow;"),
                     ui.column(4, "Línea 2, Columna B", style = "background-color: red;"),
                     ui.column(4, "Línea 2, Columna C", style = "background-color: green;"),
                     ),
                style = "background-color: gray;"
                )
        )
        ),
    ui.nav_panel("Página 2"),
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
    ...

  
# Dashboars shiny App
app = App(app_ui, server)
