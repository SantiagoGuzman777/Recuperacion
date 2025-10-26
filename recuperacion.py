

# Programa para simular la recolección de datos de clientes y productos
# sin necesidad de usar una base de datos.
# Es decir, todo se guarda en memoria mientras se ejecuta el programa.

# === Registro de Cliente ===
print("=== REGISTRO DE CLIENTE ===")  # Muestra un título en pantalla

# Se piden los datos básicos del cliente
nombre_cliente = input("Ingrese el nombre del cliente: ")  # Guarda el nombre del cliente
correo_cliente = input("Ingrese el correo del cliente: ")  # Guarda el correo del cliente
telefono_cliente = input("Ingrese el teléfono del cliente: ")  # Guarda el teléfono del cliente

print("\nCliente registrado correctamente.\n")  # Mensaje de confirmación

# === Registro de Productos ===
print("=== REGISTRO DE PRODUCTOS ===")

productos = []  # Lista vacía para guardar los productos (cada producto será un diccionario)

# Bucle principal que permite ingresar varios productos
while True:
    # Se pide el nombre del producto
    nombre_producto = input("Ingrese el nombre del producto (o 0 para finalizar): ")

    # Si el usuario escribe "0", se detiene el ciclo con break
    if nombre_producto == "0":
        break  # Sale del bucle while principal

    # --- Validar precio positivo ---
    while True:
        try:
            # Se intenta convertir lo ingresado a número decimal (float)
            precio = float(input("Ingrese el precio del producto: "))
            # Si el número es mayor que 0, se acepta
            if precio > 0:
                break
            else:
                # Si el número no es positivo, muestra error
                print(" El precio debe ser un número positivo. Intente de nuevo.")
        except ValueError:
            # Si el usuario no escribe un número válido, se muestra un error
            print(" Debe ingresar un valor numérico. Intente de nuevo.")

    # --- Validar cantidad válida ---
    while True:
        try:
            # Se intenta convertir lo ingresado a número entero
            cantidad = int(input("Ingrese la cantidad disponible: "))
            # Si la cantidad es 0 o mayor, se acepta
            if cantidad >= 0:
                break
            else:
                # Si la cantidad es negativa, se muestra error
                print(" La cantidad no puede ser negativa. Intente de nuevo.")
        except ValueError:
            # Si el usuario no ingresa un número entero, se muestra error
            print(" Debe ingresar un número entero. Intente de nuevo.")

    # --- Guardar producto ---
    # Se crea un diccionario con los datos del producto
    producto = {
        "nombre": nombre_producto,  # Clave "nombre" guarda el nombre del producto
        "precio": precio,           # Clave "precio" guarda el valor numérico del producto
        "cantidad": cantidad        # Clave "cantidad" guarda cuántos hay disponibles
    }

    # El diccionario del producto se agrega a la lista de productos
    productos.append(producto)

    # Confirmación de que se guardó bien
    print(" Producto agregado correctamente.\n")

# === Mostrar información registrada ===
print("\n=== INFORMACIÓN REGISTRADA ===")

# Muestra los datos del cliente
print(f"Cliente: {nombre_cliente}")
print(f"Correo: {correo_cliente}")
print(f"Teléfono: {telefono_cliente}")

# Muestra los productos asociados a ese cliente
print("\nProductos asociados:")

# Si no se registró ningún producto, muestra un mensaje
if len(productos) == 0:
    print("No se registraron productos.")
else:
    # Contador para numerar los productos
    contador = 1
    # Recorre la lista de productos uno por uno
    for p in productos:
        # Imprime la información de cada producto usando el contador
        print(f"\nProducto #{contador}")
        print(f"Nombre: {p['nombre']}")
        # :.2f muestra el precio con dos decimales (por ejemplo: 3000.00)
        print(f"Precio: ${p['precio']:.2f}")
        print(f"Cantidad disponible: {p['cantidad']}")
        contador += 1  # Aumenta el número para el siguiente producto

print ("\n Registro completado con éxito.")  # Mensaje final de éxito