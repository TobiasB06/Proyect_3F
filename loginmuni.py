import tkinter as tk
from PIL import Image, ImageTk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Inicio de sesión - Municipalidad Tres de Febrero")

# tamaño de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

# geometría de la ventana a tamaño de pantalla
ventana.geometry(f"{ancho_pantalla}x{alto_pantalla}")

# Iniciar en pantalla completa pero con botones de control
ventana.state("zoomed")

# Colores de la interfaz
color_azul = "#324774"  # Fondo principal azul
color_naranja = "#dc860b"  # Botón naranja
color_blanco = "#FFFFFF"  # Texto y bordes blancos

# Funciones para los marcadores de posición
def on_entry_click(event, entry, placeholder):
    if entry.get() == placeholder:
        entry.delete(0, "end")
        entry.config(fg=color_blanco)

def on_focusout(event, entry, placeholder):
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.config(fg="#a9a9a9")  # Color gris claro para el marcador de posición

# Función para mostrar/ocultar contraseña
def toggle_password():
    if contraseña_entry.cget('show') == '*':
        contraseña_entry.config(show='')
        ojo_btn.config(text="👁️")  # Cambiar a icono de "ojo abierto"
    else:
        contraseña_entry.config(show='*')
        ojo_btn.config(text="👁")  # Cambiar a icono de "ojo cerrado"

# Marco principal con fondo azul
marco = tk.Frame(ventana, bg=color_azul)
marco_width = 450
marco_height = 550
marco.place(relx=0.5, rely=0.5, anchor="center", width=marco_width, height=marco_height)

# Espacio para centrar el contenido
tk.Frame(marco, height=50, bg=color_azul).pack()

# Logo "3F"
ruta_logo = "Imagenes/IMG-3F.jpeg"  
imagen_logo = Image.open(ruta_logo)
imagen_logo = imagen_logo.resize((80, 80))  # tamaño del logo
logo_img = ImageTk.PhotoImage(imagen_logo)
logo = tk.Label(marco, image=logo_img, bg=color_azul)
logo.pack(pady=(10, 5))

# Títulos
titulo = tk.Label(marco, text="Inicio de sesión", font=("Arial", 22, "bold"), fg=color_blanco, bg=color_azul)
titulo.pack()
subtitulo = tk.Label(marco, text="Municipalidad Tres de Febrero", font=("Arial", 12), fg=color_blanco, bg=color_azul)
subtitulo.pack()

# Campo de usuario con ícono
usuario_frame = tk.Frame(marco, bg=color_azul)
usuario_frame.pack(pady=(20, 5))

usuario_icono = tk.Label(usuario_frame, text="👤", font=("Arial", 14), bg=color_azul, fg=color_naranja)
usuario_icono.pack(side="left", padx=5)

usuario_entry = tk.Entry(usuario_frame, font=("Arial", 14), width=24, bd=0, fg="#a9a9a9", bg=color_azul)
usuario_entry.insert(0, "Usuario")
usuario_entry.bind("<FocusIn>", lambda event: on_entry_click(event, usuario_entry, "Usuario"))
usuario_entry.bind("<FocusOut>", lambda event: on_focusout(event, usuario_entry, "Usuario"))
usuario_entry.pack(side="left", padx=5)

# Renglón debajo del campo de usuario
usuario_renglon = tk.Frame(marco, height=1, width=250, bg=color_blanco)
usuario_renglon.pack()

# Campo de contraseña con ícono y botón de ojo
contraseña_frame = tk.Frame(marco, bg=color_azul)
contraseña_frame.pack(pady=(20, 5))

contraseña_icono = tk.Label(contraseña_frame, text="🔒", font=("Arial", 14), bg=color_azul, fg=color_naranja)
contraseña_icono.pack(side="left", padx=5)

contraseña_entry = tk.Entry(contraseña_frame, font=("Arial", 14), show="*", width=22, bd=0, fg="#a9a9a9", bg=color_azul)
contraseña_entry.insert(0, "Contraseña")
contraseña_entry.bind("<FocusIn>", lambda event: on_entry_click(event, contraseña_entry, "Contraseña"))
contraseña_entry.bind("<FocusOut>", lambda event: on_focusout(event, contraseña_entry, "Contraseña"))
contraseña_entry.pack(side="left", padx=5)

# Botón de ojo para mostrar/ocultar la contraseña
ojo_btn = tk.Button(contraseña_frame, text="👁", font=("Arial", 12), bg=color_azul, fg=color_naranja, bd=0, command=toggle_password)
ojo_btn.pack(side="left", padx=5)

# Renglón debajo del campo de contraseña
contraseña_renglon = tk.Frame(marco, height=1, width=250, bg=color_blanco)
contraseña_renglon.pack()

# Botón "Iniciar Sesión"
boton_login = tk.Button(marco, text="Iniciar Sesión", font=("Arial", 14), bg=color_naranja, fg=color_blanco,
                        width=22, height=1, bd=0, relief="flat")
boton_login.pack(pady=(40, 0))

# Espacio para centrar el contenido
tk.Frame(marco, height=50, bg=color_azul).pack()

ventana.mainloop()
