try:
    # Primer nivel de try
    print("Primer nivel try")
    x = 10 / 2

    try:
        # Segundo nivel de try
        print("Segundo nivel try")
        y = 5 / 0  # Esto causará un ZeroDivisionError

    except ZeroDivisionError as e:
        print(f"Excepción atrapada en el segundo nivel: {e}")

        try:
            # Tercer nivel de try
            print("Tercer nivel try")
            z = int("no es un número")  # Esto causará un ValueError

        except ValueError as e:
            print(f"Excepción atrapada en el tercer nivel: {e}")

except Exception as e:
    print(f"Excepción atrapada en el primer nivel: {e}")

print("Programa finalizado.")