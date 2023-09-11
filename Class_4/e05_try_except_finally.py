"""
Controlar el flujo cuando tengo errores


"""

# 1/0


try:  # este bloque de codigo se ejecuta normalmente
    variable = '123'
    # variable = "asdfasd"
    variable = float(variable)
    variable / 3
    variable / 0


# Si ocurre un error, se ejecuta el bloque de codigo dentro del except
# Recordemos que existe una jerarquia de errores
# Imortante que los except esten ordenados de mas especifico a mas general

except ArithmeticError as error:
    print("arithmeticerror", error)

except ZeroDivisionError as error:  # si ocurre un error de division por cero, se ejecuta este bloque de codigo
    print("zerodivicionerror", error)
except ValueError as error:  # si ocurre un error de valor, se ejecuta este bloque de codigo
    print("valueerror", error)
except Exception as error:  # Si ocurre cualquier otro error, se ejecuta este bloque de codigo
    print("exception", error)


finally:  # este bloque de codigo se ejecuta siempre, haya o no haya ocurrido un error
    print("llegue aca")

# Mi programa continua normalmente

# Puedo no tratar el error especifico y directamente poner Exception

print('- - - - - - - - - -')


# Ejemplo de una funcion en la que si el nombre de usuario es Bort, no lo admitimos

def cargarUsuario(nombre):
    if nombre == "Bort":
        raise ValueError("No admitimos usuarios llamados Bort")  # Levanto un error
    else:
        print("Bienvenido", nombre)


# usuarios = ["matias","jorge","juan"]
usuarios = ["matias", 'Bort', "jorge", "juan"]
for usuario in usuarios:
    cargarUsuario(usuario)  # llamo a la funcion cargarUsuario

    # Tratando el error
    # try:
    #     cargarUsuario(usuario)
    # except ValueError as elError:
    #    pass
    #    print("No se pudo cargar el usuario:",usuario,elError)
