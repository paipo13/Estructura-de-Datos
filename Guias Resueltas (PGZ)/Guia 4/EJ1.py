# Ejercicio 1
# Diseñen una calculadora que tenga las funciones básicas (suma, resta, multiplicación y división)
# que operan siempre con dos operandos. El usuario introduce los dos operandos y el operador
# ('+', '-', '*', '/'). El programa termina cuando el usuario introduce una cadena vacía como operando.
# Maneja correctamente los posibles casos de error.

def calculadora():
    num1 = input('Ingrese el primer numero:')
    num2 = input('Ingrese el segundo numero:')
    operador = input('Ingrese el operador (+, -, *, /):')
    valores_posibles_oper = ['+', '-', '*','/']
    while operador not in valores_posibles_oper:
        return "Error: operador inválido."
    if num2 == 0:
        raise ValueError("No se puede dividir por 0.")
    try:
        num1 = float(num1)
        num2 = float(num2)

    except ValueError:
        return "Error: los operandos deben ser numéricos."
    if operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '*':
        return num1 * num2
    elif operador == '/':
        try:
            return num1 / num2
        except ZeroDivisionError as e:
            print(e)
        finally:
            print('Saliendo de la calculadora...')

calculo = calculadora()
print(calculo)
