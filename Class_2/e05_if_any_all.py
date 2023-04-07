status = "PARTIALLY_FILLED"

estados = ["NEW","PARTIALLY_FILLED","CANCELLED","REJECTED","EXPIRED","FILLED","ROUTED"]

if status in estados:
    ordenActiva = status in ["NEW","PARTIALLY_FILLED"]

    ordenFinalizada = status in ["CANCELLED","REJECTED","EXPIRED","FILLED"]

    ordenAConfirmar = status in ["ROUTED"]

    #como detectar si debo reemplazar una orden o si debo enviar una nueva
    if ordenActiva:
        print("Reemplanzdo orden")
    elif ordenFinalizada:
        print("Enviando Orden a mercado")
    else:
        pass

a = 10
condiciones = [a < 10,a == 10,a!= 20]
if all(condiciones): #a > 10 and a == 10 and a!= 20
    print("hago mas cosas")

if a > 10 or a == 10 or a!= 20:
    print("hago algo")
else:
    print("hago otra cosa")



if any(condiciones):
    print("hago algo")
else:
    print("hago otra cosa")

#El and no valida la segunda opcion si la primera ya es False

if False and a/0:
    print("Yes")
else:
    print("No")

#El or no valida la segunda opcion si la primera ya es True

if False or a/0:
    print("Yes")
else:
    print("No")