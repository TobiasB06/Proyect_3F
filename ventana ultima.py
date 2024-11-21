import tkinter as tk
from PIL import Image,ImageTk

root = tk.Tk()
root.title("")
root.state('zoomed')

def pantalla_ultima():
    color_azul = "#324774" 
    color_naranja = "#dc860b"  
    color_blanco = "#FFFFFF" 
    

    marco_principal = tk.Frame(root, bg=color_azul, width=600, height=400)
    marco_principal.pack(side="right", fill="both", expand=True)

    tk.Label(marco_principal,bg=color_azul).grid(row=0,column=0)

    def crear_entry(marco, texto, fila, col):
        entry = tk.Entry(marco, font=("Arial", 15), width=30, bd=2, highlightthickness=1,
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
    menu_desplegable.config(font=("Arial", 14), width=27, bd=1,
                            highlightthickness=1, highlightbackground="#dc860b", 
                            bg="#dc860b", fg="white",relief="sunken")
    menu_desplegable.grid(row=1, column=2, padx=5, pady=5) 

    tk.Label(marco_principal,bg=color_azul,width=3).grid(row=0,column=3)


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

    boton_volver  = tk.Button(marco_principal, text="↩️       Volver", font=("Arial", 13), width=16, bd=0,
                  highlightthickness=1, highlightbackground="#dc860b", bg="red", fg="white")
    boton_volver.grid(row=5,column=4, padx=5, pady=5)

    tabla_frame = tk.Frame(marco_principal, bg=color_azul)
    tabla_frame.grid(row=6, column=0, columnspan=5, sticky="nsew", padx=10, pady=10)

    headers = ["Fecha", "Dirección", "Expediente", "Etiqueta"]
    for col, header in enumerate(headers):
        label = tk.Label(tabla_frame, text=header, borderwidth=1, relief="solid", font=("Arial", 13), bg="#324774", fg="white")
        label.grid(row=0, column=col, sticky="nsew") 

    for row in range(1, 2):
        for col in range(len(headers)):
            entry = tk.Entry(tabla_frame, bg="#324774", fg="white", borderwidth=2, 
                             highlightbackground="white", highlightcolor="white", width=56,)
            entry.grid(row=row, column=col, sticky="nsew")  
            entry.config(insertbackground="white")

    text_fila_3 = tk.Text(tabla_frame, bg="#324774", fg="white", borderwidth=1, 
                           highlightbackground="white", height=25)  
    text_fila_3.grid(row=3, column=0, columnspan=len(headers), sticky="nsew")




pantalla_ultima()
root.mainloop()