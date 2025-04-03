# En su proyecto, un usuario registrado debe tener como atributos (nombre, apellido, dni, email). Debe
# además agregar una opción que permita ingresar un usuario como invitado,el cual no necesita proporcionar
# su usuario y contraseña. La información de este tipo de usuario (Nombre, apellido, dni, email ,
# cantidadvecesingresa) debe persistir en el sistema entre cierres del mismo.

class Usuario():
    def __init__(self,nombre,apellido,dni,email):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.email = email

class UsuarioRegistrado(Usuario):
    def __init__(self,nombre,apellido,dni,email,nombre_usuario,contraseña):
        super().__init__(nombre,apellido,dni,email)
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña

class UsuarioInvitado(Usuario):
    def __init__(self, nombre, apellido, dni, email, veces_ingresa):
        super().__init__(nombre, apellido, dni, email)
        self.veces_ingresa = veces_ingresa
def menu():
    dic_usuarios = {}
    while True:
        print("\nMenú:")
        print("a. Registrar un usuario")
        print("b. Ingresar como usuario registrado")
        print("c. Ingresar como invitado")
        print("d. Cambiar contraseña de usuario registrado")
        print("d. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "a":
            nombre_usuario = input("Nombre usuario")
            contraseña = input("Contraseña")
            valor = dic_usuarios.get(contraseña)
            if valor is None:
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                dni = input("DNI: ")
                email = input("Email: ")
                dic_usuarios[contraseña] = UsuarioRegistrado(nombre, apellido, dni, email, nombre_usuario, contraseña)
                print("Usuario registrado exitosamente.")
            else:
                print("Contraseña ya utilizada.")
                break

        elif opcion == "b":
            contraseña = input("Contraseña: ")
            
            valor = dic_usuarios.get(contraseña)
            if valor is not None:
                if isinstance(valor, UsuarioRegistrado):
                    print("Bienvenido", valor.nombre, valor.apellido)
            else:
                print("Contraseña incorrecta.")