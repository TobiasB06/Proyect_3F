import tkinter as tk
from PIL import Image,ImageTk
import mysql.connector
import subprocess
from tkinter import messagebox

# Conexión a la base de datos
def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",      
        password="", 
        database="municipalidad"
    )
    
root = tk.Tk()
root.title("")
root.state('zoomed')

def pantalla_anteultima():
    color_azul = "#324774" 
    color_naranja = "#dc860b"  
    color_blanco = "#FFFFFF" 
    def cerrar_sesion():
        respuesta = messagebox.askyesno("Cerrar sesión", "¿Estás seguro de que deseas cerrar sesión?")
        if respuesta:
            root.destroy()
            subprocess.run(["python", "logincontkinter.py"])

    # Marco izquierdo con fondo naranja
    marco_menu = tk.Frame(root, bg=color_naranja, width=200, height=400)
    marco_menu.pack(side="left", fill="y")

    marco_principal = tk.Frame(root, bg=color_azul, width=600, height=400)
    marco_principal.pack(side="right", fill="both", expand=True)
    tk.Label(marco_principal,bg=color_azul).grid(row=0,column=0)
    
    def limpiar_marco():
        for widget in marco_principal.winfo_children():
            widget.destroy()
    
    def Carga(): 
        limpiar_marco()
        entry_fecha = None
        entry_direccion = None
        entry_motivo = None
        entry_expediente = None
        selected_expediente = None

        def crear_entry(marco, texto, fila, col):
            tk.Label(marco, text=texto, font=("Arial", 15), bg=color_naranja, fg=color_blanco).grid(row=fila, column=col, padx=5, pady=5)
            entry = tk.Entry(marco, font=("Arial", 15), width=24, bd=2, highlightthickness=1,
                            highlightbackground="#dc860b", bg="#dc860b", fg="white") 
            entry.grid(row=fila+1, column=col, padx=5, pady=5, sticky="nswe")
            marco.grid_columnconfigure(col, weight=1)
            marco.grid_rowconfigure(fila, weight=1)
            return entry

        entry_fecha = crear_entry(marco_principal, "Fecha", 0, 0)
        entry_direccion = crear_entry(marco_principal, "Dirección", 0, 1)
        entry_motivo = crear_entry(marco_principal, "Motivo", 0, 2)
        entry_expediente = crear_entry(marco_principal, "Expediente", 0, 3)

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
        marco_principal.grid_rowconfigure(2, weight=1)
        menu_desplegable.grid(row=2, column=0, padx=5, pady=5,sticky="nswe") 
        def agregar_registro():
                conn = conectar_bd()
                cursor = conn.cursor()
                sql = """
                INSERT INTO consultas (fecha, direccion, expediente, motivo, etiqueta)
                VALUES (%s, %s, %s, %s, %s)
                """
                try:
                    fecha = entry_fecha.get()
                    direccion = entry_direccion.get()
                    motivo = entry_motivo.get()
                    expediente = entry_expediente.get()
                    etiqueta = opcion_seleccionada.get()

                    if not fecha or not direccion or not motivo or not expediente or etiqueta == "Etiqueta":
                        raise ValueError("Todos los campos son obligatorios")
                    
                    cursor.execute(sql, (fecha, direccion, expediente, motivo, etiqueta))
                    conn.commit()

                    messagebox.showinfo(f"Registro agregado: {fecha}, {direccion}, {motivo}, {expediente}, {etiqueta}")
                    messagebox.showinfo("Éxito", "Registro agregado correctamente.")

                    entry_fecha.delete(0, tk.END)
                    entry_direccion.delete(0, tk.END)
                    entry_motivo.delete(0, tk.END)
                    entry_expediente.delete(0, tk.END)
                    opcion_seleccionada.set("Etiqueta")
                except ValueError as e:
                    messagebox.showwarning("Advertencia", str(e))
                except Exception as e:
                    messagebox.showerror("Error", f"Ocurrió un error inesperado: {e}")
        
        def seleccionar_registro(registro):
            nonlocal selected_expediente
            selected_expediente = registro[2]  # El expediente está en la tercera columna
            entry_fecha.delete(0, tk.END)
            entry_direccion.delete(0, tk.END)
            entry_motivo.delete(0, tk.END)
            entry_expediente.delete(0, tk.END)

            entry_fecha.insert(0, registro[0])
            entry_direccion.insert(0, registro[1])
            entry_motivo.insert(0, registro[3])
            entry_expediente.insert(0, registro[2])
            opcion_seleccionada.set(registro[3])

        def editar_registro():
            if not selected_expediente:
                messagebox.showwarning("Advertencia", "Selecciona un registro para editar.")
                return

            conn = conectar_bd()
            cursor = conn.cursor()
            sql = """
            UPDATE consultas
            SET fecha = %s, direccion = %s, motivo = %s, etiqueta = %s
            WHERE expediente = %s
            """
            try:
                cursor.execute(sql, (
                    entry_fecha.get(),
                    entry_direccion.get(),
                    entry_motivo.get(),
                    opcion_seleccionada.get(),
                    selected_expediente
                ))
                conn.commit()
                cargar_datos_en_tabla()
                messagebox.showinfo("Éxito", "Registro editado correctamente.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo editar el registro: {e}")
            finally:
                cursor.close()
                conn.close()

        def eliminar_registro():
            if not selected_expediente:
                messagebox.showwarning("Advertencia", "Selecciona un registro para eliminar.")
                return

            conn = conectar_bd()
            cursor = conn.cursor()
            sql = "DELETE FROM consultas WHERE expediente = %s"
            try:
                cursor.execute(sql, (selected_expediente,))
                conn.commit()
                cargar_datos_en_tabla()
                messagebox.showinfo("Éxito", "Registro eliminado correctamente.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo eliminar el registro: {e}")
            finally:
                cursor.close()
                conn.close()

        boton_agregar = tk.Button(marco_principal, text="➕  Agregar", font=("Arial", 13), width=16, bd=0,
                    highlightthickness=1, highlightbackground="#dc860b", bg="black", fg="white", command=agregar_registro)
        boton_agregar.grid(row=1,column=4, padx=5, pady=5)
        
        def cargar_datos_en_tabla():
            conn = conectar_bd()
            cursor = conn.cursor()
            sql = "SELECT fecha, direccion, expediente, etiqueta FROM consultas"
            
            try:
                cursor.execute(sql)
                registros = cursor.fetchall()  # Obtiene todas las consultas
                for row_idx, registro in enumerate(registros, start=1):  # Empieza en la fila 1 (después del encabezado)
                    for col_idx, dato in enumerate(registro):
                        entry = tk.Entry(tabla_frame, bg="#324774", fg="white", borderwidth=1,
                                        highlightbackground="white", highlightcolor="white", width=45)
                        entry.grid(row=row_idx, column=col_idx, sticky="nsew")
                        entry.insert(0, str(dato))  # Inserta el dato en formato texto
                        entry.bind("<Button-1>", lambda e, r=registro: seleccionar_registro(r))

            except Exception as e:
                messagebox.showerror("Error", f"No se pudieron cargar los datos: {e}")
            finally:
                cursor.close()
                conn.close()

        boton_actualizar = tk.Button(marco_principal, text="🔄  Actualizar", font=("Arial", 13), width=16, bd=0,
                    highlightthickness=1, highlightbackground="#dc860b", bg="black", fg="white", command=cargar_datos_en_tabla)
        boton_actualizar.grid(row=2,column=4, padx=5, pady=5)

        boton_editar = tk.Button(marco_principal, text="✏️      Editar", font=("Arial", 13), width=16, bd=0,
                    highlightthickness=1, highlightbackground="#dc860b", bg="black", fg="white", command=editar_registro)
        boton_editar.grid(row=3,column=4, padx=5, pady=5)

        boton_eliminar = tk.Button(marco_principal, text="🗑️ Eliminar", font=("Arial", 13), width=16, bd=0,
                    highlightthickness=1, highlightbackground="#dc860b", bg="black", fg="white", command=eliminar_registro)
        boton_eliminar.grid(row=4,column=4, padx=5, pady=5)

        tabla_frame= tk.Frame(marco_principal, bg=color_azul)
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
        cargar_datos_en_tabla()

    def menu_pantalla():
        limpiar_marco()  # Limpia el marco principal
        mensaje = tk.Label(marco_principal, text="Este es el menú principal", font=("Arial", 20), 
                       bg=color_azul, fg="white", padx=10, pady=10)
        mensaje.pack()
        
    def ver_datos():
        limpiar_marco()  # Limpia el marco principal
        tabla_frame= tk.Frame(marco_principal, bg=color_azul)
        tabla_frame.grid(row=3, column=0, sticky="nsew", padx=10, pady=10, columnspan=6)
        marco_principal.rowconfigure(3, weight=6)

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
                            highlightbackground="white", height=35)  
        text_fila_3.grid(row=3, column=0, columnspan=len(headers), sticky="nsew") 
        
        conn = conectar_bd()
        cursor = conn.cursor()
        sql = "SELECT fecha, direccion, expediente, etiqueta FROM consultas"
            
        try:
            cursor.execute(sql)
            registros = cursor.fetchall()  # Se obtiene todas las consultas
            for row_idx, registro in enumerate(registros, start=1):  # Empieza en la fila 1 (después del encabezado)
                for col_idx, dato in enumerate(registro):
                    # Crea un nuevo Entry en la celda correspondiente
                    entry = tk.Entry(tabla_frame, bg="#324774", fg="white", borderwidth=1,
                                    highlightbackground="white", highlightcolor="white", width=45)
                    entry.grid(row=row_idx, column=col_idx, sticky="nsew")
                    entry.insert(0, str(dato))  # Inserta el dato en formato texto
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron cargar los datos: {e}")
        finally:
            cursor.close()
            conn.close()
        
    icono_label = tk.Label(marco_menu, text="👤", font=("Arial", 30), bg=color_naranja, fg=color_blanco)
    icono_label.pack(anchor="n", padx=20, pady=(10, 5))

    tk.Label(marco_menu,bg=color_naranja,text="\n\n\n").pack(anchor="w", padx=20, pady=5)

    boton_menu = tk.Button(marco_menu, text="🏚️ Menú", compound="left", font=("Arial", 20), 
                           bg=color_naranja, fg=color_blanco, bd=0, command=menu_pantalla)
    boton_menu.pack(anchor="w", padx=20, pady=(10, 5))

    boton_carga = tk.Button(marco_menu, text="✏️    Carga", compound="left", font=("Arial", 20), 
                            bg=color_naranja, fg=color_blanco, bd=0, command=Carga)
    boton_carga.pack(anchor="w", padx=20, pady=5)

    boton_ver_datos = tk.Button(marco_menu, text="🔍   Ver datos",  compound="left", font=("Arial", 20), bg=color_naranja, fg=color_blanco, bd=0, command=ver_datos)
    boton_ver_datos.pack(anchor="w", padx=20, pady=5)

    tk.Label(marco_menu,bg=color_naranja,text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n").pack(anchor="w", padx=20, pady=5)

    linea = tk.Frame(marco_menu, height=2, bg=color_blanco)
    linea.pack(fill="x", padx=20, pady=(5, 10))

    boton_cerrar_sesion = tk.Button(marco_menu, text="🚪 Cerrar sesión", command=cerrar_sesion, compound="left", 
                                     font=("Arial", 20), bg=color_naranja, fg=color_blanco, bd=0)
    boton_cerrar_sesion.pack(anchor="w", padx=20, pady=(5, 20))

pantalla_anteultima()
root.mainloop()