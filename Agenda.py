from io import open

## author: Julio Conchas
## email : conchasjiemenez@gmail.com



def agregar():
    name=""
    codigo=""
    carrera=""

    print("============= Agregar =============")
    nombre=str(input("Ingrese el nombre: "))
    codigo=str(input("Ingrese el codigo: "))
    carrera=str(input("Ingrese ls carrera: "))


    agenda_file=open("agenda.txt","a")
    agenda_file.write(nombre+"."+codigo+"."+carrera+"|")

    agenda_file.close()

def mostrar():
    agenda_file=open("agenda.txt","r")
    agenda = agenda_file.readlines();
    print(agenda)
    agenda_file.close()

def options():
    print("===============================");
    print("[1] Agregar                   =");
    print("[2] Mostrat                   =");
    print("[3] Exit                      =");
    print("===============================");

def menu():
    print("============= Agenda =============")
    options()
    opt=str(input("Option: "))
    while(int(opt) != 3 ):
        if int(opt) == 1:
            agregar()
        elif int(opt) == 2:
            mostrar()
        else:
            print("ERROR: Opción no valida!")
        options()
        opt=str(input("Option: "))
    print("GOOD BYE!");


menu();
