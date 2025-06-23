usuarios = []

def ingresar_usuario():
    nombre = input("Ingrese nombre de usuario: ")
    
    for usuario in usuarios:
        if usuario["nombre"] == nombre:
            print("Usuario ya existe. Intente otro.")
        return

    sexo = input("Ingrese sexo: ").upper()
    
    while sexo not in ["M", "F"]:
        print("Debe ingresar M o F solamente. Intente de nuevo.")
        
        sexo = input("Ingrese sexo: ").upper()
    contraseña = input("Ingrese contraseña: ")
        
    while len(contraseña) < 8 or " " in contraseña:
            print("Contraseña no válida. Intente otra.")
            contraseña = input("Ingrese contraseña: ")
            usuario = {"nombre": nombre, "sexo": sexo, "clave": contraseña}
            usuarios.append(usuario)
    
    print("Usuario ingresado con éxito!!")



def buscar_usuario():
 nombre = input("Ingrese usuario a buscar: ")

 for usuario in usuarios:
  if usuario["nombre"] == nombre:
   print("El sexo del usuario es:", usuario["sexo"], "y la contraseña es:", usuario["clave"])
  return

 print("El usuario no se encuentra.")




def eliminar_usuario():
 nombre = input("Ingrese usuario a buscar: ")

 for usuario in usuarios:
  if usuario["nombre"] == nombre:
    usuarios.remove(usuario)
  print("Usuario eliminado con éxito!")
  return
 print("No se pudo eliminar usuario!")


while True:
  print("MENU PRINCIPAL")
  print("1.- Ingresar usuario.")
  print("2.- Buscar usuario.") 
  print("3.- Eliminar usuario.")
  print("4.- Salir.")

  opcion=int(input("Ingrese opción: "))

  if opcion == 1:
    ingresar_usuario()
  elif opcion == 2:
    buscar_usuario()
  elif opcion == 3:
    eliminar_usuario()
  elif opcion == 4:
    print("Programa terminado...")
    break

  

 
  
  
