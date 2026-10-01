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
    if not isinstance(datos, str):
        return "Error: entrada datos, debe ser tipo lista"
    with open(nombre_archivo, "a") as archivo:
        archivo.write(datos + "\n")
        print("Datos guardados con exito")
    #preguntar si debo mostrar los datos del archivo de nuevo

def menu():
    return

#E: nombre_archivo
#S: muestra mediante prints las lineas de determiando archivo con indice
#R: entrada debe ser tipo string
def mostrar(nombre_archivo):
    if not isinstance(nombre_archivo, str):
        return "Error: entrada debe ser tipo string"
    with open(nombre_archivo, "r") as archivo:
        linea = archivo.readline()
        i = 1
        while linea != "":
            print(i, linea.strip())
            i+= 1
            linea = archivo.readline()

def verificar_descripcion(descripcion, modelos):
    if not isinstance(descripcion, str):
        return "Error: descripcion debe ser una entrada string"
    i = 0
    while i < len(modelos):
        if modelos[i][0] == descripcion:
            return False
        i+= 1    
    return True


#E: N/A
#S: agrega datos .txt al archivo modelos.txt
#R: valida que la descipcion no se repita
def incluir_modelos():
    modelos = leerArchivo("modelos.txt")
    des = input("descripcion: ")
    marca = input("marca: ")
    asientos = input("cantidad de asiento: ")
    depie = input("cantidad de espacios de pie: ")
    
    if not verificar_descripcion(des, modelos):
        return "Error: descripcion de modelo ya registrado"
    nuevo_modelo = [des + ";" + marca + ";" + asientos + ";" + depie]
    print(nuevo_modelo[0])
    guardarArchivo("modelos.txt",nuevo_modelo[0])

#E: descripcion
#S: valor boleano segun si la entrada se encuentra en el earchivo d etexto (unidades)
#R: entrada debe ser string
def verificar_unidades(descripcion):
    return True
    if not isinstance(descripcion, str):
        return "Error: entrada debe ser un string"
    with open("unidades.txt", "r") as archivo:
        lineas = archivo.readline
        while lineas != "":
            linea = archivo.strip().split(";")
            print(linea)
            if linea[1] == descripcion:
                return False
        return True
    

#E: n/a
#S: n/a, elimina una linea especifica en base al primer elemento que coinside con el string dado(descripcion).
#R: debe existir la descipcion del modelo en el archivo, no debe estar vinculado a unidades
def eliminar_modelos():
    modelos = leerArchivo("modelos.txt")
    #aqui deberia ir mostrar
    mostrar("modelos.txt")
    des = input("descripcion del modelo a eliminar: ")

    if not verificar_descripcion(des, modelos):
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
    #print(modelos)
    mostrar("modelos.txt")
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
        while i < len(modelos):
            archivo.write(modelos[i][0] + ";" + modelos[i][1] + ";" + modelos[i][2] + ";" +modelos[i][3] +"\n")
            i+= 1
    print("Se modifico con exito")
    #menu()

#E: modelo
#S: retorna el elemento selecionado en la lista de modelos
#R: el indice debe estar dentro del rango
def obtener_modelos(indice):
    modelos = leerArchivo("modelos.txt")
    print(len(modelos))
    print(indice)
    if indice > len(modelos):
        print("Error: el indice indicado supera la lista")
        incluir_unidades()
    i = 0
    while i < len(modelos):
        if i == indice-1 :
            return modelos[i][0]
        i += 1
#E: placa, nombre_archivo
#S: valor booleano que determina si el elemento se escuenta en la lista
#R: ambas entradas deben ser string
def verificar_placa(placa, nombre_archivo):
    if not isinstance(placa, str):
        return False
    if not isinstance(nombre_archivo, str):
        return False
        
    
    unidades = leerArchivo(nombre_archivo)
    i = 0
    while i < len(unidades):
        if unidades[i][0] == placa:
            return True
        i+= 1    
    return False
    
#E:n/a
#S: n/a, guarda una lista de elementos en un archivo de texto
#R: placa no debe existir en el archivo de texto
def incluir_unidades():
    while True:
        placa = input("Ingrese la placa: ") #debo usar try aqui?
        
        if verificar_placa(placa, "unidades.txt"):
            print("Error: la placa introducidad ya existe en los registros")
        else:
            break
    
    mostrar("modelos.txt")
    modelo = int(input("Ingrese el indice del mdoelo deseado: "))
    nModelo = obtener_modelos(modelo)
    anio = input("Ingrese el a;o: ")
    empresa = input("Ingrese el nombre de la empresa asignada: ")

    #debo validar que las entradas no sean vaicas
    nuevo_unidad = [placa + ";" + nModelo + ";" + anio + ";" + empresa]
    print(nuevo_unidad[0])
    guardarArchivo("unidades.txt",nuevo_unidad[0])
    
    
    
        

            
        
        
                
                


                
        
    
    
    
    
    
    
    
