#Calculadora de operaciones básicas
def main():
    seguir = True
    while seguir:
        print("Calculadora")
        print("1. S ")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("4.5 calcular potencia")
        print("4. D")
        print("5. Salir")
        opcion = input("Elija una opción: ")
        print("opcion",opcion)
        if opcion == "1":
            numero1 = float(input("Ingrese el primer numero: "))
            numero2 = float(input("Ingrese el segundo número: "))
            resultado = numero1 + numero2
            print("El resultado de la suma es: ", resultado)
        seguir = opcion != "5"

    
    
if __name__ == "__main__":
    main()
    
