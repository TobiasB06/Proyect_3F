import flet as ft

def main(page):

    # Menú lateral (barra lateral)
    menu_lateral = ft.Container(
        bgcolor="#2c3e50",  # Color de fondo de la barra lateral
        padding=20,
        width=200,  # Ancho de la barra lateral
        content=ft.Column(
            controls=[
                ft.ElevatedButton("Inicio", on_click=None),  # Ejemplo de botón
                ft.ElevatedButton("Datos", on_click=None),   # Otro botón
                ft.ElevatedButton("Configuraciones", on_click=None),
                # Agrega más botones o controles que desees en la barra lateral
            ]
        ),
    )

    # Tabla de datos
    data_table = ft.DataTable(
        border=ft.border.all(1, "WHITE"),
        border_radius=10,
        horizontal_lines=ft.BorderSide(1,"WHITE"),
        columns=[
            ft.DataColumn(label=ft.Text("Fecha", color=ft.colors.WHITE)),
            ft.DataColumn(label=ft.Text("Direccion", color=ft.colors.WHITE)),
            ft.DataColumn(label=ft.Text("Expediente", color=ft.colors.WHITE)),
            ft.DataColumn(label=ft.Text("Motivo", color=ft.colors.WHITE)),
            ft.DataColumn(label=ft.Text("#Etiqueta", color=ft.colors.WHITE)),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("2024-11-20")),
                    ft.DataCell(ft.Text("Calle Falsa 123")),
                    ft.DataCell(ft.Text("EXP-001")),
                    ft.DataCell(ft.Text("Consulta técnica")),
                    ft.DataCell(ft.Text("Consulta General")),
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("2024-11-21")),
                    ft.DataCell(ft.Text("Av. Siempre Viva 742")),
                    ft.DataCell(ft.Text("EXP-002")),
                    ft.DataCell(ft.Text("Adjuntar documentación")),
                    ft.DataCell(ft.Text("Adjuntar documentación")),
                ]
            ),
        ],
        expand=True,  # Permite que el DataTable ocupe todo el espacio disponible
    )

    # Contenido principal
    fecha = ft.Text("Fecha")
    dire = ft.Text("Dirección")
    expediente = ft.Text("Expediente")
    motivo = ft.Text("Motivo")
    etiqueta = ft.Text("#Etiqueta")

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
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                ),
                                etiqueta,
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
                    controls=[data_table],
                    alignment=ft.alignment.top_left,  # Alineación superior izquierda
                    expand=False,  # No expandir la fila
                ),
            ],
            expand=True,  # Expande el contenedor principal
        ),
    )


    # Layout con barra lateral y contenido principal
    layout = ft.Row(
        controls=[
            menu_lateral,  # Barra lateral
            ft.VerticalDivider(width=1, color=ft.colors.BLACK),  # Separador entre barra lateral y contenido
            contenido_principal,  # Contenido principal
        ],
        expand=True,  # El layout debe permitir la expansión del contenido
    )

    page.add(layout)  # Agregar al contenido de la página

ft.app(target=main)
