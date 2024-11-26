import flet as ft
from menuflet import Aplicacion

def main(ventana1: ft.Page):
    ventana1.title = "Inicio de sesión"
    ventana1.window.maximized = True
    ventana1.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    ventana1.vertical_alignment = ft.MainAxisAlignment.CENTER
    ventana1.bgcolor = ft.colors.WHITE10

    # Credenciales predeterminadas
    usuario_correcto = "a"
    contrasena_correcta = "a"

    password_visible = False

    # Función para alternar visibilidad de la contraseña
    def toggle_password_visibility(e):
        nonlocal password_visible
        password_visible = not password_visible
        contra_txt.content.controls[1].password = not password_visible
        contra_txt.content.controls[2].name = ft.icons.VISIBILITY_OFF if password_visible else ft.icons.VISIBILITY
        contra_txt.content.controls[2].update()
        contra_txt.content.controls[1].update()

    # Función para mostrar el menú
    def mostrar_menu():
        ventana1.clean()
        Aplicacion(ventana1)

    # Verifica las credenciales y redirige al menú
    def verificar_credenciales(e):
        usuario = us_txt.content.controls[1].value
        contrasena = contra_txt.content.controls[1].value

        if usuario == usuario_correcto and contrasena == contrasena_correcta:
            mostrar_menu()  # Muestra el menú
        else:
            print("Usuario o contraseña incorrectos.")

    # Ventana de inicio de sesión
    def iniciar_sesion():
        ventana1.clean()  # Limpia la ventana
        ventana1.add(container)  # Agrega el contenido inicial
        ventana1.update()

    # Logo
    logo = ft.Container(
        content=ft.Image(src="IMG-3F.jpeg", width=100, height=100),
        margin=ft.Margin(left=133, bottom=0, right=0, top=0),
    )

    # Título
    ini = ft.Container(
        content=ft.Text(
            "Inicio de sesión\nMunicipalidad Tres De Febrero",
            size=16,
            text_align=ft.TextAlign.CENTER,
            color=ft.colors.WHITE,
        ),
        margin=ft.Margin(left=75, bottom=0, right=0, top=0),
    )

    # Campo de usuario
    us_txt = ft.Container(
        content=ft.Row(
            controls=[
                ft.Icon(name=ft.icons.PERSON, color=ft.colors.ORANGE),
                ft.TextField(
                    label="Usuario",
                    width=350,
                    label_style=ft.TextStyle(color=ft.colors.WHITE),
                    text_style=ft.TextStyle(color=ft.colors.WHITE),
                    border=ft.InputBorder.NONE,
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
        ),
        border=ft.Border(bottom=ft.BorderSide(1, ft.colors.WHITE)),
    )

    # Campo de contraseña
    contra_txt = ft.Container(
        content=ft.Row(
            controls=[
                ft.Icon(name=ft.icons.LOCK, color=ft.colors.ORANGE),
                ft.TextField(
                    label="Contraseña",
                    password=True,
                    width=280,
                    label_style=ft.TextStyle(color=ft.colors.WHITE),
                    text_style=ft.TextStyle(color=ft.colors.WHITE),
                    border=ft.InputBorder.NONE,
                ),
                ft.IconButton(
                    icon=ft.icons.VISIBILITY,
                    icon_color=ft.colors.ORANGE,
                    on_click=toggle_password_visibility,
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
        ),
        border=ft.Border(bottom=ft.BorderSide(1, ft.colors.WHITE)),
    )

    # Botón de inicio de sesión
    ini_boton = ft.Container(
        content=ft.ElevatedButton(
            content=ft.Text("Iniciar sesión"),
            style=ft.ButtonStyle(
                color=ft.colors.WHITE,
                bgcolor=ft.colors.ORANGE,
                shape=ft.RoundedRectangleBorder(radius=5),
            ),
            width=170,
            height=35,
            on_click=verificar_credenciales,
        ),
        margin=ft.Margin(left=95, bottom=20, top=0, right=0),
    )

    # Contenedor principal
    container = ft.Container(
        content=ft.Column(
            [logo, ini, us_txt, contra_txt, ini_boton],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        ),
        width=400,
        height=500,
        bgcolor="#324678",
        border_radius=ft.border_radius.all(10),
        padding=20,
    )

    iniciar_sesion()  # Inicia con la pantalla de login

if __name__ == "__main__":  
    ft.app(target=main)
