import tkinter as tk
from PIL import Image, ImageTk

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inicio de sesión - Municipalidad Tres de Febrero")
        self.root.geometry("400x500")
        # Colores de la interfaz
        self.color_azul = "#324774"  # Fondo principal azul
        self.color_naranja = "#dc860b"  # Botón naranja
        self.color_blanco = "#FFFFFF"  # Texto y bordes blancos

        # Crear el marco principal
        self.marco = tk.Frame(self.root, bg=self.color_azul)
        self.marco.pack(expand=True, fill="both")

        self.crear_interfaz()

    def crear_interfaz(self):
        # Logo "3F"
        ruta_logo = "IMG-3F.jpeg"
        imagen_logo = Image.open(ruta_logo)
        imagen_logo = imagen_logo.resize((80, 80))  # Tamaño del logo
        self.logo_img = ImageTk.PhotoImage(imagen_logo)

        logo = tk.Label(self.marco, image=self.logo_img, bg=self.color_azul)
        logo.pack(pady=(10, 5))

        # Títulos
        titulo = tk.Label(self.marco, text="Inicio de sesión", font=("Arial", 22, "bold"),
                          fg=self.color_blanco, bg=self.color_azul)
        titulo.pack(pady=(0, 5))

        subtitulo = tk.Label(self.marco, text="Municipalidad Tres de Febrero", font=("Arial", 12),
                             fg=self.color_blanco, bg=self.color_azul)
        subtitulo.pack(pady=(0, 20))

        # Campos de entrada
        self.crear_campo("Usuario", es_contraseña=False)
        self.crear_campo("Contraseña", es_contraseña=True)

        # Botón "Iniciar Sesión"
        boton_login = tk.Button(self.marco, text="Iniciar Sesión", font=("Arial", 14),
                                bg=self.color_naranja, fg=self.color_blanco, width=22, height=1, bd=0, relief="flat")
        boton_login.pack(pady=(100, 0))

    def crear_campo(self, placeholder, es_contraseña=False):
        frame = tk.Frame(self.marco, bg=self.color_azul)
        frame.pack(pady=(0, 5), padx=20)

        # Campo de entrada
        entry = tk.Entry(frame, font=("Arial", 14), width=25,bd=0, fg="#a9a9a9", bg=self.color_azul)
        entry.insert(0, placeholder)
        entry.bind("<FocusIn>", lambda event: self.on_entry_click(event, entry, placeholder))
        entry.bind("<FocusOut>", lambda event: self.on_focusout(event, entry, placeholder))
        if es_contraseña:
            tk.Label(frame, text="🔒", font=("Arial", 14), fg=self.color_blanco, bg=self.color_azul).pack(side="left")
            entry.config(show="*")
        else:
            tk.Label(frame, text="👤", font=("Arial", 14), fg=self.color_blanco, bg=self.color_azul).pack(side="left")
        entry.pack(side="left", padx=5)

        # Renglón debajo del campo
        renglon = tk.Frame(self.marco, height=1, width=entry.winfo_reqwidth()+ 22, bg=self.color_blanco)
        renglon.pack(pady=(0, 10))

    def on_entry_click(self, event, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, "end")
            entry.config(fg=self.color_blanco)

    def on_focusout(self, event, entry, placeholder):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(fg="#a9a9a9")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("450x550")
    app = LoginApp(root)
    root.mainloop()
