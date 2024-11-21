import tkinter as tk
from PIL import Image,ImageTk

root = tk.Tk()
root.title("")
root.state('zoomed')

def pantalla_anteultima():
    color_azul = "#324774" 
    color_naranja = "#dc860b"  
    color_blanco = "#FFFFFF" 
    # Marco izquierdo con fondo naranja
    marco_menu = tk.Frame(root, bg=color_naranja, width=200, height=400)
    marco_menu.pack(side="left", fill="y")

    icono_label = tk.Label(marco_menu, text="👤", font=("Arial", 30), bg=color_naranja, fg=color_blanco)
    icono_label.pack(anchor="n", padx=20, pady=(10, 5))

    tk.Label(marco_menu,bg=color_naranja,text="\n\n\n").pack(anchor="w", padx=20, pady=5)

    boton_menu = tk.Button(marco_menu, text="🏚️ Menú", compound="left", font=("Arial", 20), 
                           bg=color_naranja, fg=color_blanco, bd=0)
    boton_menu.pack(anchor="w", padx=20, pady=(10, 5))

    boton_carga = tk.Button(marco_menu, text="✏️    Carga", compound="left", font=("Arial", 20), 
                            bg=color_naranja, fg=color_blanco, bd=0)
    boton_carga.pack(anchor="w", padx=20, pady=5)

    boton_ver_datos = tk.Button(marco_menu, text="🔍   Ver datos",  compound="left", font=("Arial", 20), bg=color_naranja, fg=color_blanco, bd=0)
    boton_ver_datos.pack(anchor="w", padx=20, pady=5)

    tk.Label(marco_menu,bg=color_naranja,text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n").pack(anchor="w", padx=20, pady=5)

    boton_ocultar = tk.Button(marco_menu, text="👁️Ocultar", font=("Arial", 20), bg=color_naranja, fg=color_blanco, bd=0)
    boton_ocultar.pack(anchor="w", padx=20, pady=5)

    linea = tk.Frame(marco_menu, height=2, bg=color_blanco)
    linea.pack(fill="x", padx=20, pady=(5, 10))

    boton_cerrar_sesion = tk.Button(marco_menu, text="🚪 Cerrar sesión", compound="left", 
                                     font=("Arial", 20), bg=color_naranja, fg=color_blanco, bd=0)
    boton_cerrar_sesion.pack(anchor="w", padx=20, pady=(5, 20))

    marco_principal = tk.Frame(root, bg=color_azul, width=600, height=400)
    marco_principal.pack(side="right", fill="both", expand=True)

    tk.Label(marco_principal,bg=color_azul).grid(row=0,column=0)

    def crear_entry(marco, texto, fila, col):
        entry = tk.Entry(marco, font=("Arial", 15), width=24, bd=2, highlightthickness=1,
                         highlightbackground="#dc860b", bg="#dc860b", fg="white")
        entry.insert(0, texto)  
        entry.bind("<FocusIn>", lambda e: entry.delete(0, tk.END) if entry.get() == texto else None)
        entry.bind("<FocusOut>", lambda e: entry.insert(0, texto) if entry.get() == "" else None)
        entry.grid(row=fila, column=col, padx=5, pady=5) 
        return entry

    crear_entry(marco_principal, "Fecha", 1, 0)  
    crear_entry(marco_principal, "Dirección", 1, 1)  
    crear_entry(marco_principal, "Motivo", 2, 0) 
    crear_entry(marco_principal, "Expediente",2,1)

    opcion_seleccionada = tk.StringVar(value="Etiqueta") 
    opciones = ["Consulta general", "Adjuntar documentacion", "Retiro documentación", "Consulta tecnica",
                "Retiro de aprobado", "Intimacion", "Consulta adminitrativa + Avisador", 
                "Solicitud de plano", "Pagos/Rafam", "Cambios de Destino", 
                "Carpeta Nueva", "Desligamiento", "Consulta con Visador", 
                "Intimación/Infracción", "Cambio del Profesional", 
                "Desligamiento del Profesional", "Modificación de Croquis", 
                "Aviso de obra simple", "Final de obra", "Consulta por trámite"]

    menu_desplegable = tk.OptionMenu(marco_principal, opcion_seleccionada, *opciones)
    menu_desplegable.config(font=("Arial", 14), width=21, bd=1,
                            highlightthickness=1, highlightbackground="#dc860b", 
                            bg="#dc860b", fg="white",relief="sunken")
    menu_desplegable.grid(row=1, column=2, padx=5, pady=5) 

    tk.Label(marco_principal,bg=color_azul,width=10).grid(row=0,column=3)


    boton_agregar = tk.Button(marco_principal, text="➕  Agregar", font=("Arial", 13), width=16, bd=0,
                  highlightthickness=1, highlightbackground="#dc860b", bg="black", fg="white")
    boton_agregar.grid(row=1,column=4, padx=5, pady=5)

    boton_actualizar = tk.Button(marco_principal, text="🔄  Actualizar", font=("Arial", 13), width=16, bd=0,
                  highlightthickness=1, highlightbackground="#dc860b", bg="black", fg="white")
    boton_actualizar.grid(row=2,column=4, padx=5, pady=5)

    boton_editar = tk.Button(marco_principal, text="✏️      Editar", font=("Arial", 13), width=16, bd=0,
                  highlightthickness=1, highlightbackground="#dc860b", bg="black", fg="white")
    boton_editar.grid(row=3,column=4, padx=5, pady=5)

    boton_eliminar = tk.Button(marco_principal, text="🗑️ Eliminar", font=("Arial", 13), width=16, bd=0,
                  highlightthickness=1, highlightbackground="#dc860b", bg="black", fg="white")
    boton_eliminar.grid(row=4,column=4, padx=5, pady=5)

    tabla_frame = tk.Frame(marco_principal, bg=color_azul)
    tabla_frame.grid(row=5, column=0, columnspan=5, sticky="nsew", padx=10, pady=10)

    headers = ["Fecha", "Dirección", "Expediente", "Etiqueta"]
    for col, header in enumerate(headers):
        label = tk.Label(tabla_frame, text=header, borderwidth=1, relief="solid", bg="#324774", fg="white")
        label.grid(row=0, column=col, sticky="nsew") 

    for row in range(1, 2):
        for col in range(len(headers)):
            entry = tk.Entry(tabla_frame, bg="#324774", fg="white", borderwidth=1, 
                             highlightbackground="white", highlightcolor="white", width=45,)
            entry.grid(row=row, column=col, sticky="nsew")  
            entry.config(insertbackground="white")

    text_fila_3 = tk.Text(tabla_frame, bg="#324774", fg="white", borderwidth=1, 
                           highlightbackground="white", height=29)  
    text_fila_3.grid(row=3, column=0, columnspan=len(headers), sticky="nsew")




pantalla_anteultima()
root.mainloop()