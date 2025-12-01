import tkinter as tk
from tkinter import scrolledtext, messagebox
from datetime import datetime

inventario = [
    {"id": "0001", "product": "FNAF 4", "genre": "Terror", "price": "150$mxn", "stock": 16, "additional details": "weight: 2 GB"},
    {"id": "0002", "product": "Los Sims 4", "genre": "Juego de Rol", "price": "350$mxn", "stock": 10, "additional details": "weight: 25 GB"},
    {"id": "0003", "product": "Minecraft:Java|Bedrock edition", "género": "RPG", "price": "170$mxn", "stock": 7, "additional details": "weight: 5 GB"},
    {"id": "0004", "product": "Nintendo Switch OLED", "price": "4,999$mxn", "stock": 10, "additional details": "Color: Neon"},
    {"id": "0005", "product": "Play Station 5 Slim", "price": "7,899$mxn", "stock": 7, "additional details": "Color:Cobalt Blue"},
    {"id": "0006", "product": "Pay Station 5 Slim", "price": "7,899$mxn", "stock": 5, "additional details": "Color: Sterling Silver"},
    {"id": "0007", "product": "Play Station Dualsense", "price": "1,499$mxn", "stock": 18, "additional details": "Color: white"},
    {"id": "0008", "product": "Nintendo Switch Pro-Controller", "price": "2,499$mxn", "stock": 2, "additional details": "Color: Black"},
    {"id": "0009", "product": "Hyper X wireless mouse", "price": "1,399$mxn", "stock": 6, "additional details": "Color: Black"},
    {"id": "0010", "product": "Hyper X wireless headset", "price": "4,999$mxn", "stock": 9, "additional details": "Color: Midnight"}
]

historial_ventas = []
STOCK_MINIMO = 3

# Funciones
def mostrar_bienvenida():
    """Muestra la pantalla de bienvenida con estadísticas rápidas"""
    global boton_activo
    texto.delete(1.0, tk.END)
    activar_boton(btn_home)

    total_modelos = len(inventario)
    total_productos = sum(t['stock'] for t in inventario)
    ventas_hoy = sum(1 for v in historial_ventas if datetime.strptime(v['fecha'], "%d/%m/%Y %H").date() == datetime.now().date())
    productos_stock_bajo = sum(1 for t in inventario if t['stock'] > 0 and t['stock'] <= STOCK_MINIMO)

    texto.insert(tk.END, "----------------------------------------\n\n")
    texto.insert(tk.END, "Welcome to Game Vault Store!\n\n")
    texto.insert(tk.END, "----------------------------------------\n\n")

    texto.insert(tk.END, "QUICK PREVIEW:\n\n", "título")
    texto.insert(tk.END,f"Unique Models!: {total_modelos}\n")
    texto.insert(tk.END, f"Products available!: {total_productos}\n")
    texto.insert(tk.END, f"Today sales: {ventas_hoy}\n")

    if productos_stock_bajo > 0:
        texto.insert(tk.END, f"LOW STOCK...!: {productos_stock_bajo} Products need an urgent restock!")
    else:
        texto.insert(tk.END, "No adjustments needed!\n")

    texto.insert(tk.END, "\nSelect a menu option to continue...\n")

def activar_boton(boton):
    """Actualiza el color del botón activo"""
    global boton_activo

    for btn in [btn_home, btn1, btn2, btn3, btn4]:
        btn.config(bg= "#000000")

    if boton:
        boton.config(bg= "#ff4500")
        boton_activo = boton

def on_enter(e, boton):
    if boton != boton_activo:
        boton.config(bg= "#ff4500")

def on_leave(e,boton):
    if boton != boton_activo:
        boton.config(bg="#000000")

ventana = tk.Tk()
ventana.title(" .-° GameVault Store °-.")
ventana.geometry("1200x800")
ventana.configure(bg= "#2D2D2D")

boton_activo = None

titulo = tk.Label(ventana, text= " .-° GAMEVAULT STORE °-.",
                  font=("Helvetica", 32, "bold"), bg="#2D2D2D", fg="#f5f5f5")
titulo.pack(pady=20)

subtitulo = tk.Label(ventana, text="INVENTORY AND SALES GESTION SYSTEM",
                     font=("Helvetica", 12), bg="#2D2D2D", fg="#D4D4D4")
subtitulo.pack()

frame_botones = tk.Frame(ventana, bg="#f5f5f5")
frame_botones.pack(pady=20)

btn_style = {"font": ("Albert Sans", 11, "bold"), "bg": "#000000", "fg": "white",
             "width": 12, "height": 2, "cursor": "hand2", "relief": tk.FLAT, "bd": 0}


btn_home = tk.Button(frame_botones, text = "HOME", command=mostrar_bienvenida, **btn_style)
btn_home.grid(row=0, column=0, padx=8)
btn1 = tk.Button(frame_botones, text= "INVENTORY", command=lambda: messagebox.showinfo("Info", "Función disponible en Día 2 (Martes)"), **btn_style)
btn1.grid(row=0, column=1, padx=8)
btn2 = tk.Button(frame_botones, text= "ADD", command=lambda: messagebox.showinfo("Info", "Función disponible en Día 2 (Martes)"), **btn_style)
btn2.grid(row=0, column=2, padx=8)
btn3 = tk.Button( frame_botones, text= "SELL", command=lambda: messagebox.showinfo("Info", "Función disponible en Día 2 (Martes)"), **btn_style)
btn3.grid(row=0, column=3, padx=8)
btn4 = tk.Button(frame_botones, text= "SEARCH", command=lambda: messagebox.showinfo("Info", "Función disponible en Día 2 (Martes)"), **btn_style)
btn4.grid(row=0, column=4, padx=8)
for btn in [btn_home, btn1, btn2, btn3, btn4]:
    btn.bind("<Enter>", lambda e, b=btn: on_enter(e,b))
    btn.bind("<Leave>", lambda e, b=btn: on_leave(e,b))

texto = scrolledtext.ScrolledText(ventana,
                                  font= ("Open Sans", 11),
                                  bg="#ffffff", fg="#000000",
                                  height=18,
                                  padx=20, pady=20,
                                  relief=tk.SOLID, bd=1)
texto.pack(padx=30, pady=15, fill=tk.BOTH, expand=True)

texto.tag_config("título", font=("OpenSans", 11, "bold"), foreground="#000000")
texto.tag_config("alerta", background="#ffe5e5", foreground="#ff4500", font=("Open Sans", 11, "bold"))
texto.tag_config("agotado", background="#fddede", foreground="#cc0000", font=("Open Sans", 11, "bold"))

footer = tk.Label(ventana, text="2025 GameVault Store | DÍA 1 (LUNES) - Interfaz Base y HOME",
                  font=("Helvetica", 10), bg="#f5f5f5", fg="#999999")
footer.pack(pady=10)

mostrar_bienvenida()
ventana.mainloop()