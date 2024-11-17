# soluciones_2.py

# Solución del Ejercicio 1
def suma(a, b):
    return a + b
print(f"Ejercicio 1: {suma(3, 4)}")


# Solución del Ejercicio 2
def mayor(a, b):
    if a > b:
        return a
    else:
        return b
print(f"Ejercicio 2: {mayor(5, 3)}")


# Solución del Ejercicio 3
def resta(a, b):
    return a - b
print(f"Ejercicio 3: {resta(10, 4)}")


# Solución del Ejercicio 4
def tabla_del_2():
    for i in range(1, 11):
        print(f"2 x {i} = {2 * i}")
tabla_del_2()


# Solución del Ejercicio 5
def doble(numero):
    return numero * 2
print(f"Ejercicio 5: {doble(7)}")


# Solución del Ejercicio 6
def par_o_impar(numero):
    return "Par" if numero % 2 == 0 else "Impar"
print(f"Ejercicio 6: {par_o_impar(8)}")


# Solución del Ejercicio 7
def adivina_numero_secreto(numero):
    numero_secreto = 3
    return "¡Correcto!" if numero == numero_secreto else "Intenta de nuevo"
print(adivina_numero_secreto(3))


# Solución del Ejercicio 8
def contar_letras(palabra):
    return len(palabra)
print(f"Ejercicio 8: {contar_letras('programacion')}")


# Solución del Ejercicio 9
def cuenta_hasta_10():
    for i in range(1, 11):
        print(i)
cuenta_hasta_10()


# Solución del Ejercicio 10
def mostrar_frutas():
    frutas = ["Manzana", "Banana", "Naranja"]
    for fruta in frutas:
        print(fruta)
mostrar_frutas()


# Solución del Ejercicio 11
def es_mayor_de_edad(edad):
    return "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(f"Ejercicio 11: {es_mayor_de_edad(20)}")


# Solución del Ejercicio 12
def sonidos_animales():
    animales = {"Perro": "Ladra", "Gato": "Maulla", "Vaca": "Muge"}
    for animal, sonido in animales.items():
        print(f"El {animal} hace {sonido}")
sonidos_animales()


# Solución del Ejercicio 13
def numeros_hasta_20():
    for i in range(1, 21):
        print(i)
numeros_hasta_20()


# Solución del Ejercicio 14
def verificar_palabra_en_lista(palabra):
    palabras = ["sol", "luna", "estrella"]
    return "Está en la lista" if palabra in palabras else "No está en la lista"
print(f"Ejercicio 14: {verificar_palabra_en_lista('sol')}")


# Solución del Ejercicio 15
def elegir_opcion(opcion):
    if opcion == "a":
        return "Elegiste la opción A"
    elif opcion == "b":
        return "Elegiste la opción B"
    elif opcion == "c":
        return "Elegiste la opción C"
    else:
        return "Opción no válida"
print(f"Ejercicio 15: {elegir_opcion('b')}")
