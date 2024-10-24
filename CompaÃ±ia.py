from Personal import Personal

class Compañia: 

    def __init__(self):
        self.personal: list[Personal] = []

    #funcion que pide los datos del trabajador 
    def personal_data(self):
       nombre = input("Por favor ingrese su nombre: ")
       cedula = input("Por favor ingrese su numero de cedula: ")
       tip_tren = input("Por favor ingrese el tipo de tren S/C: ")
       ho_tra = input("Por favor ingrese la cantiad de horas de trabajo: ")
       



    #Menu
    def menu(self):
        res = 's'
        while res == 's':
            option = input('''
                1. Ingresar datos
                ''')
            if option == "1":
                self.personal_data()
            else:
                ans = input('Desea continuar (s/n)?: ').lower()

        