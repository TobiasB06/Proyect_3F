import flet as ft
import datetime
import mysql.connector
class Aplicacion:
    def __init__(self, ventana2: ft.Page):
        self.ventana2 = ventana2
        self.fecha_seleccionada = None
        self.ventana2.title = "Menu"
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
    def handle_change(self,e,mostrar_datos):
        self.fecha_seleccionada = e.control.value.strftime('%Y-%m-%d')
        if mostrar_datos:
            self.opcion_fecha.options=[
                ft.dropdown.Option(f"Despues del {self.fecha_seleccionada} "),
                ft.dropdown.Option(f"Antes del {self.fecha_seleccionada}"),
                ft.dropdown.Option(f"El {self.fecha_seleccionada}")
            ]
            self.opcion_fecha.update()
    def conectar_db(self):
        try:
            # Establecer conexión con la base de datos MySQL
            self.cnx = mysql.connector.connect(
                host="localhost",        
                user="root",          
                database="municipalidad"
            )
            self.cursor = self.cnx.cursor()
        except mysql.connector.Error as e:
            print(f"Error de conexión a MySQL: {e}")
            return None
    def obtener_registros_mysql(self):
        self.conectar_db()
        if self.cursor:
            try:
                self.cursor.execute("SELECT FECHA, DIRECCION, EXPEDIENTE, MOTIVO, ETIQUETA FROM consultas")
                registros = self.cursor.fetchall()
                self.agregar_filas_a_tabla(self.data_table, registros)
                self.cursor.close()
                self.cnx.close()
            except mysql.connector.Error as e:
                print(f"Error al obtener los registros: {e}")
    def eliminar_filas_seleccionadas(self, e):
        filas_a_eliminar = []
        ids_a_eliminar = []

        # Verificar qué filas tienen el CheckBox seleccionado
        for row in self.data_table.rows:
            checkbox = row.cells[0].content
            if checkbox.value:  # Si el CheckBox está seleccionado
                filas_a_eliminar.append(row)
                ids_a_eliminar.append(row.cells[3].content.value)  # Usar expediente o ID como referencia

        # Eliminar las filas de la tabla visual
        for fila in filas_a_eliminar:
            self.data_table.rows.remove(fila)

        self.data_table.update()

        # Eliminar los registros de la base de datos
        print(ids_a_eliminar)
        if ids_a_eliminar:
            self.conectar_db()
            try:
                # Usar una consulta SQL para eliminar varios registros
                query = "DELETE FROM consultas WHERE EXPEDIENTE IN (%s)" % (
                    ",".join(["%s"] * len(ids_a_eliminar))
                )
                self.cursor.execute(query, ids_a_eliminar)
                self.cnx.commit()
            except mysql.connector.Error as e:
                print(f"Error al eliminar registros: {e}")
            finally:
                self.cursor.close()
                self.cnx.close()
    def agregar_filas_a_tabla(self,data_table, registros):
        for registro in registros:
            # Asegúrate de que cada registro tenga el formato correcto
            nueva_fila = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Checkbox()),
                    ft.DataCell(ft.Text(str(registro[0]))),  # Fecha
                    ft.DataCell(ft.Text(str(registro[1]))),  # Dirección
                    ft.DataCell(ft.Text(str(registro[2]))),  # Expediente
                    ft.DataCell(ft.Text(str(registro[3]))),  # Motivo
                    ft.DataCell(ft.Text(str(registro[4]))),  # Etiqueta
                ]
            )
            data_table.rows.append(nueva_fila)
        data_table.update()  # Actualizar la tabla
    def mostrar_carga(self, e):
        self.fecha = ft.ElevatedButton(
            "Elegir fecha",
            icon=ft.icons.DATE_RANGE,
            bgcolor=ft.colors.ORANGE_600,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=5),
            ),
            color="#323d6b",
            width=250,
            height=50,
            on_click=lambda e: self.ventana2.open(
                ft.DatePicker(
                    first_date=datetime.datetime(year=2000, month=10, day=1),
                    on_change=lambda e:self.handle_change(e,False),
                )
            ),
        )
        self.direccion = ft.TextField(label="Dirección", width=210, bgcolor=ft.colors.ORANGE,color=ft.colors.WHITE)
        self.expediente = ft.TextField(label="Expediente", width=210, bgcolor=ft.colors.ORANGE,color=ft.colors.WHITE)
        self.motivo = ft.TextField(label="Motivo", width=210, bgcolor=ft.colors.ORANGE,color=ft.colors.WHITE)
        
        self.etiqueta = ft.Dropdown(
            label="Etiqueta",
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
                    icon=ft.icons.DELETE,
                    text="Eliminar",
                    bgcolor=ft.colors.BLACK54,
                    color=ft.colors.WHITE,
                    on_click=self.eliminar_filas_seleccionadas,
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
            border=ft.border.all(1, "BLACK"),
            bgcolor="white",
            show_bottom_border=True,
            border_radius=5,
            data_text_style=ft.TextStyle(color=ft.colors.BLACK),
            heading_text_style=ft.TextStyle(color=ft.colors.BLACK),
            columns=[
                ft.DataColumn(label=ft.Text("")),
                ft.DataColumn(label=ft.Text("Fecha")),
                ft.DataColumn(label=ft.Text("Direccion")),
                ft.DataColumn(label=ft.Text("Expediente")),
                ft.DataColumn(label=ft.Text("Motivo")),
                ft.DataColumn(label=ft.Text("Etiqueta")),
            ],
            expand=True,  # Permite que el DataTable ocupe todo el espacio disponible
        )

        # Crear el ListView
        lv = ft.ListView(
            expand=1, 
            spacing=10, 
            padding=5, 
        )
        lv.controls.append(self.data_table)

        # Crear el contenedor principal
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
                                        controls=[self.fecha, self.direccion, self.expediente, self.motivo],
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    ),
                                    self.etiqueta,
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
                        controls=[lv],
                        alignment=ft.alignment.top_left,  # Alineación superior izquierda
                        expand=True,  # No expandir la fila
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
        self.obtener_registros_mysql()
    def buscar_datos(self, e):
        expediente = self.expediente.value.strip()  # Elimina espacios adicionales
        opcion_fecha = self.opcion_fecha.value
        fecha = self.fecha_seleccionada

        # Base de la consulta SQL
        sql_statement = "SELECT * FROM consultas WHERE 1=1"
        filtros = []

        # Filtrar por fecha según la opción seleccionada
        if opcion_fecha:
            if "Despues del" in opcion_fecha:
                filtros.append(f"FECHA > '{fecha}'")
            elif "Antes del" in opcion_fecha:
                filtros.append(f"FECHA < '{fecha}'")
            elif "El" in opcion_fecha:
                filtros.append(f"FECHA = '{fecha}'")

        # Filtrar por expediente si se proporciona
        if expediente:
            filtros.append(f"EXPEDIENTE = '{expediente}'")

        # Añadir filtros al SQL si hay alguno
        if filtros:
            sql_statement += " AND " + " AND ".join(filtros)

        # Ejemplo de consulta final
        print(f"Consulta generada: {sql_statement}")

        # Conectar a la base de datos y ejecutar la consulta
        self.conectar_db()
        self.cursor.execute(sql_statement)
        resultados = self.cursor.fetchall()
        self.cursor.close()
        self.cnx.close()

        # Limpiar la tabla antes de mostrar los resultados
        self.data_table.rows.clear()

        # Agregar los resultados obtenidos
        for fila in resultados:
            nueva_fila = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Checkbox()),
                    ft.DataCell(ft.Text(fila[0])),  # Suponiendo que FECHA es la primera columna
                    ft.DataCell(ft.Text(fila[1])),  # DIRECCION
                    ft.DataCell(ft.Text(fila[2])),  # EXPEDIENTE
                    ft.DataCell(ft.Text(fila[3])),  # MOTIVO
                    ft.DataCell(ft.Text(fila[4])),  # ETIQUETA
                ]
            )
            self.data_table.rows.append(nueva_fila)

        # Refrescar la tabla para mostrar los nuevos datos
        self.data_table.update()
            
    def agregar_campos(self, e):
        
        valor_fecha = self.fecha_seleccionada
        valor_direccion = self.direccion.value
        valor_expediente = self.expediente.value
        valor_motivo = self.motivo.value
        valor_etiqueta = self.etiqueta.value
        
        nueva_fila = ft.DataRow(
            cells=[
                ft.DataCell(ft.Checkbox()),
                ft.DataCell(ft.Text(valor_fecha)),
                ft.DataCell(ft.Text(valor_direccion)),
                ft.DataCell(ft.Text(valor_expediente)),
                ft.DataCell(ft.Text(valor_motivo)),
                ft.DataCell(ft.Text(valor_etiqueta)),
            ]
        )
        self.data_table.rows.append(nueva_fila)
        self.data_table.update()
        self.conectar_db()
        self.cursor.execute("INSERT INTO consultas (FECHA, DIRECCION, EXPEDIENTE, MOTIVO, ETIQUETA) VALUES (%s, %s, %s, %s, %s)", (valor_fecha, valor_direccion, valor_expediente, valor_motivo, valor_etiqueta))
        self.cnx.commit()
        self.cursor.close()
        self.cnx.close()
        self.direccion.value = ""
        self.expediente.value = ""
        self.motivo.value = ""
        self.etiqueta.value = ""
    def mostrar_datos(self, e):
        # Crear el botón para elegir la fecha
        self.fecha_filtro = ft.ElevatedButton(
            "Elegir fecha",
            icon=ft.icons.DATE_RANGE,
            bgcolor=ft.colors.ORANGE_600,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=5),
            ),
            width=250,
            height=60,
            on_click=lambda e:self.ventana2.open(
                ft.DatePicker(
                    first_date=datetime.datetime(year=2000, month=10, day=1),
                    on_change=lambda e:self.handle_change(e,True),
                )
            )
        )
        # Crear la lista de opciones
        self.opcion_fecha=ft.Dropdown(
            label="Elegir Momento",
            options=[
                ft.dropdown.Option("Seleccione una fecha"),
            ],
            bgcolor=ft.colors.ORANGE,
            color=ft.colors.WHITE,
            width=300
        )
        # Crear los Entry
        self.expediente = ft.TextField(label="Expediente", width=210, bgcolor=ft.colors.ORANGE,color=ft.colors.WHITE)
        # Crear los botones
        botones= ft.Column(
            controls=[
                ft.ElevatedButton(
                    icon=ft.icons.SEARCH,
                    text="Buscar",
                    bgcolor=ft.colors.BLACK54,
                    color=ft.colors.WHITE, 
                    icon_color=ft.colors.WHITE,
                    height=35,
                    width=142,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=5),
                        icon_size=30,
                    ),
                    
                    on_click=self.buscar_datos
                ),
                ft.ElevatedButton(
                    icon=ft.icons.DELETE,
                    text="Eliminar",
                    bgcolor=ft.colors.BLACK54,
                    color=ft.colors.WHITE,
                    on_click=self.eliminar_filas_seleccionadas,
                    height=35,
                    width=142,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=5),  
                        icon_size=30
                    ),
                )
            ]
        )
        # Crea la tabla
        self.data_table = ft.DataTable(
            border=ft.border.all(1, "BLACK"),
            bgcolor="white",
            show_bottom_border=True,
            border_radius=5,
            data_text_style=ft.TextStyle(color=ft.colors.BLACK),
            heading_text_style=ft.TextStyle(color=ft.colors.BLACK),
            horizontal_lines=ft.BorderSide(1, "WHITE"),
            columns=[
                ft.DataColumn(label=ft.Text("")),
                ft.DataColumn(label=ft.Text("Fecha")),
                ft.DataColumn(label=ft.Text("Direccion")),
                ft.DataColumn(label=ft.Text("Expediente")),
                ft.DataColumn(label=ft.Text("Motivo")),
                ft.DataColumn(label=ft.Text("Etiqueta")),
            ],
            expand=True,  # Permite que el DataTable ocupe todo el espacio disponible
        )

        # Crear el ListView
        lv = ft.ListView(
            expand=1, 
            spacing=10, 
        )
        lv.controls.append(self.data_table)

        # Crear el contenido principal de mostrar datos
        contenido_mostrar_datos=ft.Container(
            bgcolor="#323d6b",
            expand=True,
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Column(
                                controls=[
                                    ft.Row(
                                        controls=[self.fecha_filtro,self.opcion_fecha, self.expediente,],
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    ),
                                ],
                                expand=True,  # Solo la columna que contiene los Entry y etiqueta se expandirse
                            ),
                            ft.Container(
                                content=botones,
                                alignment=ft.alignment.top_right,
                                margin=ft.margin.only(left=20),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Row(
                        controls=[lv],
                    )
                ],
                expand=True,
            )
        )
        layout=ft.Row(
            controls=[
                contenido_mostrar_datos,
            ],
            expand=True,
        )
        self.contenido_principal.content = layout
        self.ventana2.update()
        self.obtener_registros_mysql()

    def mostrar_cerrar_sesion(self, e):
        from loginconflet import main as main_login_flet
        self.ventana2.clean()
        main_login_flet(self.ventana2)

