import tkinter as tk
from tkinter import scrolledtext, messagebox, simpledialog # Día 2 agregamos simpledialog
from datetime import datetime

inventario = [
    {"id": "0001", "product": "FNAF 4", "genre": "Horror", "price": 150, "stock": 16, "additional details": "weight: 2 GB"},
    {"id": "0002", "product": "Los Sims 4", "genre": "Roleplay", "price": 350, "stock": 10, "additional details": "weight: 25 GB"},
    {"id": "0003", "product": "Minecraft:Java|Bedrock edition", "genre": "RPG", "price": 170, "stock": 7, "additional details": "weight: 5 GB"},
    {"id": "0004", "product": "Nintendo Switch OLED", "genre": "Console", "price": 4999, "stock": 10, "additional details": "Color: Neon"},
    {"id": "0005", "product": "Play Station 5 Slim", "genre": "Console", "price": 7899, "stock": 7, "additional details": "Color:Cobalt Blue"},
    {"id": "0006", "product": "Pay Station 5 Slim", "genre": "Console", "price": 7899, "stock": 5, "additional details": "Color: Sterling Silver"},
    {"id": "0007", "product": "Play Station Dualsense", "genre": "Controller", "price": 1499, "stock": 18, "additional details": "Color: white"},
    {"id": "0008", "product": "Nintendo Switch Pro-Controller", "genre": "Controller", "price": 2499, "stock": 2, "additional details": "Color: Black"},
    {"id": "0009", "product": "Hyper X wireless mouse", "genre": "Computer Mouse", "price": 1399, "stock": 6, "additional details": "Color: Black"},
    {"id": "0010", "product": "Hyper X wireless headset", "genre": "Gamer Headset", "price": 4999, "stock": 9, "additional details": "Color: Midnight"}
]

historial_ventas = []
STOCK_MINIMO = 3

# Día 1
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

# Día 2
def validar_numero_positivo(valor, nombre_campo):
    """Valida que el valor sea un número positivo."""
    try:
        num = float(valor)
        if num < 0:
            messagebox.showerror("Validation Error", f"The field '{nombre_campo}' cannot be negative.")
            return None
        return num
    except ValueError:
        messagebox.showerror("Validation Error", f"The field '{nombre_campo}' has to be a valid number")
        return None

# Día 2
def generar_nuevo_id():
    """Genera un nuevo ID consecutivo basado en el ID númerico más alto actual"""
    if not inventario:
        return "001"
    
    max_id = 0
    for products in inventario:
        try:
            num_id = int(products['id'])
            if num_id > max_id:
                max_id = num_id
        except ValueError:
            continue
        
    return str(max_id + 1).zfill(3)

# Día 2
def mostrar_inventario():
    """Muestra el listado completo del inventario"""
    texto.delete(1.0, tk.END)
    texto.insert(tk.END, "= FULL INVENTORY =\n\n")
    activar_boton(btn1)

    if not inventario:
        texto.insert(tk.END, "X There is no products in the inventory\n")
    else:
        texto.insert(tk.END, f"{'ID':<4} | {'PRODUCT':<25} | {'GENRE': <2} | {'PRICE':<10} | {'STOCK':<5}")
        texto.insert(tk.END, "-"*70 + "\n")

        for products in inventario:
            linea = f"{products['id']:<4} | {products['product']:<25} | {products['genre']: <2} | {products['price']:<10} | {products['stock']:<5}"
            texto.insert(tk.END, linea)

            if products['stock'] > 0 and products['stock'] <= STOCK_MINIMO:
                texto.insert(tk.END, "LOW STOCK", "ALERT")
            elif products['stock'] == 0:
                texto.insert(tk.END, "SOLD OUT", "sold out")

            texto.insert(tk.END, "\n")

        texto.insert(tk.END, "\nUse button 'ADD' to incorporate new products. \n")

# Día 2
def agregar_producto():
    """Agrega un nuevo producto al inventario."""
    activar_boton(btn2)
    new_id = generar_nuevo_id()

    product = simpledialog.askstring("Add Product", "1. Product name (mandatory):", parent=ventana)
    if not product: return

    genre = simpledialog.askstring("Add Product", "2. If it is a videogame, insert the genre. If it is an accesory, specify it (mandatory):", parent=ventana)
    if not genre: return

    price_str = simpledialog.askstring("Add product", "3. Unitary price (mandatory):", parent=ventana)
    if not price_str: return
    validaded_price = validar_numero_positivo(price_str, "Price")

    stock_str = simpledialog.askstring("Add product", "4. Initial quantity (stock) (mandatory):", parent=ventana)
    if not stock_str: return
    validaded_stock = validar_numero_positivo(stock_str, "Initial quantity")
    if validaded_stock is None: return

    additional_details = simpledialog.askstring("Add Product", "5. Additional details (optional):", parent=ventana)

    new_product = {
        "id": new_id,
        "product": product,
        "genre": genre if genre else "none",
        "price": float(validaded_price),
        "stock": int(validaded_stock),
        "additional details": additional_details if additional_details else "none"
    }

    inventario.append(new_product)

    messagebox.showinfo("Congratulations!", f"'{product}' added with the ID {new_id} to the inventory!")

# Día 3
def buscar_producto():
    """Busca un producto en el inventario por ID, Producto o Género"""
    activar_boton(btn4)

    if not inventario:
        messagebox.showwarning("Error", "No similar product available... try again", parent=ventana)
        return
    
    criterio_busqueda = simpledialog.askstring("Search Product",
                                           "Search by: ID, Product name or Genre:",
                                           parent=ventana)
    
    if not criterio_busqueda:
        return
    
    criterio = criterio_busqueda.lower()
    resultados=[]

    for products in inventario:
        if (criterio in products['id'].lower() or
            criterio in products['product'].lower() or
            criterio in products['genre'].lower()):
            resultados.append(products)

    texto.delete(1.0, tk.END)
    texto.insert(tk.END, f"SEARCH RESULT: '{criterio_busqueda}' ===\n\n")

    if not resultados:
        texto.insert(tk.END, "X No result found")
    else:
        texto.insert(tk.END, f"Perfect! {len(resultados)} product(s) matched your search:\n\n")
        texto.insert(tk.END, f"{'ID':<4} | {'PRODUCT':<25} | {'GENRE':<2} | {'PRICE':<10} | {'STOCK':<5}\n")
        texto.insert(tk.END, "-"*70 + "\n")

    for products in resultados:
        línea = f"{products['id']:<4} | {products['product']:<25} | {products['genre']:<2} | ${products['price']:<10} | {products['stock']:<5}"
        texto.insert(tk.END, línea)

        if products['stock'] > 0 and products['stock'] <= STOCK_MINIMO:
            texto.insert(tk.END, " LOW STOCK", "warning")
        elif products['stock'] == 0:
            texto.insert(tk.END, "SOLD OUT", "sold out")

        texto.insert(tk.END, "\n")

# Día 3
def vender_producto():
    """Registra una venta de productos y actualiza el inventario. """
    activar_boton(btn3)

    if not inventario:
        messagebox.showwarning("Unavailable Inventory", "There are no products left to sell", parent=ventana)
        return
    
    opciones = "\n".join([f"{i+1}. ID:{t['id']} - {t['product']} ({t['genre']}) - Stock: {t['stock']}" for i, t in enumerate(inventario)])
    seleccion = simpledialog.askinteger("Sell Product", f"Select the product number to sell:\n\n{opciones}", parent=ventana)

    if not seleccion or seleccion <1 or seleccion > len(inventario):
        if seleccion is not None: messagebox.showerror("Error", "Invalid Selection")
        return
    
    producto_a_vender = inventario[seleccion - 1]

    if producto_a_vender['stock'] <= 0:
        messagebox.showwarning("Stock unavailable", "This product is sold out", parent=ventana)
        return
    
    cantidad_str = simpledialog.askstring("Sell Product", f"¿How many units of '{producto_a_vender['product']} do you want to sell?", parent=ventana)
    if not cantidad_str: return

    cantidad_validada = validar_numero_positivo(cantidad_str, "Quantity to sell")
    if cantidad_validada is None: return
    cantidad = int(cantidad_validada)

    if cantidad > producto_a_vender['stock']:
        messagebox.showerror("Sell Error", f"There are {producto_a_vender['stock']} units available. {cantidad} cant be sold.", parent=ventana)
        return
    
    monto_total = cantidad * producto_a_vender['price']
    
    producto_a_vender['stock'] -= cantidad

    registro_venta = {
    "date": datetime.now().strftime("%d/%m/%Y %H:%M"),
    "product_id": producto_a_vender['id'],
    "product name": producto_a_vender['product'],
    "quantity": cantidad,
    "unitary_price": producto_a_vender['price'],
    "total": monto_total
    }
    
    historial_ventas.append(registro_venta)

    messagebox.showinfo("Registered Sale",
                        f"It was sold {cantidad} units of '{producto_a_vender['product']}'\n"
                        f"Total amount: ${monto_total:,.2f}")
    
    mostrar_resumen_venta(registro_venta)

# Día 3
def mostrar_resumen_venta(venta):
    """Muestra el resumen detallado de la venta realizada."""
    texto.delete(1.0, tk.END)
    texto.insert(tk.END, "= REGISTERED PURCHASE =\n\n")

    texto.insert(tk.END, "PURCHASE DETAILS: \n", "title")
    texto.insert(tk.END, f"Date: {venta['date']}\n")
    texto.insert(tk.END, f"Product ID: {venta['product_id']}\n")
    texto.insert(tk.END, f"Product Name: {venta['product name']}\n")
    texto.insert(tk.END, f"Unitary price: ${venta['unitary_price']:,.2f}\n")
    texto.insert(tk.END, f"TOTAL: ${venta['total']:1,.2f}\n", "total")

    texto.insert(tk.END, "\nPurchase registered succesfully!\n")

# Día 1
def activar_boton(boton):
    """Actualiza el color del botón activo"""
    global boton_activo

    for btn in [btn_home, btn1, btn2, btn3, btn4]:
        btn.config(bg= "#000122")

    if boton:
        boton.config(bg= "#6F87D6")
        boton_activo = boton

def on_enter(e, boton):
    if boton != boton_activo:
        boton.config(bg= "#6F87D6")

def on_leave(e,boton):
    if boton != boton_activo:
        boton.config(bg="#000122")

ventana = tk.Tk()
ventana.title(" ✰ GAMEVAULT STORE ✰")
ventana.geometry("1200x800")
ventana.configure(bg= "#272727")

boton_activo = None

titulo = tk.Label(ventana, text= "˚ ᯓ★ ˖ ۫ ִ GAMEVAULT STORE  ۫ ִ ˖ ★ᯓ ˖ ۫ ִ",
                  font=("Aptos Slab Black", 32, "bold"), bg="#272727", fg="#f5f5f5")
titulo.pack(pady=20)

subtitulo = tk.Label(ventana, text="INVENTORY AND SALES GESTION SYSTEM",
                     font=("Calibri Light", 12), bg="#272727", fg="#f5f5f5")
subtitulo.pack()

frame_botones = tk.Frame(ventana, bg="#272727")
frame_botones.pack(pady=20)

btn_style = {"font": ("Calibri Light", 11, "bold"), "bg": "#000000", "fg": "white",
             "width": 12, "height": 2, "cursor": "hand2", "relief": tk.FLAT, "bd": 0}

# Día 2
btn_home = tk.Button(frame_botones, text = "HOME", command=mostrar_bienvenida, **btn_style)
btn_home.grid(row=0, column=0, padx=8)

# Día 2
btn1 = tk.Button(frame_botones, text= "INVENTORY", command=mostrar_inventario, **btn_style)
btn1.grid(row=0, column=1, padx=8)

# Día 2
btn2 = tk.Button(frame_botones, text= "ADD", command=agregar_producto, **btn_style)
btn2.grid(row=0, column=2, padx=8)

# Día 3
btn3 = tk.Button(frame_botones, text="SELL", command=vender_producto, **btn_style)
btn3.grid(row=0, column=3, padx=8)

# Día 3
btn4 = tk.Button(frame_botones, text="SEARCH", command=buscar_producto, **btn_style)
btn4.grid(row=0, column=4, padx=8)

for btn in [btn_home, btn1, btn2, btn3, btn4]:
    btn.bind("<Enter>", lambda e, b=btn: on_enter(e,b))
    btn.bind("<Leave>", lambda e, b=btn: on_leave(e,b))

texto = scrolledtext.ScrolledText(ventana,
                                  font= ("Calibri Light", 11),
                                  bg="#ddd8d8", fg="#000000",
                                  height=18,
                                  padx=20, pady=20,
                                  relief=tk.SOLID, bd=1)
texto.pack(padx=30, pady=15, fill=tk.BOTH, expand=True)

texto.tag_config("title", font=("Calibri Light", 11, "bold"), foreground="#000000")
texto.tag_config("alert", background="#ffe5e5", foreground="#ff4500", font=("Calibri Light", 11, "bold"))
texto.tag_config("sold out", background="#fddede", foreground="#cc0000", font=("Calibri Light", 11, "bold"))
texto.tag_config("total", font=("Calibri Light", 12, "bold"), foreground="#008000")

# Día 3
footer = tk.Label(ventana, text="2025 GameVault Store | Created by: HAYUUN",
                  font=("Helvetica", 10), bg="#272727", fg="#E1E1E1")
footer.pack(pady=10)

mostrar_bienvenida()
ventana.mainloop()