#Calculadora de operaciones básicas
def main():
    seguir = True
    while seguir:
        print("Calculadora")
        print("1. Sumar mata mas que antes")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        opcion = input("Elija una opción: ")
        print("opcion",opcion)
        seguir = opcion != "5"

    
    
if __name__ == "__main__":
    main()
    
