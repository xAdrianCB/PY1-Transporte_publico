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
#E: descripcion, modelos
#S: valor boleano segun si la entrada se encuentra en el archivo de texto (modelos)
#R: entrada debe ser string
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

#E: lista
#S: retorna la lista
#R: entrada debe ser tipo lista
def ordenar_lista(lista):
    if not isinstance(lista, list):
        return "Error: entrada debe ser una lista"
    i= 0
    while i < len(lista):
        fil = 0
        while fil < len(lista)-1:
            if lista[fil][1]>lista[fil+1][1]:
                mayor = lista[fil]
                menor = lista[fil+1]
                lista[fil] = menor
                lista[fil+1] = mayor
            fil+= 1
        i+= 1
    return lista

#E: lista
#S: retorna la lista
#R: entrada debe ser tipo lista
def mostrar_lista(lista):
    i= 0
    print(["Codigo"]+["ord"]+["Parada"]+["km"])
    while i< len(lista)-1:
        print(lista[i])
        i+= 1

#E: lista,lista2, orden
#S: retorna la lista de los elementos sustituidos
#R: lista y lista2 deben ser tipo lista, orden debe ser un numero entero
def incluir_lista(lista,lista2, orden):
    if not isinstance(lista, list):
        return "Error: entrada lista debe ser una lista"
    if not isinstance(lista2, list):
        return "Error: entrada lista2 debe ser una lista"
    if not isinstance(orden, int):
        return "Error: entrada debe ser un numero entero"
    Nlista = []
    i = 0
    a = 1
    while i< len(lista)-1:
        if i == orden:
            Nlista += [lista2]
            a+= 1
        lista[i][1] = str(a)
        Nlista += [lista[i]]
        i+= 1
        a+= 1
    return Nlista

#E: lista,codigo
#S: retorna la lista de los elementos que no tienen el elemento indicado
#R: lista deben ser tipo lista y codigo tipo string
def quitar_paradas(lista,codigo):
    if not isinstance(lista, list):
        return "Errror: entrada lista debe ser una lista"
    if not isinstance(codigo, str):
        return "Error: entrada codigo debe ser de tipo string"
    listaN = []
    while lista != []:
        if lista[0][0] != codigo:
            listaN += lista[0]
        lista = lista[1:]
    return listaN

#E: paradas, lista
#S: retorna la lista para con los lementos de la lista agregados
#R: lista y paradas deben ser tipo lista
def sumar_lista(paradas, lista):
    if not isinstance(lista, list):
        return "Error: entrada lista debe ser una lista"
    if not isinstance(paradas, list):
        return "Error: entrada paradas debe ser una lista"
    while lista != []:
        paradas += [lista[0]]
        lista = lista[1:]
    return paradas

#E: n/a
#S: n/a, incluye una nueva parada en base al indice introducido y re ordena el archivo
#R: validaciones de indice y verificacion de tipo de entrada
def incluir_paradas():
    rutas = leerArchivo("rutas.txt")
    mostrar("rutas.txt")
    while True:
        indice = int(input("digite el indice de la ruta que desea ver: "))

        if indice < 1 or indice > len(rutas):
            print("Error: indice no esta dentro del rango")
        else:
            codigo = rutas[indice-1][0]
            kmMayor = rutas[indice-1][3]
            break
    
    lista= extraer_lista(rutas[indice-1][0])
    lista = ordenar_lista(lista)
    mostrar_lista(lista)

    while True:
        orden = int(input("digite el orden deseado dentro de la lista: "))

        if orden > len(lista)+1 or orden < 1:
            print(f"Error: orden indicado tiene que ser entre 1 y {len(lista)}")
        elif orden == 1 and lista[0][3] == "0":
            print("Error: ya existe una salida para la ruta")
        else:
            break

    nombre = input("Introduzca el nombre de la parada: ")

    while True:
        #recordar que el indice real en lista es orden-1
        km = int(input("digite la cantidad de kilometros: "))
        if orden == 1 and km != 0:
            print("Error: orden en la posicion 1 debe tener 0 km")
        elif orden-1 == len(lista) and km > int(lista[orden-2][3]):
            km = str(km)
            break
        elif orden == 1 and lista == []:
            km = str(0)
            break  
        elif km >= int(lista[orden-1][3]) or km <= int(lista[orden-2][3]):
            print(f"Error: la posicion seleccionada debe tener un rango entre ({lista[orden-1][3]},{lista[orden][3]})")  
        else:
            km = str(km)
            break
    lista= incluir_lista(lista,[codigo, str(orden), nombre, km],orden-1) 
    paradas = quitar_paradas(lista,codigo)
    paradas = sumar_lista(paradas, lista)
    with open("paradas.txt", "w") as archivo:
        i = 0
        while i < len(paradas):
            archivo.write(paradas[i][0] + ";" + paradas[i][1] + ";" + paradas[i][2] + ";" + paradas[i][3] +"\n")
            i+= 1
    print("Se modifico con exito")

#E: n/a
#S: n/a, eliminar una fila y ordena el indice
#R: validaciones de indice y verificacion de tipo de entrada
def eliminar_paradas():
    rutas = leerArchivo("rutas.txt")
    mostrar("rutas.txt")
    while True:
        indice = int(input("digite el indice de la ruta que desea ver: "))

        if indice < 1 or indice > len(rutas):
            print("Error: indice no esta dentro del rango")
        else:
            codigo = rutas[indice-1][0]
            break
    
    lista= extraer_lista(rutas[indice-1][0])
    lista = ordenar_lista(lista)
    mostrar_lista(lista)

    while True:
        orden = int(input("digite el orden que desea eliminar: "))
        if orden == 1:
            km = "0"
            break
        elif orden > len(lista)+1 or orden < 1:
            print("Error: fuera de rango")
        else:
            break
    a = 1
    i = 1
    listaN = []
    while lista != []:
        if a != orden:
            lista[0][1] = str(i)
            listaN+= [lista[0]]
            i+= 1
        a+= 1
        lista = lista[1:]
    
    paradas = quitar_paradas(listaN,codigo)
    paradas = sumar_lista(paradas, listaN)
    print(paradas)
    with open("paradas.txt", "w") as archivo:
        i = 0
        while i < len(paradas):
            archivo.write(paradas[i][0] + ";" + paradas[i][1] + ";" + paradas[i][2] + ";" + paradas[i][3] +"\n")
            i+= 1
    print("Se modifico con exito")
#E: n/a
#S: n/a, modifica elementos de una lista selecionada
#R: validaciones de indice y verificacion de tipo de entrada
def modificar_paradas():
    rutas = leerArchivo("rutas.txt")
    mostrar("rutas.txt")
    while True:
        indice = int(input("digite el indice de la ruta que desea ver: "))

        if indice < 1 or indice > len(rutas):
            print("Error: indice no esta dentro del rango")
        else:
            codigo = rutas[indice-1][0]
            kmMayor = rutas[indice-1][3]
            break
    
    lista= extraer_lista(rutas[indice-1][0])
    lista = ordenar_lista(lista)
    mostrar_lista(lista)
    while True:
        indice = int(input("selecione la linea que desea modificar mediante indice: "))

        if indice < 1 or indice > len(lista):
            print("Error: indice no esta dentro del rango")
        else:
            break
    nombre= input("Ingrese el nombre de la parada: ")
    while True:
        km = input("Ingrese los kilometros: ")
        if int(lista[indice-1][1]) < len(lista) and km > kmMayor:
            print("Error: los kilometros ingresados superan el limite")
        else:
            break
    
        
                    
    if codigo != "":
        lista[indice-1][0] = codigo
    """
    if orden != "":
        lista[indice-1][1] = orden
    """
    if nombre != "":
        lista[indice-1][2] = nombre
    if km != "":
        lista[indice-1][3] = km

    paradas = quitar_paradas(lista,codigo)
    paradas = sumar_lista(paradas, lista)
    
    with open("paradas.txt", "w") as archivo:
        i = 0
        while i < len(paradas):
            archivo.write(paradas[i][0] + ";" + paradas[i][1] + ";" + paradas[i][2] + ";" +paradas[i][3] +"\n")
            i+= 1
    print("Se modifico con exito")

#E: indice
#S: retorna el elemento selecionado en la lista de rutas
#R: el indice debe estar dentro del rango, indice debe ser un numero entero y nombre_archivo un string
def obtener_elemento(indice,nombre_archivo):
    if not isinstance(indice, int):
        return "Error: "
    if not isinstance(nombre_archivo, str):
        return "Error: "
    lista = leerArchivo(nombre_archivo)
    if indice > len(lista) or indice < 0:
        return "Error: el indice no cumple con el rango"
    i = 0
    while i < len(lista):
        if i == indice-1 :
            return lista[i][0]
        i += 1

#E: hora
#s: retorna las horas en minutos
#R: n/a
def minutos(hora):
    lista = hora.split(":")
    tiempo = int(lista[0]) * 60 + int(lista[1])
    return tiempo

#E: elem,lista , indice, salida, entrada
#S: retorna valor booleano segun si encuentra un traslape
#R: n/a
def existe_traslape(elem,lista , indice,fecha, salida, entrada):
    n_salida = minutos(salida)
    n_entrada = minutos(entrada)
    i = 0
    while i < len(lista):
        if lista[i][indice] == elem and lista[i][4] == fecha:
            e_salida = minutos(lista[i][5])
            e_entrada = minutos(lista[i][6])

            if n_salida < e_entrada and n_entrada > e_salida:
                return True
        i+= 1
    return False
        
#E: fecha
#S: retorna el arreglo de los numero enteros(fechas)
#R: n/a
def conversionFecha(fecha):
    lista = fecha.split("/")
    dia = int(lista[0])
    mes = int(lista[1])
    anio= int(lista[2])
    return dia + anio*10000 + mes*100

#E: elem,lista,fecha
#S: retorna valor False si la fecha es menor al vencimiento y True sino
#R: valida que elem sea string, fecha tipo string y la lista sea tipo lista
def validar_licencia(elem,lista,fecha):
    if not isinstance(elem,str):
        return "Error: "
    if not isinstance(lista,list):
        return "Error: "
    if not isinstance(fecha,str):
        return "Error: "
    fecha = conversionFecha(fecha)
    i= 0
    while i < len(lista):
        if lista[i][0] == elem:
            vencida = conversion(lista[i][3])
            if vencida < fecha:
                return True
            else:
                return False
        i+= 1
    return False
#E: elem,lista,lista2,salida
#S:
#R:
def horas_totales(elem,lista,lista2,salida):
    return False

#E:n/a
#S:
#R:
def incluir_salidas():
    lista = leerArchivo("salidas.txt")
    mostrar("salidas.txt")
    if len(lista)+1 < 10:
        cod = "S00" + str(len(lista)+1)
    elif len(lista)+1 < 100:
        cod = "S0" + str(len(lista)+1)
    else:
        cod = "S" + str(len(lista)+1)
    print(cod)
    
    mostrar("rutas.txt")
    rutas = leerArchivo("rutas.txt")
    while True:
        try:
            indice = int(input("Ingrese el indice del codigo: "))
            if indice > len(rutas):
                print("Error: el indice supera el rango de la lista rutas")
            else:
                break
        except:
            print("Error")
    ruta = obtener_elemento(indice-1,"rutas.txt")

    while True:
        try:
            dia = input("Ingre solo el dia: ")
            mes = input("Ingrese solo el mes: ")
            anio = input("Ingrese solo el año: ")
            if int(dia) > 31 or int(dia) < 1:
                print("Error: el dia no esta dentro del rango(1 y 30)")
            elif int(mes) > 12 or int(mes) < 1:
                print("Error: el mes no esta dentro del rango(1 y 12)")
            else:
                fecha = dia + "/" + mes + "/" + anio
                print(fecha)
                break
        except:
            print("Error, alguna de las entradas no es un numero entero")

    while True:
        try:
            h_salida = input("Ingrese la hora de salida (06 o 12): ")
            m_salida = input("Ingrese los  minutos de salida(:05 o :30): ")
            h_entrada = input("Ingrese la hora de entrada(06 o 12): ")
            m_entrada = input("Ingrese los  minutos de entrada(:05 o :30): ")
            if int(h_salida) * 60 + int(m_salida) >= int(h_entrada)*60 + int(m_entrada):
                print("Error: la hora estimada de llegada no puede ser posterior a la salida")
            if int(h_salida) > 24 or int(h_entrada) > 24 :
                print("Error: las horas deben ser de un rango entre 01 al 24")
            if int(m_salida) >59 or int(m_entrada) > 59:
                print("Error: los minutos deben ser de un rango entre 00 y 59")
            else:
                salida = h_salida +":"+ m_salida
                entrada = h_entrada +":"+ m_entrada
                print(salida)
                print(entrada)
                break
        except:
            print("Error")
    
    mostrar("unidades.txt")
    unidades = leerArchivo("unidades.txt")
    while True:
        try:
            indice = int(input("Ingrese el indice del codigo: "))
            if indice > len(unidades):
                print("Error: el indice supera el rango de la lista unidades")
            
            else:
                placa = obtener_elemento(indice-1,"unidades.txt")
                print(placa)
                if existe_traslape(placa,lista,2,fecha, salida, entrada):
                    print("Error: ")
                else:
                    break
        except:
            print("Error")

    mostrar("conductores.txt")
    conductores = leerArchivo("conductores.txt")
    while True:
        try:
            indice = int(input("Ingrese el indice del codigo: "))
            if indice > len(conductores):
                print("Error: el indice supera el rango de la lista conductores")

            cedula = obtener_elemento(indice-1,"conductores.txt")
            if existe_traslape(cedula,lista,3,fecha,salida, entrada):
                print("Error: ")
            if validar_licencia(cedula,conductores,fecha):
                print("Error: ")
                
            elif horas_totales(cedula,lista,conductores,salida):
                print("Error: ")
            else:
                break
        except:
            print("Error")
    salidas = [cod + ";" + ruta + ";" + fecha + ";" + salida + ";" + entrada]
    guardarArchivo("salidas.txt",salidas[0])
