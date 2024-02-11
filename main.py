Primeralista=[]

while True:
    print("Menu de lista")
    print("1. Agregar elemento")
    print("2. Borrar elemnto")
    print("3. Imprimir lista")
    print("4. salir")

    opcion = input("seleccione una opcion:  ")
    if opcion == "1":
        elemento = input("Ingrese elemento:  ")
        Primeralista.append(elemento)

    elif opcion == "2":
        print(Primeralista)
        indice = int(input("Ingrese el indice que desea borrar: "))
        Primeralista.pop(indice)
        print("Elemento borrado correctamente")


    elif opcion == "3":
        print("Lista Actual")
        print(Primeralista)

    elif opcion == "4":
        print("¡ saliendo del progrma !")
        break

    else:
        print("opcion no valida")


