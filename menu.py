import flet as ft
import datetime
class Aplicacion:
    def __init__(self, ventana2: ft.Page):
        self.ventana2 = ventana2
        self.fecha_seleccionada = None
        self.ventana2.title = "Bienvenida"
        self.ventana2.window.width = 400
        self.ventana2.window.height = 600  
        self.ventana2.window.maximized = True 
        self.ventana2.bgcolor = "#323d6b"
        self.ventana2.spacing = 0  
        self.ventana2.padding = 0
        self.ventana2.theme_mode = ft.ThemeMode.LIGHT
        
        # Crear elementos de la interfaz
        self.menu_lateral = self.crear_menu_lateral()
        self.contenido_principal = self.crear_contenido_principal()
        self.layout = self.crear_layout()

        # Agregar el layout inicial
        self.ventana2.add(self.layout)

    def crear_menu_lateral(self):
        # Contenido del menú lateral
        menu_lateral = ft.Container(
            width=250,
            bgcolor=ft.colors.ORANGE_600,
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Image(
                            src="IMG-3F.jpeg",
                            width=150,
                            height=150,
                            fit=ft.ImageFit.COVER,  # Esto asegura que la imagen se ajuste al contenedor sin distorsionarse
                        ),
                        width=150,
                        height=150,
                        border_radius=20,  # Redondeo de bordes
                        margin=ft.margin.symmetric(horizontal=50, vertical=10),
                        alignment=ft.alignment.center,  # Centra la imagen dentro del contenedor
                    ),
                    self.crear_boton_menu("Menú", ft.icons.HOME, self.mostrar_menu),
                    self.crear_boton_menu("Carga", ft.icons.UPLOAD, self.mostrar_carga),
                    self.crear_boton_menu("Ver datos", ft.icons.LOUPE, self.mostrar_datos),
                    self.crear_boton_menu("Cerrar sesión", ft.icons.DOOR_SLIDING_ROUNDED, self.mostrar_cerrar_sesion),
                ],
                alignment=ft.MainAxisAlignment.START,  # Esto organiza los botones verticalmente
            ),
            alignment=ft.alignment.top_center
        )
        return menu_lateral

    def crear_boton_menu(self, texto, icono, on_click):
        return ft.Container(
            ft.TextButton(
                content=ft.Row(
                    controls=[
                        ft.Icon(icono),
                        ft.Text(texto, size=24, color=ft.colors.WHITE)
                    ]
                ),
                on_click=on_click
            ),
            margin=ft.margin.only(top=50)
        )
    
    def crear_contenido_principal(self):
        # Este es el contenido que cambia según la opción seleccionada en el menú
        return ft.Container(
            bgcolor="#323d6b",
            padding=20,
            border_radius=10,
            expand=True,
            content=ft.Text("Contenido principal aquí", color=ft.colors.WHITE),
        )
    
    def crear_layout(self):
        # Layout que contiene el menú lateral y el contenido principal
        layout = ft.Row(
            controls=[
                self.menu_lateral,
                self.contenido_principal
            ],
            expand=True,
        )
        return layout

    # Funciones para manejar los cambios de pantalla
    def mostrar_menu(self, e):
        self.contenido_principal.content = ft.Text("Bienvenido al menú", color=ft.colors.WHITE)
        self.ventana2.update()
    def handle_change(self,e):
        self.fecha_seleccionada = e.control.value.strftime('%d/%m/%Y')
        
    def mostrar_carga(self, e):
        self.fecha = ft.ElevatedButton(
            "Elegir Fecha",
            icon=ft.icons.CALENDAR_MONTH,
            on_click=lambda e: self.ventana2.open(
                ft.DatePicker(
                    first_date=datetime.datetime(year=2000, month=10, day=1),
                    on_change=self.handle_change,
                )
            ),
        )
        self.direccion = ft.TextField(label="Dirección", width=210, bgcolor=ft.colors.ORANGE,color=ft.colors.WHITE)
        self.expediente = ft.TextField(label="Expediente", width=210, bgcolor=ft.colors.ORANGE,color=ft.colors.WHITE)
        self.motivo = ft.TextField(label="Motivo", width=210, bgcolor=ft.colors.ORANGE,color=ft.colors.WHITE)
        
        self.etiqueta = ft.Dropdown(
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
                    bgcolor=ft.colors.BLACK54,
                    color=ft.colors.WHITE, 
                    icon_color=ft.colors.WHITE,
                    height=35,
                    width=142,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=5),
                        icon_size=30,
                    ),
                    on_click=self.agregar_campos
                ), 
                ft.ElevatedButton(
                    icon=ft.icons.REFRESH,
                    bgcolor=ft.colors.BLACK54,
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
                    bgcolor=ft.colors.BLACK54,
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
                    bgcolor=ft.colors.BLACK54,
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


        self.data_table = ft.DataTable(
            border=ft.border.all(1, "WHITE"),
            border_radius=10,
            horizontal_lines=ft.BorderSide(1,"WHITE"),
            data_text_style=ft.TextStyle(color=ft.colors.WHITE),
            columns=[
                ft.DataColumn(label=ft.Text("Fecha", color=ft.colors.WHITE)),
                ft.DataColumn(label=ft.Text("Direccion", color=ft.colors.WHITE)),
                ft.DataColumn(label=ft.Text("Expediente", color=ft.colors.WHITE)),
                ft.DataColumn(label=ft.Text("Motivo", color=ft.colors.WHITE)),
                ft.DataColumn(label=ft.Text("#Etiqueta", color=ft.colors.WHITE)),
            ],
            expand=True,  # Permite que el DataTable ocupe todo el espacio disponible
            
        )

        contenido_principal = ft.Container(
            bgcolor="#323d6b",
            expand=True,
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Column(
                                controls=[
                                    ft.Row(
                                        controls=[self.fecha, self.direccion, self.expediente, self.motivo,self.etiqueta],
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                        
                                    ),
                                ],
                                expand=True,  # Solo la columna que contiene los Entry y etiqueta se expandirá
                            ),
                            ft.Container(
                                content=botones,
                                alignment=ft.alignment.top_right,
                            ),
                        ],
                    ),
                    # Fila con DataTable alineada a la parte superior
                    ft.Row(
                        controls=[self.data_table],
                        alignment=ft.alignment.top_left,  # Alineación superior izquierda
                        expand=False,  # No expandir la fila
                    ),
                ],
                expand=True,  # Expande el contenedor principal
            ),
        )

        layout = ft.Row(
            controls=[
                contenido_principal,
            ],
            expand=True,
        )
        self.contenido_principal.content = layout
        self.ventana2.update()
    def agregar_campos(self, e):
        valor_fecha = self.fecha_seleccionada
        valor_direccion = self.direccion.value
        valor_expediente = self.expediente.value
        valor_motivo = self.motivo.value
        valor_etiqueta = self.etiqueta.value
        
        nueva_fila = ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(valor_fecha)),
                ft.DataCell(ft.Text(valor_direccion)),
                ft.DataCell(ft.Text(valor_expediente)),
                ft.DataCell(ft.Text(valor_motivo)),
                ft.DataCell(ft.Text(valor_etiqueta)),
            ]
        )
        self.data_table.rows.append(nueva_fila)
        self.data_table.update()
        self.direccion.value = ""
        self.expediente.value = ""
        self.motivo.value = ""
        self.etiqueta.value = ""
    def mostrar_datos(self, e):
        self.contenido_principal.content = ft.Text("Datos", color=ft.colors.WHITE)
        self.ventana2.update()

    def mostrar_cerrar_sesion(self, e):
        self.contenido_principal.content = ft.Text("Cerrar Sesion", color=ft.colors.WHITE)
        self.ventana2.update()

def main(ventana2: ft.Page):
    app = Aplicacion(ventana2)

ft.app(target=main)
