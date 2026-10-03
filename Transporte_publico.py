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
    mostrar("modelos.txt")
    des = input("descripcion: ")
    marca = input("marca: ")
    asientos = input("cantidad de asiento: ")
    depie = input("cantidad de espacios de pie: ")
    
    if not verificar_descripcion(des, modelos):
        return "Error: descripcion de modelo ya registrado"
    nuevo_modelo = [des + ";" + marca + ";" + asientos + ";" + depie]
    guardarArchivo("modelos.txt",nuevo_modelo[0])

#E: descripcion
#S: valor boleano segun si la entrada se encuentra en el earchivo d etexto (unidades)
#R: entrada debe ser string
def verificar_unidades(descripcion):
    if not isinstance(descripcion, str):
        return "Error: entrada debe ser un string"
    with open("unidades.txt", "r") as archivo:
        lineas = archivo.readline()
        while lineas != "":
            lineas = lineas.strip().split(";")
            if lineas[1] == descripcion:
                return False
            lineas = archivo.readline()
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
    else:
        print("Error: el modelo no existe")
    # menuModelo

#E: n/a
#S: n/a, modifica
#R: indice debe ser entero, si los input estan vacios no se modifican
def modificar_modelos():
    modelos = leerArchivo("modelos.txt")
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
    if indice > len(modelos) or indice < 1:
        return "Error: el indice no cumple con el ranfo(1,largo de lista"
    i = 0
    while i < len(modelos):
        if i == indice-1 :
            return modelos[i][0]
        i += 1
#E: placa, nombre_archivo
#S: retorna valor booleano que determina si el elemento se escuenta en el archivo
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
    mostrar("unidades.txt")
    while True:
        placa = input("Ingrese la placa: ") #debo usar try aqui?
        
        if verificar_placa(placa, "unidades.txt"):
            print("Error: la placa introducidad ya existe en los registros")
        else:
            break
    
    mostrar("modelos.txt")
    modelo = int(input("Ingrese el indice del modelo deseado: "))
    nModelo = obtener_modelos(modelo)
    anio = input("Ingrese el año: ")
    empresa = input("Ingrese el nombre de la empresa asignada: ")

    #debo validar que las entradas no sean vaicas
    nuevo_unidad = [placa + ";" + nModelo + ";" + anio + ";" + empresa]
    guardarArchivo("unidades.txt",nuevo_unidad[0])
#E: placa
#S: retorna valor booleano si el elemento existe o no
#R: entrada debe ser string
def verificar_salidas(placa):
    if not isinstance(placa, str):
        return "Error: entrada debe ser un string"
    with open("salidas.txt", "r") as archivo:
        lineas = archivo.readline()
        while lineas != "":
            lineas = lineas.strip().split(";")
            if lineas[2] == descripcion:
                return False
            lineas = archivo.readline()
    return True

 
#E: n/a
#S: n/a, eliminar una linea que consida con la placa
#R: la unidad no debe estar asignada a una salida
def eliminar_unidades():
    unidades = leerArchivo("unidades.txt")
    mostrar("unidades.txt")

    while True:
        placa = input("Ingrese la placa: ")
        
        if not verificar_placa(placa, "unidades.txt"):
            print("Error: la placa introducidad no existe en los registros")
        else:
            break
    if verificar_salidas(placa):
        with open("unidades.txt", "w") as archivo:
            i = 0
            while i< len(unidades):
                if placa != unidades[i][0]:
                    archivo.write(unidades[i][0] + ";" + unidades[i][1] + ";" + unidades[i][2] + ";" + unidades[i][3] + "\n")
                i+= 1
            print("Unidad eliminado")
    else:
        print("Error: la unidad no debe estar vinculado en salidas programadas")

#E: n/a
#S: modifica la linea indicada del archivo de texto
#R: indice tiene que ser en un rango del 1 al len(unidades) 
def modificar_unidades():
    unidades = leerArchivo("unidades.txt")
    mostrar("unidades.txt")
    while True:
        indice = int(input("selecione el indice de la fila que desea modificar: "))

        if indice < 1 or indice > len(unidades):
            print("Error: indice no esta dentro del rango")
        else:
            break
    placa = input("Ingrese la placa: ")
    mostrar("modelos.txt")
    modelo = int(input("Ingrese el indice del modelo deseado: "))
    nModelo = obtener_modelos(modelo)
    anio = input("Ingrese el año: ")
    empresa = input("Ingrese el nombre de la empresa asignada: ")

    if placa != "":
        unidades[indice-1][0] = placa
    if nModelo != "":
        unidades[indice-1][1] = nModelo
    if anio != "":
        unidades[indice-1][2] = anio
    if empresa != "":
        unidades[indice-1][3] = empresa
    
    with open("unidades.txt", "w") as archivo:
        i = 0
        while i < len(unidades):
            archivo.write(unidades[i][0] + ";" + unidades[i][1] + ";" + unidades[i][2] + ";" +unidades[i][3] +"\n")
            i+= 1
    print("Se modifico con exito")

#E: cedula, nombre_archivo
#S: retorna valor booleano que determina si el elemento se escuenta en el archivo
#R: ambas entradas deben ser string
def verificar_cedula(cedula, nombre_archivo):
    if not isinstance(cedula,str):
        print("Error: entrada cedula debe ser tipo string")
    if not isinstance(nombre_archivo,str):
        print("Error: entrada nombre_archivo debe ser tipo string")
    conductores = leerArchivo(nombre_archivo)
    i = 0
    while i < len(conductores):
        if conductores[i][0] == cedula:
            return True
        i+= 1    
    return False
    
#E: n/a
#S: n/a, cumple la funcion de agregar un conductor nuevo con sus datos al archivo de texto conductores.
#R: la cedula ingresada no puede existir en el archivo, valida largo de cedula, valida el tipo de licencia en variable lista "tipo"
def incluir_conductor():
    mostrar("conductores.txt")
    while True:
        try:
            cedula = int(input("Ingrese la cedula: "))
            
            if len(str(cedula)) > 7 or len(str(cedula)) < 7:
                print("Error: la cedula debe ser de 7 digitos")  
            elif verificar_cedula(str(cedula), "conductores.txt"):
                print("Error: la cedula introducidad ya existe en los registros")
            else:
                cedula = str(cedula)
                break
        except:
            print("Error: debe introducir un numero entero")

    nombre = input("Ingrese el nombre completo (Form: nombre y apellido): ")
    tipos = ["B1","B2","B3","B4"]
    
    valido = True
    while valido:
        T_licencia = input("Ingrese el tipo de licencia (Form: B1,,,B4): ").upper()
        for i in tipos:
            if i == T_licencia:
                valido = False
                break
        if valido:
            print("Error: el tipo de licencia no es valido(B1,B2,B3,B4")
    
    print("Ingrese la fecha de vencimiento de la licencia (Form: dia/mes/año)")
    while True:
        try:
            dia = int(input("Ingre solo el dia: "))
            mes = int(input("Ingrese solo el mes: "))
            anio = int(input("Ingrese solo el año: "))
            if dia > 31 or dia < 1:
                print("Error: el dia no esta dentro del rango(1 y 30)")
            elif mes > 12 or mes < 1:
                print("Error: el mes no esta dentro del rango(1 y 12)")
            else:
                vencimiento = str(dia) + "/" + str(mes) + "/" + str(anio)
                break
        except:
            print("Error, alguna de las entradas no es un numero entero")
    while True:
        jornadaM = int(input("Ingrese la jornada maxima diaria(en horas): "))
        if jornadaM < 0:
            print("Error: el rango de jornada empieza apartir de 1")
        else:
            jornadaM = str(jornadaM)
            break
    conductor = [cedula + ";" + nombre + ";" + T_licencia + ";" + vencimiento + ";" + jornadaM]
    guardarArchivo("conductores.txt",conductor[0])

#E: cedula
#S: valores boleanos dependiendo si encuentra similitudes
#R: valida que cedula sea un string
def verificar_salidas_conductor(cedula):
    if not isinstance(cedula, str):
        return "Error: entrada debe ser un string"
    with open("salidas.txt", "r") as archivo:
        lineas = archivo.readline()
        while lineas != "":
            lineas = lineas.strip().split(";")
            if lineas[3] == cedula:
                return False
            lineas = archivo.readline()
    return True

#E: n/a
#S: n/a, su funcion es eliminar una linea del archivo conductores mediantes la cedula
#R: valida los digitos de cedula, valida que no este vinculada, cedula = int, valida que cedula existe
def eliminar_conductor():
    conductores = leerArchivo("conductores.txt")
    mostrar("conductores.txt")

    while True:
        try:
            cedula = int(input("Ingrese la cedula: "))
            
            if len(str(cedula)) > 7 or len(str(cedula)) < 7:
                print("Error: la cedula debe ser de 7 digitos")  
            elif not verificar_cedula(str(cedula), "conductores.txt"):
                print("Error: la cedula no se encuentra en el archivo")
            else:
                cedula = str(cedula)
                break
        except:
            print("Error: debe introducir un numero entero")
            
    if verificar_salidas_conductor(cedula):
        with open("conductores.txt", "w") as archivo:
            i = 0
            while i< len(conductores):
                if cedula != conductores[i][0]:
                    archivo.write(conductores[i][0] + ";" + conductores[i][1] + ";" + conductores[i][2] + ";" + conductores[i][3] + ";" + conductores[i][4] + "\n")
                i+= 1
            print("conductor eliminado")
    else:
        print("Error: el conductor no debe estar vinculado en salidas programadas")
    
#E: n/a
#S: modifica una linea del archivo txt por medio de un indice
#R: la cedula ingresada no puede existir en el archivo, valida largo de cedula, valida el tipo de licencia en variable lista "tipo"
def modificar_conductor():
    conductores = leerArchivo("conductores.txt")
    mostrar("conductores.txt")
    while True:
        indice = int(input("selecione el indice de la fila que desea modificar: "))

        if indice < 1 or indice > len(conductores):
            print("Error: indice no esta dentro del rango")
        else:
            break
    while True:
        try:
            cedula = int(input("Ingrese la cedula: "))
            
            if len(str(cedula)) > 7 or len(str(cedula)) < 7:
                print("Error: la cedula debe ser de 7 digitos")  
            elif verificar_cedula(str(cedula), "conductores.txt"):
                print("Error: la cedula introducidad ya existe en los registros")
            else:
                cedula = str(cedula)
                break
        except:
            print("Error: debe introducir un numero entero")

    nombre = input("Ingrese el nombre completo (Form: nombre y apellido): ")
    tipos = ["B1","B2","B3","B4"]
    
    valido = True
    while valido:
        T_licencia = input("Ingrese el tipo de licencia (Form: B1,,,B4): ").upper()
        for i in tipos:
            if i == T_licencia:
                valido = False
                break
        if valido:
            print("Error: el tipo de licencia no es valido(B1,B2,B3,B4")
    
    print("Ingrese la fecha de vencimiento de la licencia (Form: dia/mes/año)")
    while True:
        try:
            dia = int(input("Ingre solo el dia: "))
            mes = int(input("Ingrese solo el mes: "))
            anio = int(input("Ingrese solo el año: "))
            if dia > 31 or dia < 1:
                print("Error: el dia no esta dentro del rango(1 y 30)")
            elif mes > 12 or mes < 1:
                print("Error: el mes no esta dentro del rango(1 y 12)")
            else:
                vencimiento = str(dia) + "/" + str(mes) + "/" + str(anio)
                break
        except:
            print("Error, alguna de las entradas no es un numero entero")
    while True:
        jornadaM = int(input("Ingrese la jornada maxima diaria(en horas): "))
        if jornadaM < 0:
            print("Error: el rango de jornada empieza apartir de 1")
        else:
            jornadaM = str(jornadaM)
            break
    if not verificar_cedula(cedula, "conductores.txt"):
        if cedula != "":
            conductores[indice-1][0] = cedula
    if nombre != "":
        conductores[indice-1][1] = nombre
    if T_licencia != "":
        conductores[indice-1][2] = T_licencia
    if vencimiento != "":
        conductores[indice-1][3] = vencimiento
    if jornadaM != "":
        conductores[indice-1][4] = jornadaM
    
    with open("conductores.txt", "w") as archivo:
        i = 0
        while i < len(conductores):
            archivo.write(conductores[i][0] + ";" + conductores[i][1] + ";" + conductores[i][2] + ";" + conductores[i][3] + ";" + conductores[i][4]+"\n")
            i+= 1
    print("Se modifico con exito")

#E: codigo, nombre_archivo
#S: retorna valor booleano que determina si el elemento se escuenta en el archivo
#R: ambas entradas deben ser string
def verificar_rutas(codigo, nombre_archivo):
    if not isinstance(codigo,str):
        print("Error: entrada codigo debe ser tipo string")
    if not isinstance(nombre_archivo,str):
        print("Error: entrada nombre_archivo debe ser tipo string")
    rutas = leerArchivo(nombre_archivo)
    i = 0
    while i < len(rutas):
        if rutas[i][0] == codigo:
            return True
        i+= 1    
    return False

#E: n/a
#S: n/a, añade una nueva linea al archivo de texto rutas
#R: valida si el codigo ya existe en el archivo, km = int, tarifa = int y > 0.
def incluir_rutas():
    mostrar("rutas.txt")
    while True:
        try:
            print("Ingrese el codigo de ruta(Codigo salida - Codigo llegada)")
            llegada = input("Ingre solo el codigo de llegada(ejemp: LIM): ").upper()
            salida = input("Ingre solo el codigo de salida(ejemp: SJO): ").upper()
            
            codigo = llegada + "-" + salida
            if verificar_rutas(codigo, "rutas.txt"):
                print("Error: el codigo de ruta ya existe en el registro")
            else:
                break
        except:
            print("Error")

    origen = input("Ingrese el nombre del lugar de origen: ")
    destino = input("Ingrese el nombre del lugar de destino: ")
    
    while True:
        try:
            km = int(input("Ingrese la distancia total en kilometros(km): "))
            km =str(km)
            break
        except:
            print("Error: la entrada debe ser un numero entero")
    
    while True:
        try:
            tarifa = int(input("ingrese el valor en colones: "))
            if tarifa < 1:
                print("Error: la tarifa debe ser superior a 0")
            else:
                tarifa = str(tarifa)
                break
        except:
            print("Error: la entrada no es un numero entero")

    ruta = [codigo + ";" + origen + ";" + destino + ";" + km + ";" + tarifa]
    guardarArchivo("rutas.txt",ruta[0])

#E: codigo
#S: valores boleanos dependiendo si encuentra similitudes
#R: valida que codigo sea un string
def verificar_paradas_rutas(codigo):
    if not isinstance(codigo, str):
        return "Error: entrada debe ser un string"
    with open("paradas.txt", "r") as archivo:
        lineas = archivo.readline()
        while lineas != "":
            lineas = lineas.strip().split(";")
            if lineas[0] == codigo:
                return False
            lineas = archivo.readline()
    return True

#E: codigo
#S: valores boleanos dependiendo si encuentra similitudes
#R: valida que codigo sea un string
def verificar_salidas_rutas(codigo):
    if not isinstance(codigo, str):
        return "Error: entrada debe ser un string"
    with open("salidas.txt", "r") as archivo:
        lineas = archivo.readline()
        while lineas != "":
            lineas = lineas.strip().split(";")
            if lineas[1] == codigo:
                return False
            lineas = archivo.readline()
    return True

#E: n/a
#S: n/a, su funcion es eliminar una linea del archivo  mediantes el codigo
#R: valida si el codigo ya existe en el archivo, verifica si el codigo esta vinculado a una parada o salida
def eliminar_rutas():
    rutas = leerArchivo("rutas.txt")
    mostrar("rutas.txt")

    while True:
        try:
            print("Ingrese el codigo de ruta(Codigo salida - Codigo llegada)")
            llegada = input("Ingre solo el codigo de llegada(ejemp: LIM): ").upper()
            salida = input("Ingre solo el codigo de salida(ejemp: SJO): ").upper()
            
            codigo = llegada + "-" + salida
            if not verificar_rutas(codigo, "rutas.txt"):
                print("Error: el codigo de ruta no existe en el registro")
            else:
                break
        except:
            print("Error")
            
    if verificar_paradas_rutas(codigo):       
        if verificar_salidas_rutas(codigo):
            with open("rutas.txt", "w") as archivo:
                i = 0
                while i< len(rutas):
                    if codigo != rutas[i][0]:
                        archivo.write(rutas[i][0] + ";" + rutas[i][1] + ";" + rutas[i][2] + ";" + rutas[i][3] + ";" + rutas[i][4] + "\n")
                    i+= 1
                print("ruta eliminada")
        else:
            print("Error: la ruta no debe estar vinculado a salidas programadas")
    else:
        print("Error: la ruta no debe estar vinculado a paradas registradas")

#E: n/a
#S: modifica una linea del archivo txt por medio de un indice
#R: el codigo ingresada no puede existir en el archivo, km = int, km >0
def modificar_rutas():
    rutas = leerArchivo("rutas.txt")
    mostrar("rutas.txt")
    while True:
        indice = int(input("selecione el indice de la fila que desea modificar: "))

        if indice < 1 or indice > len(rutas):
            print("Error: indice no esta dentro del rango")
        else:
            break
    
    while True:
        try:
            print("Ingrese el codigo de ruta(Codigo salida - Codigo llegada)")
            llegada = input("Ingre solo el codigo de llegada(ejemp: LIM): ").upper()
            salida = input("Ingre solo el codigo de salida(ejemp: SJO): ").upper()
            
            codigo = llegada + "-" + salida
            if verificar_rutas(codigo, "rutas.txt"):
                codigo = ""
                break
            else:
                break
        except:
            print("Error")
    origen = input("Ingrese el nombre del lugar de origen: ")
    destino = input("Ingrese el nombre del lugar de destino: ")
    
    while True:
        try:
            km = int(input("Ingrese la distancia total en kilometros(km): "))
            km =str(km)
            break
        except:
            print("Error: la entrada debe ser un numero entero")
    
    while True:
        try:
            tarifa = int(input("ingrese el valor en colones: "))
            if tarifa < 1:
                print("Error: la tarifa debe ser superior a 0")
            else:
                tarifa = str(tarifa)
                break
        except:
            print("Error: la entrada no es un numero entero")
    
    if codigo != "":
        rutas[indice-1][0] = codigo
    if origen != "":
        rutas[indice-1][1] = origen
    if destino != "":
        rutas[indice-1][2] = destino
    if km != "":
        rutas[indice-1][3] = km
    if tarifa != "":
        rutas[indice-1][4] = tarifa
    
    with open("rutas.txt", "w") as archivo:
        i = 0
        while i < len(rutas):
            archivo.write(rutas[i][0] + ";" + rutas[i][1] + ";" + rutas[i][2] + ";" + rutas[i][3] + ";" + rutas[i][4]+"\n")
            i+= 1
    print("Se modifico con exito")

#E: ruta
#S: retorna una lista de archivo de texto d eparadas
#R: entrada debe ser tipo string
def extraer_lista(ruta):
    if not isinstance(ruta, str):
        return "Errror: entrada debe ser tipo string"
    lista = []
    with open("paradas.txt","r") as archivo:
        lineas = archivo.readline()
        while lineas != "":
            linea = lineas.strip().split(";")
            if linea[0] == ruta.upper(): 
                lista += [linea]
            lineas = archivo.readline()
    return lista
