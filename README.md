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

## Ejemplos de Programación

### 1. **Variables**

Las **variables** permiten almacenar valores para usarlos más tarde en el programa. Pueden contener diferentes tipos de datos, como números, texto, etc.

#### Ejemplo:
```python
nombre = "Juan"  # Almacena un texto
edad = 6         # Almacena un número entero
### 2. **Función `input()`**

La función **`input()`** permite pedir información al usuario, y el dato que se ingresa se guarda como texto.

#### Ejemplo:
```python
nombre = input("¿Cuál es tu nombre? ")
print("Hola, " + nombre + "!")

### 3. **Operadores Matemáticos Básicos**

Los **operadores matemáticos** se utilizan para realizar operaciones con números. Los más comunes son:

- **Suma (`+`)**
- **Resta (`-`)**
- **Multiplicación (`*`)**
- **División (`/`)**

#### Ejemplo:
```python
a = 3
b = 2
print(a + b)  # Muestra: 5
### 4. **Condicionales `if`**### 5. **Funciones**

Las **funciones** permiten organizar el código en bloques reutilizables. Se definen con la palabra clave `def` seguida del nombre de la función.

#### Ejemplo:
```python
def saludar(nombre):
    print("Hola, " + nombre + "!")


Las **condiciones** permiten tomar decisiones en el programa. Se usan para ejecutar una parte del código si se cumple una condición, y otra parte si no se cumple.

#### Ejemplo:
```python
edad = 6
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

### 6. **Bucle `for`**

El **bucle `for`** se usa para repetir un bloque de código un número específico de veces. Se puede usar con un rango de números o con una lista.

#### Ejemplo:
```python
for i in range(1, 4):  # Repite 3 veces
    print(i)             # Muestra: 1, 2, 3

### 7. **Listas**

Las **listas** permiten almacenar múltiples elementos en una sola variable. Cada elemento tiene un índice que comienza en 0.

#### Ejemplo:
```python
frutas = ["manzana", "banana", "cereza"]
print(frutas[0])  # Muestra: manzana
### 8. **Comentarios**

Los **comentarios** son textos dentro del código que explican lo que hace el código. Los comentarios no son ejecutados.

#### Ejemplo:
```python
# Esto es un comentario
nombre = "Ana"  # Asignamos "Ana" a la variable nombre

### 9. **Comparadores**

Los **comparadores** se usan para comparar dos valores. Algunos de los más comunes son:

- **`==`** : igual a
- **`!=`** : diferente de
- **`>`**  : mayor que
- **`<`**  : menor que
- **`>=`** : mayor o igual que
- **`<=`** : menor o igual que

#### Ejemplo:
```python
a = 5
b = 3
print(a > b)  # Muestra: True
print(a == b)  # Muestra: False

### 10. **Operador de Módulo `%`**

El **operador de módulo** `%` se utiliza para obtener el resto de una división.

#### Ejemplo:
```python
numero = 8
if numero % 2 == 0:
    print("Es par")
else:
    print("Es impar")

### 11. **Concatenación de Cadenas de Texto**

La **concatenación** permite unir dos o más cadenas de texto.

#### Ejemplo:
```python
nombre = "Ana"
print("Hola, " + nombre + "!")  # Muestra: Hola, Ana!

### 12. **Convertir Tipos de Datos**

A veces es necesario convertir un tipo de dato a otro. Por ejemplo, convertir texto a un número entero para poder realizar operaciones matemáticas.

#### Ejemplo:
```python
numero = input("Escribe un número: ")  # Esto es texto
numero = int(numero)                   # Ahora es un número entero
print(numero + 5)                       # Muestra el resultado de la operación

### 13. **Uso de `while` para Repetir Código**

El bucle **`while`** se utiliza para ejecutar un bloque de código mientras se cumpla una condición. Es útil cuando no sabemos cuántas veces necesitamos repetir una acción.

#### Ejemplo:
```python
contador = 1
while contador <= 5:
    print(contador)
    contador += 1  # Aumentamos el contador en 1


fin