ruta = "C:/archivos/personas.txt"

def Agregar(nombre, edad, genero):
    with open(ruta, "a") as archivo:
        fila = "{},{},{}\n".format(nombre,edad,genero)
        archivo.write(fila)
        print("----Persona Agregada-----")

def Lista():
    with open(ruta, "r") as archivo:
        print("-----Lista----")
        print(archivo.read())
        print("--------------")

def Listar_Genero(letra_genero):
    with open(ruta, "r") as archivos:
        archivos.seek(0, 0)
        for archivo in archivos:
            archivo = archivo.strip("\n")
            nombre, edad, genero = archivo.split(",")

            if letra_genero == genero:
                print(archivo)

while True:
    print("---Elige una opcion----")
    print("1 - Agregar una persona")
    print("2 - Listar personas")
    print("3 - Listar personas por generos")
    print("4 - Cerrar registro")
    opcion = input("Que quieres hacer? (1-4): ").strip()

    if int(opcion) == 1:
        nom = input("Tu nombre: ").strip().capitalize()
        ed = input("Tu edad: ").strip()
        gen = input("Tu genero: ").strip().upper()
        Agregar(nom, ed, gen)
    elif int(opcion) == 2 :
        Lista()
    elif int(opcion) == 3:
        gen = input("Ingresa el genero: ").strip().upper()
        Listar_Genero(gen)
    elif int(opcion) == 4:
        break
    else:
        print("Opcion Invalida")





    
