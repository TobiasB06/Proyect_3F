import flet as ft

def main(ventana1: ft.Page):
    ventana1.title = "Inicio de sesión"
    ventana1.window.width = 400
    ventana1.window.height = 600  
    ventana1.window.resizable = False
    ventana1.window.maximized = True 
    ventana1.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    ventana1.vertical_alignment = ft.MainAxisAlignment.CENTER
    ventana1.bgcolor = ft.colors.WHITE10

    password_visible = False

    # Función para alternar el estado de visibilidad de la contraseña
    def toggle_password_visibility(e):
        nonlocal password_visible
        password_visible = not password_visible
        contra_txt.content.controls[1].password = not password_visible
        contra_txt.content.controls[2].name = ft.icons.VISIBILITY_OFF if password_visible else ft.icons.VISIBILITY
        contra_txt.content.controls[2].update()
        contra_txt.content.controls[1].update()
    
    logo = ft.Container(
        content=ft.Image(
            src="Imagenes/IMG-3F.jpeg",
            width=100,
            height=100,
        ),
        margin=ft.Margin(left=133, bottom=0, right=0, top=0) 
    )
    
    ini = ft.Container(
        content=ft.Text(
            "Inicio de sesión\nMunicipalidad Tres De Febrero",
            size=16,
            text_align=ft.TextAlign.CENTER,
            color=ft.colors.WHITE,
        ),
        margin=ft.Margin(left=75, bottom=0, right=0, top=0)
    )
    
    # Variable para el estado de visibilidad de la contraseña
    
    
    # Campo de texto de usuario con icono en una fila (Row)
    us_txt = ft.Container(
        content=ft.Row(
            controls=[
                ft.Icon(name=ft.icons.PERSON, color=ft.colors.ORANGE),  # Icono de usuario en naranja
                ft.TextField(
                    label="Usuario",
                    width=350,
                    label_style=ft.TextStyle(color=ft.colors.WHITE),  # Texto blanco
                    border=ft.InputBorder.NONE  # Sin bordes
                ),
            ],
            alignment=ft.MainAxisAlignment.START,  # Alineado a la izquierda
        ),
        border=ft.Border(bottom=ft.BorderSide(1, ft.colors.WHITE))  # Barra inferior blanca
    )
    
    # Función para alternar la visibilidad de la contraseña

    # Campo de texto de contraseña con icono en una fila (Row)
    contra_txt = ft.Container(
        content=ft.Row(
            controls=[
                ft.Icon(name=ft.icons.LOCK, color=ft.colors.ORANGE),  # Icono de candado en naranja
                ft.TextField(
                    label="Contraseña",
                    password=True,
                    width=280,  # Ajuste del tamaño para el ícono al final
                    label_style=ft.TextStyle(color=ft.colors.WHITE),  # Texto blanco
                    border=ft.InputBorder.NONE  # Sin bordes
                ),
                ft.IconButton(
                    icon=ft.icons.VISIBILITY,
                    icon_color=ft.colors.ORANGE,
                    on_click=toggle_password_visibility
                )
            ],
            alignment=ft.MainAxisAlignment.START,
        ),
        border=ft.Border(bottom=ft.BorderSide(1, ft.colors.WHITE))  # Barra inferior blanca
    )
    
    ini_boton = ft.Container(
        content=ft.ElevatedButton(
            content=ft.Text("Iniciar sesión"),
            style=ft.ButtonStyle(
                color=ft.colors.WHITE,
                bgcolor=ft.colors.ORANGE,
                shape=ft.RoundedRectangleBorder(radius=5)
            ),
            width=170,
            height=35,
        ),
        margin=ft.Margin(left=95, bottom=20, top=0, right=0),
    )
    
    container = ft.Container(
        content=ft.Column(
            [
                logo,
                ini,
                us_txt,
                contra_txt,
                ini_boton
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        ),
        width=400,
        height=500,
        bgcolor="#324678",
        border_radius=ft.border_radius.all(10),
        padding=20
    )
    
    ventana1.add(container)

ft.app(target=main)
