import json
import time
from datetime import datetime
usuarios={}
libros={}

def validacion_Encontrar_Libro(titulo, codigo):
    for titulo in libros:
        if titulo['Codigo'] == codigo:
            return titulo
    return None

def ValidacionCode(codigo):
    try:
        codigo_num = int(codigo)
        if codigo_num < 0:
            print('Error ⚠️ No se permite números negativos')
            return None
        return codigo_num
    except ValueError:
        print('No se permite ingresar letras, ejemplo: (002)')
        return None
    
def ValidacionFech(fecha):
    try:
        fecha = datetime.strptime(fecha, '%Y-%m-%d')
        return fecha
    except ValueError:
        print('Error, ingrese la fecha de esta forma si no sabe como escribirlo (Año,Dia,Mes ejemplo: (2024-05-09))')
        return None

def cargarUsuario ():
    try: 
        with open ('bd/usuarios.json' , 'r') as file:
            return file.load(file)
    except FileNotFoundError:
        return {}    
    except json.JSONDecodeError:
        return {}    

def saveDataUsuarios(usuarios):
    with open('bd/usuarios.json', 'w') as file:
        json.dump(usuarios, file, indent=4)

def validarDats(usuarios):
    documento = input("Ingresa el numero de documento: ")

    #Se hace verificacion si el usuario ya existe
    if documento in usuarios:
        print("La identificacion ya esta registrada")
        return False
    else:

        #Funcion para crear usuario
        nombre = input("Ingresa el nombre: ")
        cargo = input("Ingresa el cargo: ")
        email = input ("Ingresa el correo: ")
        contraseña = input ("Ingresa la contraseña: ")

        usuarios[documento]={
            "nombre":nombre,
            "cargo":cargo,
            "email":email,
            "contraseña": contraseña
            }
        print("Usuario creado exitosamente")
    return usuarios

def eliminarUser():
    try:
        IDelimar=input('Digte el documento del usuario que desea eliminar: ')
        if IDelimar in usuarios:
            print('Usuario eliminado exitosamente')
        else:
            print('Usuario no encontrado')
    except ValueError:
        print('Error vuelve a intentar')
        return IDelimar

def Gestiondelibros():
    codigo=input('Ingrese el codigo: ')

    if codigo in libros:
        print("El codigo ya se encuentra registrado")
        return False
    else:
       
       libroTitulo=input('Ingrese el título del libro: ')
       if not ValidacionCode(codigo):
           return
       sinopsis=input('Digite la sinopsis del libro: ')
       autor=input('Ingrese el nombre del autor del libro: ')
       fecha=input('Ingrese la fecha de publicación: ')
       fecha= ValidacionFech(fecha)
       cantidades=input('Ingrese la cantidad disponibles del libro: ')
       if not ValidacionCode(codigo):
           return
       libros[codigo]={
        "Codigo":codigo,
        "Titulo":libroTitulo,
        "sinopsis": sinopsis,
        "autor": autor,
        "cantidades": cantidades
        }
       print("Usuario creado exitosamente")
    return codigo

def eliminarLIbro():
    try:
        Libelimar=input('Digte el codigo del libro que desea eliminar: ')
        if Libelimar in libros:
            print('Libro eliminado exitosamente')
        else:
            print('Libro no encontrado')
    except ValueError:
        print('Error vuelve a intentar')
        return Libelimar   

def Listartitulos():

    print('*************** HISTORIAL ****************')
    codigo=input('Ingrese el código del libro: ')
    codigo = ValidacionCode(codigo)
    if codigo is None:
        return
    titulo= validacion_Encontrar_Libro(titulo, codigo)
    if titulo is None:
        print('libro del titulo no encontrado')
        return
    print('Cargando historial...')
    time.sleep(1.5)
    print('****************************************************************')
    print(f"titulo del libro: {libros['libroTitulo']} Código: {libros['Codigo']}")
    print(f"Autor: {libros['autor']}, cantidades: {libros['cantidades']}")
    print(f'Sinopsis: {libros['sinopsis']}')
    print('****************************************************************')
    
    if not titulo['codigo']:
        print('***** No hay historial de ese codigo *****')
        return

def menu():

    while True:
        print('1. Gestion de usuarios\n'
            '2. Gestion de libros\n'
            '3. Reporte de libros\n'
            '0. Salir\n')
        opcion=input('--> ')

        if opcion=='1':
            ()
        elif opcion=='2':
            ()
        elif opcion =='3':
            ()
        elif opcion == '0':
            print('Hasta luego...')  
            time.sleep(1.6)   
            print('vuelve pronto ♥')
            break
        else:
            print('Error, escoge una opción del (1 al 4). Gracias ♥') 
            
menu()    