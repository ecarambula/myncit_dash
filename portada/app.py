from shiny import ui, App

# Interfase de usuario ----
app_ui = ui.page_navbar(
    ui.nav("Página 1"),
    ui.nav("Página 2"),
    title = ui.row(
        ui.column(3, ui.img(src = "/workspaces/myncit_dash/Data/Mincyt.png")),
        ui.column(9, "PFI 2023")
    )
)


# Servidor ---
def server(input, output, session):
    ...
    
# Dashboars shiny App
app = App(app_ui, server)
