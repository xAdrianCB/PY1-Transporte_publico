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
        

def menu():
    return

def mostrar():
    return

def verificar_descripcion(descripcion, modelos):
    return

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
    nuevo_modelo= [[des], [marca], [asiento], [depie]]
    guardarArchivo("modelos.txt",nuevo_modelo)
    
    
    
    
    
    
    
    
    
