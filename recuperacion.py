# ================================
# TEMA 1: VARIABLES
# Definición: Las variables guardan datos en memoria con un nombre.
# ================================

# 1) Guardar nombre y apellido
nombre = "Santiago"
apellido = "Guzmán"
print("Nombre completo:", nombre, apellido)

# 2) Guardar la edad
edad = 15
print("Edad:", edad)

# 3) Guardar un promedio con decimal
promed = 4.1
print("Promedio:", promed)

# 4) Guardar la ciudad
ciudad = "Palmira"
print("Vivo en", ciudad)

# 5) Guardar el país
pais = "Colombia"
print("Soy", nombre, apellido, "de", pais)

# 6) Variable booleana (verdadero o falso)
activo = True
print("¿Activo?:", activo)

# 7) Guardar la altura
altura = 1.70
print("Altura:", altura, "m")

# 8) Guardar curso
curso = "Python"
print("Curso:", curso)

# 9) Mostrar nombre y materia
materia = "Tecnología"
print(nombre + " estudia", materia)

# 10) Contador simple
visitas = 0
print("Visitas iniciales:", visitas)
visitas = visitas + 1
print("Visitas después de una entrada:", visitas)


# ======================================
# TEMA 2: OPERACIONES MATEMÁTICAS
# Definición: Permiten sumar, restar, multiplicar, dividir y más.
# ======================================

a = 10
b = 5

# 1) Suma
print("Suma:", a + b)

# 2) Resta
print("Resta:", a - b)

# 3) Multiplicación
print("Multiplicación:", a * b)

# 4) División
print("División:", a / b)

# 5) Módulo (residuo)
print("Residuo de a % 3:", a % 3)

# 6) Potencia
print("a al cuadrado:", a ** 2)

# 7) División entera
c = 15
d = 3
print("División entera:", c // d)

# 8) Operación con paréntesis
resultado = (a + b) * c
print("Operación combinada (a+b)*c:", resultado)

# 9) Suma total
suma_total = a + b + c + d
print("Suma total:", suma_total)

# 10) Promedio
promedio = suma_total / 4
print("Promedio:", promedio)


# ======================================
# TEMA 3: CONCATENACIÓN DE CADENAS
# Definición: Unir textos (strings) con + o comas.
# ======================================

# 1) Unir nombre y apellido
nombre = "Santiago"
apellido = "Guzmán"
full = nombre + " " + apellido
print("Nombre completo:", full)

# 2) Texto fijo y variable
animal = "gato"
print("Tengo un " + animal + " en casa")

# 3) Concatenar número convertido a texto
a = 5
b = 3
print("La suma de a y b es " + str(a + b))

# 4) Concatenar edad
anos = 15
print("Tengo " + str(anos) + " años")

# 5) Frase con varias palabras
p1 = "Python"
p2 = "es"
p3 = "genial"
print(p1 + " " + p2 + " " + p3)

# 6) Concatenación con salto de línea
fr1 = "Hola"
fr2 = "Mundo"
print(fr1 + "\n" + fr2)

# 7) Concatenación con coma
juego = "Fútbol"
print("Me gusta jugar", juego)

# 8) Repetir texto
letra = "A"
print("Repetir letra:", letra * 5)

# 9) Frase con ciudad
ciudad = "Palmira"
print("Vivo en la ciudad de " + ciudad)

# 10) Nombre completo y edad
print("Mi nombre es " + nombre + " " + apellido + " y tengo " + str(anos) + " años")


# ======================================
# TEMA 4: DICCIONARIOS
# Definición: Guardan datos en pares clave:valor.
# ======================================

# 1) Crear diccionario persona
persona = {"nombre": "Santiago", "apellido": "Guzmán", "edad": 15}
print("Diccionario persona:", persona)

# 2) Acceder por clave
print("Nombre:", persona["nombre"])

# 3) Agregar ciudad
persona["ciudad"] = "Palmira"
print("Agregué ciudad:", persona)

# 4) Modificar edad
persona["edad"] = 16
print("Edad actualizada:", persona["edad"])

# 5) Eliminar clave
del persona["ciudad"]
print("Diccionario sin ciudad:", persona)

# 6) Recorrer claves
for clave in persona:
    print("Clave:", clave)

# 7) Claves y valores
for clave, valor in persona.items():
    print(clave + ":", valor)

# 8) Obtener solo valores
print("Valores:", list(persona.values()))

# 9) Diccionario anidado
estudiante = {"nombre": "Santiago", "apellido": "Guzmán", "notas": {"mate": 4.5, "lenguaje": 4.1}}
print("Diccionario anidado:", estudiante)

# 10) Verificar clave
print("¿'edad' está en persona?", "edad" in persona)


# ======================================
# TEMA 5: TUPLAS
# Definición: Colección ordenada e inmutable (no se puede modificar).
# ======================================

# 1) Tupla de colores
colores = ("rojo", "verde", "azul")
print("Tupla colores:", colores)

# 2) Acceder por índice
print("Primer color:", colores[0])

# 3) Recorrer tupla
for c in colores:
    print("Color:", c)

# 4) Longitud
print("Tamaño de la tupla:", len(colores))

# 5) Tupla con varios tipos
datos = ("Santiago", "Guzmán", 15, 1.70)
print("Tupla datos:", datos)

# 6) Tupla anidada
tupla_anidada = (1, 2, (3, 4))
print("Acceder a 3:", tupla_anidada[2][0])

# 7) Convertir lista a tupla
lista = [1, 2, 3]
tupla_convertida = tuple(lista)
print("Tupla convertida:", tupla_convertida)

# 8) Comprobar existencia
numeros = (10, 20, 30, 40)
print("¿20 está en numeros?", 20 in numeros)

# 9) Contar repeticiones
repetidos = (1, 2, 2, 3, 2, 4)
print("Veces que aparece 2:", repetidos.count(2))

# 10) Posición de un valor
print("Posición de 3:", repetidos.index(3))


# ======================================
# TEMA 6: LISTAS
# Definición: Colección ordenada y modificable.
# ======================================

# 1) Lista de frutas
frutas = ["manzana", "banana", "cereza"]
print("Lista frutas:", frutas)

# 2) Acceder por índice
print("Primera fruta:", frutas[0])

# 3) Modificar elemento
frutas[1] = "pera"
print("Lista modificada:", frutas)

# 4) Agregar al final
frutas.append("mango")
print("Lista tras append:", frutas)

# 5) Insertar en posición
frutas.insert(1, "fresa")
print("Lista tras insert:", frutas)

# 6) Eliminar por valor
frutas.remove("cereza")
print("Lista tras remove:", frutas)

# 7) Recorrer lista
for f in frutas:
    print("Fruta:", f)

# 8) Comprobar existencia
print("¿mango está en frutas?", "mango" in frutas)

# 9) Ordenar lista
numeros = [4, 1, 7, 3, 9]
numeros.sort()
print("Números ordenados:", numeros)

# 10) Longitud
print("Cantidad de frutas:", len(frutas))


# ======================================
# TEMA 7: F-STRINGS
# Definición: Permiten insertar variables en cadenas fácilmente.
# ======================================

# 1) Saludo con nombre
print(f"Hola, {nombre} {apellido}")

# 2) Edad
print(f"Tienes {edad} años")

# 3) Promedio
promedio = 4.1
print(f"Tu promedio es {promedio}")

# 4) Operación dentro del texto
a = 5
b = 3
print(f"La suma de {a} y {b} es {a + b}")

# 5) Ciudad
print(f"Vives en {ciudad}")

# 6) Curso
print(f"Estás aprendiendo {curso}")

# 7) Nota con formato
nota = 3.8
print(f"Tu nota final fue {nota}")

# 8) Varios datos
animal = "perro"
color = "marrón"
print(f"Tengo un {animal} de color {color}")

# 9) Temperatura
temperatura = 22.5
print(f"La temperatura es de {temperatura}°C")

# 10) Nombre y edad
print(f"{nombre} {apellido} tiene {edad} años")


# ======================================
# TEMA 8: CONDICIONALES (if, elif, else)
# Definición: Permiten ejecutar acciones según una condición.
# ======================================

# 1) Mayor de edad
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("No eres mayor de edad")

# 2) Nota aprobada o no
nota = 3.2
if nota >= 3:
    print("Pasaste la materia")
else:
    print("Perdiste la materia")

# 3) Positivo, negativo o cero
numero = 0
if numero > 0:
    print("Número positivo")
elif numero < 0:
    print("Número negativo")
else:
    print("El número es cero")

# 4) Saludo por hora
hora = 14
if hora < 12:
    print("Buenos días")
elif hora < 18:
    print("Buenas tardes")
else:
    print("Buenas noches")

# 5) Positivo y par o impar
x = 10
if x > 0:
    if x % 2 == 0:
        print("Es positivo y par")
    else:
        print("Es positivo e impar")

# 6) Comparar texto
color = "rojo"
if color == "rojo":
    print("El color es rojo")
else:
    print("El color no es rojo")

# 7) Comparar números
a = 7
b = 12
if a > b:
    print("a es mayor")
else:
    print("b es mayor")

# 8) Días de la semana
dia = "lunes"
if dia == "lunes":
    print("Inicio de semana")
elif dia == "viernes":
    print("Fin de semana cerca")
elif dia == "sábado" or dia == "domingo":
    print("Es fin de semana")
else:
    print("Día normal")

# 9) Condición con booleano
llueve = False
if llueve:
    print("Lleva paraguas")
else:
    print("No necesitas paraguas")

# 10) Calificación
nota = 4.5
if nota >= 4.5:
    print("Excelente")
elif nota >= 3.5:
    print("Bien")
elif nota >= 3.0:
    print("Pasaste")
else:
    print("Reprobaste")


# ======================================
# TEMA 9: BUCLE WHILE
# Definición: Repite un bloque mientras la condición sea verdadera.
# ======================================

# 1) Contar del 1 al 5
i = 1
while i <= 5:
    print(i)
    i += 1

# 2) Repetir mensaje
contador = 0
while contador < 3:
    print("Hola")
    contador += 1

# 3) Contar regresivo
x = 10
while x >= 0:
    print(x)
    x -= 2

# 4) Múltiplos de 2
n = 1
while n <= 10:
    print(n * 2)
    n += 1

# 5) Sumar números del 1 al 5
suma = 0
num = 1
while num <= 5:
    suma += num
    num += 1
print("Suma total:", suma)

# 6) Mostrar intentos
intento = 1
while intento <= 3:
    print("Intento", intento)
    intento += 1

# 7) Simular crecimiento de edad
ed = 0
while ed < 18:
    print("Eres menor de edad (edad simulada):", ed)
    ed += 6
print("Ahora simulado que eres mayor")

# 8) Cuenta regresiva
cuenta = 5
while cuenta > 0:
    print("Cuenta regresiva:", cuenta)
    cuenta -= 1
print("¡Despegue!")

# 9) Acumulador
acumulador = 0
valor = 1
while valor <= 4:
    acumulador += valor
    valor += 1
print("Resultado final acumulador:", acumulador)

# 10) While con condición falsa inicial (no entra al ciclo)
activo = False
while activo:
    print("Esto no se ejecuta porque activo es False")
print("Fin del programa")