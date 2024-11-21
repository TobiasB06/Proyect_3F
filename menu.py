import flet as ft 

def main(ventana2: ft.Page):
    ventana2.title = "Bienvenida"
    ventana2.window.width = 400
    ventana2.window.height = 600  
    ventana2.window.resizable = False
    ventana2.window.maximized = True 
    ventana2.bgcolor = ft.colors.BLACK
    ventana2.spacing = 0  
    ventana2.padding = 0
    ventana2.theme_mode = ft.ThemeMode

    menu_lateral = ft.Container(
        width=250,
        bgcolor=ft.colors.ORANGE_600,
        content=ft.Column(
            controls=[
                ft.Container(
                    content=ft.CircleAvatar(
                        content=ft.Image(
                            src="Imagenes/IMG-3F.jpeg",
                            fit=ft.ImageFit.COVER,
                        ),
                    ),
                    margin=ft.margin.only(left=20, top=35),
                    border_radius=250,  
                    height=200,
                    width=200,  
                ),
                ft.Container(
                    ft.TextButton(
                        content=ft.Row(
                            controls=[
                                ft.Icon(ft.icons.HOME),
                                ft.Text("Menú", size=24, color=ft.colors.WHITE)
                            ]
                        ),
                        on_click=lambda e: None
                    ),
                    margin=ft.margin.only(top=50)  
                ),
                ft.Container(
                    ft.TextButton(
                        content=ft.Row(
                            controls=[
                                ft.Icon(ft.icons.UPLOAD),
                                ft.Text("Carga", size=24, color=ft.colors.WHITE)
                            ]
                        ),
                        on_click=lambda e: None
                    ),
                    margin=ft.margin.only(top=50)
                ),
                ft.Container(
                    ft.TextButton(
                        content=ft.Row(
                            controls=[
                                ft.Icon(ft.icons.LOUPE),
                                ft.Text("Ver datos", size=24, color=ft.colors.WHITE)
                            ]
                        ),
                    ),
                    margin=ft.margin.only(top=50),
                ),
                ft.Container(
                    ft.TextButton(
                        content=ft.Row(
                            controls=[
                                ft.Icon(ft.icons.VISIBILITY_OFF),
                                ft.Text("Ocultar", size=24, color=ft.colors.WHITE)
                            ]
                        ),
                    ),
                    margin=ft.margin.only(top=50),
                ),
                ft.Container(
                    ft.TextButton(
                        content=ft.Row(
                            controls=[
                                ft.Icon(ft.icons.DOOR_SLIDING_ROUNDED),
                                ft.Text("Cerrar sesión", size=24, color=ft.colors.WHITE)
                            ]
                        ),
                    ),
                    margin=ft.margin.only(top=65),
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
        ),
    )

    fecha = ft.TextField(label="Fecha",width=210, bgcolor=ft.colors.ORANGE,color=ft.colors.WHITE)
    dire = ft.TextField(label="Dirección", width=210, bgcolor=ft.colors.ORANGE,color=ft.colors.WHITE)
    expediente = ft.TextField(label="Expediente", width=210, bgcolor=ft.colors.ORANGE,color=ft.colors.WHITE)
    motivo = ft.TextField(label="Motivo", width=210, bgcolor=ft.colors.ORANGE,color=ft.colors.WHITE)
    etiqueta = ft.Dropdown(
        label="# Etiqueta",
        height=50,
        options=[
            ft.dropdown.Option("Consulta General"),
            ft.dropdown.Option("Adjuntar documentación"),
            ft.dropdown.Option("Retiro Documentación"),
            ft.dropdown.Option("Consulta Tecnica"),
            ft.dropdown.Option("Consulta Técnica"),
            ft.dropdown.Option("Intimación"),
            ft.dropdown.Option("Consulta Administrativa + visador"),
            ft.dropdown.Option("Solicitud De Plano "),
            ft.dropdown.Option("Pagos/Rafam"), 
            ft.dropdown.Option("Cambio De Destino"),
            ft.dropdown.Option("Carpeta Nueva"),
            ft.dropdown.Option("Desligamiento"),
            ft.dropdown.Option("Consulta Con Visador"),
            ft.dropdown.Option("Intimación/Infracción"),
            ft.dropdown.Option("Cambio De Profesional"),
            ft.dropdown.Option("Desligamiento De Profesional"),
            ft.dropdown.Option("Modifficación De Croquis"),
            ft.dropdown.Option("Aviso De Obra Simple "),
            ft.dropdown.Option("Final De obra "),
            ft.dropdown.Option("Consulta De Trámite"), 
                 
        ],
        bgcolor=ft.colors.ORANGE,
        color=ft.colors.WHITE,
        width=300
    )

    botones = ft.Column(  # Cambiar de Row a Column para disposición vertical
        controls=[
            ft.ElevatedButton(  
                icon=ft.icons.ADD,
                text="Agregar",
                color=ft.colors.WHITE, 
                icon_color=ft.colors.WHITE,
                height=35,
                width=142,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=5),
                    icon_size=30,
                ),
            ), 
            ft.ElevatedButton(
                icon=ft.icons.REFRESH,
                text="Actualizar",
                color=ft.colors.WHITE,
                height=35,
                width=142,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=5),  
                    icon_size=30
                ),
            ),
            ft.ElevatedButton(
                icon=ft.icons.EDIT,
                text="Editar",
                color=ft.colors.WHITE,
                height=35,
                width=142,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=5),  
                    icon_size=30
                ),
            ),
            ft.ElevatedButton(
                icon=ft.icons.DELETE,
                text="Eliminar",
                color=ft.colors.WHITE,
                height=35,
                width=142,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=5),  
                    icon_size=30
                ),
            )
        ],
        alignment=ft.MainAxisAlignment.START,  # Alinear al inicio si lo deseas
    )

    data_table = ft.DataTable(
        height=1000,
        width=1148,
        bgcolor=ft.colors.WHITE,

        columns=[
            ft.DataColumn(label=ft.Text("Fecha",color= ft.colors.BLACK)),
            ft.DataColumn(label=ft.Text("Direccion",color= ft.colors.BLACK)),
            ft.DataColumn(label=ft.Text("Expediente",color= ft.colors.BLACK)),
            ft.DataColumn(label=ft.Text("Motivo",color = ft.colors.BLACK)),
            ft.DataColumn(label=ft.Text("#Etiqueta",color = ft.colors.BLACK)),
        ],
        rows=[]
        
    )

    # Crear una "simulación de borde" alrededor del DataTable usando relleno
    

    contenido_principal = ft.Container(
        bgcolor="#323d6b",
        padding=20,
        border_radius=10,
        expand=True,
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[fecha, dire, expediente, motivo],
                                    alignment=ft.MainAxisAlignment.START,
                                ),
                                etiqueta,
                            ],
                            expand=True
                        ),
                        ft.Container(
                            content=botones,  # Aquí se incluye el Column de botones
                            alignment=ft.alignment.top_right  # Alineación a la esquina superior derecha
                        ),
                    ],
                ),
                ft.Row(  # Nueva fila para la tabla
                    controls=[
                        data_table
                          # Añadiendo la tabla aquí
                    ],
                ),
            ],
        ),
    )

    layout = ft.Row(
        controls=[
            menu_lateral,
            ft.VerticalDivider(width=1, color=ft.colors.BLACK),
            contenido_principal,
        ],
        expand=True
    )

    ventana2.add(layout)

ft.app(target=main)
