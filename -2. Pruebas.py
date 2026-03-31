import tkinter as tk
from tkinter import messagebox

# =========================
# CONFIGURACIÓN PRINCIPAL
# =========================
ventana = tk.Tk()
ventana.title("⚔️ El Camino del Valhalla 🛡️")
ventana.geometry("600x400")
ventana.resizable(False, False)

# =========================
# VARIABLES DEL JUEGO
# =========================
vida = 100

# =========================
# UI ELEMENTS
# =========================
texto = tk.Label(ventana, text="", wraplength=500, justify="center", font=("Arial", 12))
texto.pack(pady=30)

frame_botones = tk.Frame(ventana)
frame_botones.pack()

# =========================
# FUNCIONES BASE
# =========================
def limpiar_botones():
    for widget in frame_botones.winfo_children():
        widget.destroy()

def mostrar_opciones(opciones):
    limpiar_botones()
    for texto_btn, funcion in opciones:
        tk.Button(frame_botones, text=texto_btn, width=25, command=funcion).pack(pady=5)

def game_over(mensaje):
    limpiar_botones()
    texto.config(text=mensaje)
    messagebox.showinfo("Fin del juego", mensaje)
    mostrar_opciones([("Reiniciar 🔄", inicio)])

# =========================
# HISTORIA
# =========================
def inicio():
    global vida
    vida = 100
    texto.config(text=(
        "Eres un joven guerrero vikingo que despierta en una aldea destruida 🔥\n"
        "Debes sobrevivir y descubrir quién atacó tu hogar."
    ))
    mostrar_opciones([
        ("Hacha 🪓", ruta_hacha),
        ("Escudo 🛡️", ruta_escudo)
    ])

# =========================
# RUTA HACHA
# =========================
def ruta_hacha():
    texto.config(text="Te adentras en el bosque oscuro... Un ruido aparece.")
    mostrar_opciones([
        ("Investigar 🔍", investigar),
        ("Huir 🏃", huir),
        ("Emboscada ⚔️", emboscada)
    ])

def investigar():
    texto.config(text="Encuentras un guerrero herido...")
    mostrar_opciones([
        ("Interrogar ❓", interrogar),
        ("Ignorar 🚶", ignorar)
    ])

def ignorar():
    game_over("Te atacan por la espalda. Has muerto 😔")

def interrogar():
    texto.config(text="Te da información clave...")
    mostrar_opciones([
        ("Matar ⚔️", matar),
        ("Perdonar 🤝", perdonar)
    ])

def perdonar():
    game_over("Te traiciona y mueres 😔")

def matar():
    texto.config(text="Encuentras el campamento enemigo 🔥")
    mostrar_opciones([
        ("Atacar ⚔️", atacar),
        ("Infiltrarse 🕶️", infiltrar),
        ("Observar 👀", observar)
    ])

def atacar():
    game_over("Te rodean y mueres en combate 😔")

def infiltrar():
    game_over("Eliminas al líder. ¡Victoria! 🛡️🔥")

def observar():
    texto.config(text="Descubres una conspiración mayor...")
    mostrar_opciones([("Continuar...", inicio)])

# =========================
# EMBOSCADA
# =========================
def emboscada():
    texto.config(text="Preparas una emboscada...")
    mostrar_opciones([
        ("Atacar ahora ⚔️", atacar),
        ("Esperar ⏳", victoria_emboscada),
        ("Retirarte 🔙", retirada)
    ])

def victoria_emboscada():
    game_over("Victoria total. Vengaste tu aldea 🛡️🔥")

def retirada():
    game_over("Pierdes tu oportunidad 😔")

def huir():
    game_over("Huyes y pierdes tu honor 😔")

# =========================
# RUTA ESCUDO
# =========================
def ruta_escudo():
    texto.config(text="Avanzas con cautela...")
    mostrar_opciones([
        ("Contraatacar ⚔️", contraataque),
        ("Huir 🏃", huir)
    ])

def contraataque():
    texto.config(text="Derrotas al enemigo y encuentras un mapa 🗺️")
    mostrar_opciones([
        ("Seguir mapa 🧭", fortaleza),
    ])

def fortaleza():
    texto.config(text="Llegas a la fortaleza final 🏰")
    mostrar_opciones([
        ("Asaltar ⚔️", atacar),
        ("Esperar ⏳", victoria_final),
        ("Entrada secreta 🕵️", trampa)
    ])

def victoria_final():
    game_over("Has vengado tu aldea. Valhalla te espera 🛡️🔥")

def trampa():
    game_over("Caes en una trampa 😔")

# =========================
# INICIAR JUEGO
# =========================
inicio()
ventana.mainloop()