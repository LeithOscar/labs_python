# Mi Proyecto Python

Este es un proyecto simple en Python que permite al usuario realizar operaciones matemáticas como suma, resta, multiplicación y división.

## Requisitos

- Python 3.x
- Instalar python desde la web.
- Instalar un IDE como visual studio code
- Añade las extensiones Python en el VsCode.

## Instrucciones

1. Clona o descarga el repositorio.
2. Abre el archivo `...py` y ejecútalo. (F5)
3. Selecciona la operación que deseas realizar.



## WIKI

# wiki.py

# --- Mini Wiki de Programación Básica en Python ---

# 1. Variables
# Una variable es un espacio en la memoria donde podemos almacenar datos para usarlos en nuestro programa.
# Las variables tienen un nombre y pueden contener diferentes tipos de datos, como números, texto, y más.

# Ejemplo de variables:
nombre = "Juan"      # Variable que guarda un texto
edad = 6             # Variable que guarda un número

# Tipos de Variables Comunes:
# - Texto (str): cadenas de texto, como "Hola"
# - Número Entero (int): números sin decimales, como 10
# - Número Decimal (float): números con decimales, como 3.5


# 2. Función print()
# La función print() se usa para mostrar información en la pantalla.
# Puedes usarla para mostrar textos, números, o el valor de una variable.

# Ejemplo:
print("Hola, mundo")    # Muestra: Hola, mundo
edad = 6
print(edad)             # Muestra: 6


# 3. Función input()
# La función input() permite que el usuario ingrese datos desde el teclado.
# Lo que el usuario escribe se guarda como texto (tipo str) y puede ser asignado a una variable.

# Ejemplo:
# nombre = input("¿Cuál es tu nombre? ")
# print("Hola, " + nombre + "!")


# 4. Operadores Matemáticos Básicos
# Los operadores matemáticos se utilizan para hacer operaciones con números.
# Algunos de los operadores más comunes son:
# - Suma (+): suma dos números
# - Resta (-): resta dos números
# - Multiplicación (*): multiplica dos números
# - División (/): divide dos números
# - Módulo (%): obtiene el resto de la división entre dos números (útil para saber si un número es par o impar)

# Ejemplo:
a = 3
b = 2
print(a + b)   # Muestra: 5
print(a % 2)   # Muestra: 1, porque el resto de dividir 3 entre 2 es 1


# 5. Condiciones if
# Las condiciones se utilizan para tomar decisiones en el código.
# La estructura básica es usar if para verificar si una condición es verdadera, y si lo es, ejecutar un bloque de código.
# También puedes usar else para ejecutar otro bloque si la condición es falsa.

# Ejemplo:
edad = 6
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


# 6. Funciones
# Una función es un bloque de código que se puede reutilizar.
# Las funciones permiten organizar el código en tareas específicas y llamarlas cuando sean necesarias.
# Para definir una función, se usa la palabra clave def seguida del nombre de la función y los parámetros (si tiene).

# Ejemplo:
def saludar(nombre):
    print("Hola, " + nombre + "!")

# Para llamar a la función:
saludar("Ana")   # Muestra: Hola, Ana!


# 7. Bucle for
# Un bucle for se usa para repetir un bloque de código un número específico de veces.
# En Python, for se suele usar para recorrer una secuencia de números o una lista.

# Ejemplo:
for i in range(1, 4):
    print(i)


# 8. Listas
# Las listas son estructuras de datos que nos permiten almacenar varios valores en una sola variable.
# Cada valor en una lista tiene un índice que empieza desde 0 (el primer elemento está en la posición 0, el segundo en 1, etc.)

# Ejemplo:
frutas = ["manzana", "banana", "cereza"]
print(frutas[0])   # Muestra: manzana


# 9. Comentarios
# Los comentarios son textos en el código que no se ejecutan.
# Se usan para explicar lo que hace el código. En Python, los comentarios se escriben usando el símbolo #.

# Ejemplo:
# Esto es un comentario
nombre = "Ana"  # Asignamos "Ana" a la variable nombre


# 10. Comparadores
# Los comparadores se usan para comparar valores en las condiciones.
# Algunos de los más comunes son:
# - == : igual a
# - != : diferente de
# - >  : mayor que
# - <  : menor que
# - >= : mayor o igual que
# - <= : menor o igual que

# Ejemplo:
a = 5
b = 3
print(a > b)    # Muestra: True
print(a == b)   # Muestra: False


# 11. Operador de Módulo %
# El operador módulo % se usa para obtener el resto de una división.
# Este operador es útil para saber si un número es par o impar.

# Ejemplo:
numero = 8
if numero % 2 == 0:
    print("Es par")
else:
    print("Es impar")


# 12. Concatenación de Cadenas de Texto
# La concatenación se refiere a unir dos o más cadenas de texto usando el operador +.
# Esto es útil para combinar textos con variables de tipo str.

# Ejemplo:
nombre = "Ana"
print("Hola, " + nombre + "!")   # Muestra: Hola, Ana!


# 13. Convertir Tipos de Datos
# A veces es necesario convertir datos de un tipo a otro.
# Por ejemplo, cuando usamos input() para obtener un número del usuario, el dato se guarda como texto (tipo str).
# Para hacer operaciones matemáticas, hay que convertirlo a entero (int) o decimal (float).

# Ejemplo:
# numero = input("Escribe un número: ")   # Esto es texto
# numero = int(numero)                    # Ahora es un número entero
# print(numero + 5)

# --- Fin de la Mini Wiki ---
