# src/main.py

from auth import registrar_usuario, login


def mostrar_menu_inicio():
    """
    Menú principal del programa.
    """
    print("\n===== ATMOS-APP =====")
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Salir")


def hacer_registro():
    """
    Pide los datos para crear un nuevo usuario.
    """
    print("\n--- REGISTRO ---")

    usuario = input("Usuario: ")
    email = input("Email: ")
    contrasena = input("Contraseña: ")

    correcto, mensaje = registrar_usuario(usuario, email, contrasena)
    print(mensaje)


def hacer_login():
    """
    Pide email y contraseña para intentar entrar al sistema.
    Devuelve True o False según el resultado.
    """
    print("\n--- LOGIN ---")

    email = input("Email: ")
    contrasena = input("Contraseña: ")

    correcto, mensaje = login(email, contrasena)
    print(mensaje)

    return correcto


def menu_atmos_app():
    """
    Aquí iría la lógica real de vuestro proyecto.
    De momento dejamos un ejemplo sencillo.
    """
    print("\nHas accedido a Atmos-App.")

    while True:
        print("\n--- MENÚ INTERNO ATMOS-APP ---")
        print("1. Ejecutar módulo principal")
        print("2. Cerrar sesión")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            print("Aquí iría el código real de vuestra aplicación.")

        elif opcion == "2":
            print("Cerrando sesión...")
            break

        else:
            print("Opción no válida.")


def main():
    """
    Bucle principal del programa.
    """
    while True:
        mostrar_menu_inicio()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            hacer_registro()

        elif opcion == "2":
            acceso = hacer_login()

            if acceso:
                menu_atmos_app()

        elif opcion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")


# Este bloque hace que el programa arranque desde este archivo
if __name__ == "__main__":
    main()
