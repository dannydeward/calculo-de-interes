import tkinter as tk

def calcular_rentabilidad():
    try:
        monto = float(entry_monto.get())
        porcentaje = float(entry_porcentaje.get())
        tasa_diaria = porcentaje / 100 / 360  # Tasa de interés diaria
        
        if tipo_inversion.get() == "Inversión Inmobiliaria":
            rentabilidad = monto * tasa_diaria * 365
        elif tipo_inversion.get() == "Plazo Fijo 30 días":
            rentabilidad = monto * tasa_diaria * 30
        elif tipo_inversion.get() == "Plazo Fijo 60 días":
            rentabilidad = monto * tasa_diaria * 60
        elif tipo_inversion.get() == "Plazo Fijo 90 días":
            rentabilidad = monto * tasa_diaria * 90
        else:
            resultado.config(text="Selecciona un tipo de inversión válido.")
            return
        
        resultado.config(text=f"Rentabilidad: {rentabilidad:.2f} {moneda.get()}")

    except ValueError:
        resultado.config(text="Por favor, ingresa valores numéricos.")

# Configuración de la interfaz
# Configuración de la interfaz
ventana = tk.Tk()
ventana.title("Calculadora de Rentabilidad")
ventana.geometry("400x400")  # Cambia las dimensiones según tus preferencias

# Etiqueta y entrada para el monto de la inversión
label_monto = tk.Label(ventana, text="Monto de la inversión:")
label_monto.pack(pady=8)

entry_monto = tk.Entry(ventana)
entry_monto.pack(pady=8)

# Etiqueta y entrada para el porcentaje de ganancia anual
label_porcentaje = tk.Label(ventana, text="Porcentaje de ganancia anual:")
label_porcentaje.pack(pady=8)

entry_porcentaje = tk.Entry(ventana)
entry_porcentaje.pack(pady=8)

# Etiqueta y entrada para la moneda
label_moneda = tk.Label(ventana, text="Moneda:")
label_moneda.pack(pady=8)

moneda = tk.StringVar()
entry_moneda = tk.Entry(ventana, textvariable=moneda)
entry_moneda.pack(pady=8)

# Opciones de tipo de inversión
label_tipo_inversion = tk.Label(ventana, text="Tipo de inversión:")
label_tipo_inversion.pack(pady=8)

tipos_inversion = ["Inversión Inmobiliaria", "Plazo Fijo 30 días", "Plazo Fijo 60 días", "Plazo Fijo 90 días"]
tipo_inversion = tk.StringVar()
tipo_inversion.set(tipos_inversion[0])  # Establecer el valor predeterminado

opcion_tipo_inversion = tk.OptionMenu(ventana, tipo_inversion, *tipos_inversion)
opcion_tipo_inversion.pack(pady=10)

# Botón para calcular rentabilidad
calcular_button = tk.Button(ventana, text="Calcular Rentabilidad", command=calcular_rentabilidad)
calcular_button.pack(pady=10)

# Resultado
resultado = tk.Label(ventana, text="")
resultado.pack(pady=30)

ventana.mainloop()
