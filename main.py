from operaciones import suma, resta, multiplicacion, division

def mostrar_menu():
    print("Seleccione una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Opción: "))
            
            if opcion == 5:
                print("Saliendo del programa...")
                break

            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))

            if opcion == 1:
                print(f"Resultado: {suma(num1, num2)}")
            elif opcion == 2:
                print(f"Resultado: {resta(num1, num2)}")
            elif opcion == 3:
                print(f"Resultado: {multiplicacion(num1, num2)}")
            elif opcion == 4:
                if num2 == 0:
                    print("Error: No se puede dividir entre 0")
                else:
                    print(f"Resultado: {division(num1, num2)}")
            else:
                print("Opción no válida")
        
        except ValueError:
            print("Error: Debes ingresar un número válido.")

if __name__ == "__main__":
    main()
