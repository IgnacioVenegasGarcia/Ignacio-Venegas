print("ESTRUCTURAS DE SELECCION")
cal = float(input("ingresa tu calificacion: "))
if cal>=60 and cal<=100:
    print("---Tu calificacion es aprobatoria---")
    if cal >= 99.99:
        print("EXCELENTE")
    if cal >= 90 and cal <= 99.99:
        print("Muy Bien")
    if cal >= 80 and cal <= 89.99:
        print("Bien")
    if cal >= 70 and cal <= 79.99:
        print("Regular")
    if cal >= 60 and cal <= 69.99:
        print("Suficiente")

else:
    if cal >= 0 and cal <= 59.99:
        print("reprobado")
    else:
        print("Ingrese una calificacion valida")
