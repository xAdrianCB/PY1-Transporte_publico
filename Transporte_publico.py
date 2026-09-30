#Creacion del archivo proyecto

def leerArchivo(nombre_archivo):
    if not isinstance(nombre_archivo, str):
        return "Error: la entrada debe ser tipo string"
    lista = []
    with open(nombre_archivo,"r") as archivo:
        lineas = archivo.readline()
        while lineas != "":
            linea = lineas.strip().split(";")
            lista += [linea]
            lineas = archivo.readline()
    return lista

def guardarArchivo(nombre_archivo, datos):
    if not isinstance(nombre_archivo, str):
        return "Error: entrada debe ser tipo string"
    if not isinstance(datos, list):
        return "Error: entrada datos, debe ser tipo lista"
    with open(nombre_archivo, "a") as archivo:
        archivo.write(datos + "\n")
        print("Datos guardados con exito")
    #preguntar si debo mostrar los datos del archivo de nuevo

def menu():
    return

def mostrar():
    return

def verificar_descripcion(descripcion, modelos):
    if not isinstance(descripcion, str):
        return "Error: descripcion debe ser una entrada string"
    i = 0
    while modelos < len(modelos)-1:
        if modelos[i][1] == descripcion:
            return True
        i+= 1
    return False
        

#E: N/A
#S: agrega datos .txt al archivo modelos.txt
#R: valida que la descipcion no se repita
def incluir_modelos():
    modelos = leerArchivo(modelos.txt)
    des = input("descripcion: ")
    marca = input("marca: ")
    asientos = input("cantidad de asiento: ")
    depie = input("cantidad de espacios de pie: ")
    
    if not verificar_descripcion(des, modelos):
        return "Error: descripcion de modelo ya registrado"
    nuevo_modelo = [des + ";" + marca + ";" + asiento + ";" + depie]
    guardarArchivo("modelos.txt",nuevo_modelo)

#E: descripcion
#S: valor boleano segun si la entrada se encuentra en el earchivo d etexto (unidades)
#R: entrada debe ser string
def verificar_unidad(descripcion):
    if not isinstance(descripcion, str):
        return "Error: entrada debe ser un string"
    with open("unidades.txt", "r") as archivo:
        lineas = archivo.readline
        while lineas != "":
            linea = archivo.strip().split(";")
            if linea[1] == descripcion:
                return False
        return True
    

#E: n/a
#S: n/a, elimina una linea especifica en base al primer elemento que coinside con el string dado(descripcion).
#R: debe existir la descipcion del modelo en el archivo, no debe estar vinculado a unidades
def eliminar_modelos():
    modelos = leerArchivo("modelos.txt")
    #aqui deberia ir mostrar
    des = input("descripcion del modelo a eliminar: ")

    if verificar_descripcion(des, modelos):
        if verificar_unidades(des):
            with open("modelos.txt", "w") as archivo:
                i = 0
                while i< len(modelos):
                    if des != modelos[i][0]:
                        archivo.write(modelos[i][0] + ";" + modelos[i][1] + ";" + modelos[i][2] + ";" + modelos[i][3] + "\n")
                    i+= 1
            print("Modelo eliminado")
        else:
            print("Error: el modelo no debe estar vinculado en unidads")
            #menuModelo
    # menuModelo

#E: n/a
#S: n/a, modifica
#R: indice debe ser entero, si los input estan vacios no se modifican
def modificar_modelos():
    modelos = leerArchivo("modelos.txt")
    print(modelos)
    #mostrar()
    indice = int(input("selecione el indice de la fila que desea modificar: "))
    
    des = input("descripcion: ")
    marca = input("marca: ")
    asientos = input("cantidad de asiento: ")
    depie = input("cantidad de espacios de pie: ")

    if des != "":
        modelos[indice-1][0] = des
    if marca != "":
        modelos[indice-1][1] = marca
    if asientos != "":
        modelos[indice-1][2] = asientos
    if depie != "":
        modelos[indice-1][3] = depie
    
    with open("modelos.txt", "w") as archivo:
        i = 0
        print(modelos)
        while i < len(modelos):
            archivo.write(modelos[i][0] + ";" + modelos[i][1] + ";" + modelos[i][2] + ";" +modelos[i][3] +"\n")
            i+= 1
    print("Se modifico con exito")
    #menu()
            
        
        
                
                


                
        
    
    
    
    
    
    
    
