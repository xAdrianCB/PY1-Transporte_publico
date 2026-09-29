#Creacion del archivo proyecto

def leerArchivo(archivo):
    return

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
    
    
    
    
    
    
    
    
    
