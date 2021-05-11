#!/usr/bin/env python

"""
Modulos para exportar al proyecto py inicial
"""

def validation(NAME_ADMIN, PASS_ADMIN,KEY):
    while True:
        name = str(input("Ingrese nombre de usuario administrador: "))
        password = str(input("Ingrese contraseña de administrador: "))
        print("")
                
        if name == NAME_ADMIN and password == PASS_ADMIN:
            print("Bienvenido {}".format(name))
            print("")
            KEY = True
            break
        elif name == "exit" or password == "exit":
            exit()
        else:
            print("Datos de sesión incorrectos, intentelo de nuevo")
            print("")
# tools for admin