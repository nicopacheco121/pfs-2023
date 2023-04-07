try:
    variable = "123"
    variable = float(variable)
    variable/3

except ZeroDivisionError as error:
    print("zerodivicionerror",error)
except ValueError as error:
    print("valueerror",error)
except Exception as error:
    print("exception",error)

finally:
    print("llegue aca")


def cargarUsuario(nombre):
    if nombre == "Bort":
        raise ValueError("No admitimos usuarios llamados Bort")
    else:
        print("Bienvenido",nombre)

usuarios = ["matias","jorge","juan"]
for usuario in usuarios:
    try:
        cargarUsuario(usuario)
    except ValueError as elError:
    #    pass
        print("No se pudo cargar el usuario:",usuario,elError)

