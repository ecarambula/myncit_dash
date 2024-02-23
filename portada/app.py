from shiny import ui, App

# Interfase de usuario ----
app_ui = ui.page_navbar(
    ui.nav_panel("Página 1"),
    ui.nav_panel("Página 2"),
    ui.nav_control(ui.a("MINCyT", href = "https://www.argentina.gob.ar/ciencia")),
    ui.nav_menu(
        "Más",
        ui.nav_control(ui.a("Financiamiento", href = "https://www.argentina.gob.ar/ciencia/financiamiento")),
        ui.nav_control(ui.a("Publicaciones", href = "https://www.argentina.gob.ar/ciencia/publicaciones-cyt"))
        ),
    title = ui.row(
        ui.column(3, ui.img(src = "/workspaces/myncit_dash/portada/Mincyt.png")),
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
