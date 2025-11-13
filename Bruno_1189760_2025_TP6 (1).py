def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir_simple(a, b):
    if b == 0:
        print("Error: La division por cero no se puede realizar.")
        return 0, 0

    dividendo = a
    div = 0

    while dividendo >= b:
        dividendo = dividendo - b
        div = div + 1

    resto = dividendo
    return div, resto

def numeros():
    num1 = int(input("Ingrese el primer numero entero: "))
    num2 = int(input("Ingrese el segundo numero entero: "))
    return num1, num2

def calculadora_basica():
    
    seguir = True
    while seguir == True:

        print("CALCULADORA")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        
        opcion = input("Opcion (1-5): ")
        
        if opcion == '5':
            print("Adios!!")
            seguir = False
        
        elif opcion == '1':
            a, b = numeros()
            res = sumar(a, b)
            print("Resultado: ", a, " + ", b, " = ", res)
            input("Presione ENTER para continuar...")

        elif opcion == '2':
            a, b = numeros()
            res = restar(a, b)
            print("Resultado: ", a, " - ", b, " = ", res)
            input("Presione ENTER para continuar...")

        elif opcion == '3':
            a, b = numeros()
            res = multiplicar(a, b)
            print("Resultado: ", a, " * ", b, " = ", res)
            input("Presione ENTER para continuar...")
                
        elif opcion == '4':
            a, b = numeros()
            div, resto = dividir_simple(a, b) 
            
            print("")
            print("Division por Restas Sucesivas:")
            print("   Resultado Entero (div): ", div)
            print("   Resto: ", resto)
            input("Presione ENTER para continuar...")
        
        else:
            print("Opcion no valida. Intente de nuevo.")
            
if __name__ == "__main__":
    calculadora_basica()

