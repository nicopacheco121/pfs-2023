# Trabajamos con la sentencia if y la identacion

status = "ROUTED"  # importante utilizar variables con nombres que expliquen el contenido
# status = "REJECTED"

# A la variable estado le asignamos un conjunto de valores.
estados = ["NEW", "PARTIALLY_FILLED", "CANCELLED", "REJECTED", "EXPIRED", "FILLED", "ROUTED"]

if status in estados:
    ordenActiva = status in ["NEW", "PARTIALLY_FILLED"]  # esta sentencia es verdadera o falsa?

    ordenFinalizada = status in ["CANCELLED", "REJECTED", "EXPIRED", "FILLED"]

    ordenAConfirmar = status in ["ROUTED"]

    if ordenActiva:
        print("Reemplanzdo orden")
    elif ordenFinalizada:
        print("Enviando Orden a mercado")
    else:
        # no puedo dejar esto vacio
        pass

if status in ["NEW", "PARTIALLY_FILLED", "CANCELLED", "REJECTED", "EXPIRED", "FILLED", "ROUTED"]:
    # Otra forma de hacerlo
    if status in ["NEW", "PARTIALLY_FILLED"]:
        print("Reemplanzdo orden")
    elif status in ["CANCELLED", "REJECTED", "EXPIRED", "FILLED"]:  # codigo opcional, no hace falta que exista elif
        print("Enviando Orden a mercado")
    else:  # codigo opcional, no hace falta que exista elif
        # no puedo dejar esto vacio el else
        pass
    # Que es mas legible??


# Puedo evaluar conjunto de condiciones
# Evaluamos si toddas son verdaderas con "all"
a = 10
condiciones = [a < 10, a == 10, a != 20]  # conjunto de condiciones, lista con valores booleanos
if all(condiciones):  # evalua si todos los elementos son verdaderos
    print("hago mas cosas")

# Evaluamos si alguna es verdadera con "any"
if any(condiciones):
    print("hago algo")
else:
    print("hago otra cosa")

# es lo mismo a hacer esto
if a < 10 or a == 10 or a != 20:
    print("hago algo")
else:
    print("hago otra cosa")


# El and no valida la segunda opcion si la primera ya es False
if False and a / 0:
    print("Yes")
else:
    print("No")
# Esto es importante tenerlo en cuenta porque puede ser que yo necesite que una instruccion se ejecute si o si
# porque por ejemplo me podria cambiar el estado de una variable. Si estas instrucciones las tengo dentro de
# condicionales puede que no se ejecuten nunca.

# El or no valida la segunda opcion si la primera ya es True
if True or a / 0:
    print("Yes")
else:
    print("No")