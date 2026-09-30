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
    
    if not verifica_descripcion(des, modelos):
        return "Error: descripcion de modelo ya registrado"
    nuevo_modelo= [des + ";" marca + ";" + asiento + ";" + depie]
    guardarArchivo("modelos.txt",nuevo_modelo)

#E: n/a
#S: n/a, elimina una linea especifica en base al primer elemento que coinside con el string dado(descripcion).
#R: debe existir la descipcion del modelo en el archivo.
def eliminar_modelos():
    modelos = leerArchivo("modelos.txt")
    #aqui deberia ir mostrar
    des = input("descripcion del modelo a eliminar: ")

    if verificar_descripcion(des, modelos):
        with open("modelos.txt", "w") as archivo:
            i = 0
            while i< len(modelos):
                if des != modelos[i][0]:
                    archivo.write(modelos[i][0] + ";" + modelos[i][1] + ";" + modelos[i][2] + ";" + modelos[i][3] + "\n")
                i+= 1
        print("Modelo eliminado")
    #return menuModelo()
    
                


                
        
    
    
    
    
    
    
    
