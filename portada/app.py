from shiny import ui, App

# Interfase de usuario ----
app_ui = ui.page_navbar(
    ui.nav("Página 1"),
    ui.nav("Página 2"),
    title = ui.row(
        ui.column(3, ui.img(src = "https://aluno.analisemacro.com.br/wp-content/uploads/dlm_uploads/2023/05/logo_am_45.png")),
        ui.column(9, "PFI 2023")
    )
)


# Servidor ---
def server(input, output, session):
    ...
    
# Dashboars shiny App
app = App(app_ui, server)
