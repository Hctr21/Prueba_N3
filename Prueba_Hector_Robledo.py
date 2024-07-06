import numpy as np
import json

def isNum():
    while True:
        try:
            num = input()
            num = int(num)
            break
        except ValueError:
            print("Error, se esperaba un número entero, reintente")
    return num

def showMenu():
    print("""
SERVICIO DE ATENCIÓN MÉDICA VETERINARIA
    1) Crear Ficha Mascota
    2) Buscar por Código Mascota
    3) Eliminar por Código Mascota
    4) Listar Mascotas
    5) Salir
    Ingrese una opción: """, end="")

def Codigo_Mascota():
    while True:
        Codigo = input()
        if Codigo == "":
            print("Error, campo ingresado vacío, reintente.")
        else:
            break
    return Codigo

def showPacient(paciente):
    print("Nombre Mascota:", paciente['Nombre'])
    print("Código Mascota:", paciente['Código Mascota'])
    print("Edad Mascota:", paciente['Edad Mascota'])
    print("Peso:", paciente['Peso'])
    print("Raza:", paciente['Raza'])
    print("Especie:", paciente['Especie'])
    print(f"Diagnóstico: {paciente['Diagnostico']}")
    print(f"Medicamentos recetados: {paciente['Medicamentos']}")

def guardarDatos():
    datos = []
    for i in range(f):
        paciente = {
            'Nombre Mascota': pac[i, 0],
            'Código Mascota': pac[i, 1],
            'Edad Mascota': pac[i, 2],
            'Peso': pac[i, 3],
            'Raza': pac[i, 4],
            'Especie': pac[i, 5],
            'Diagnóstico': pac[i, 6],
            'Medicamentos': pac[i, 7]
        }
        datos.append(paciente)
    
    with open('pacientes.json', 'w') as file:
        json.dump(datos, file, indent=4)

def cargarDatos():
    global f
    try:
        with open('pacientes.json', 'r') as file:
            datos = json.load(file)
        
        f = len(datos)
        for i, paciente in enumerate(datos):
            pac[i, 0] = paciente['Nombre Mascota']
            pac[i, 1] = paciente['Código Mascota']
            pac[i, 2] = paciente['Edad Mascota']
            pac[i, 3] = paciente['Peso']
            pac[i, 4] = paciente['Raza']
            pac[i, 5] = paciente['Especie']
            pac[i, 6] = paciente['Diagnóstico']
            pac[i, 7] = paciente['Medicamentos']
    
    except FileNotFoundError:
        f = 0

pac = np.empty([50, 8], dtype="object")
f = 0

cargarDatos()

while True:
    showMenu()
    op = isNum()
    match op:
        case 1:
            for i in range(8):
                if i == 0:
                    pac[f, i] = input("Ingrese el nombre de la mascota: ")
                elif i == 1:
                    print("Ingrese el código de la mascota: ", end="")
                    pac[f, i] = Codigo_Mascota()
                elif i == 2:
                    pac[f, i] = input("Ingrese la edad: ")
                elif i == 3:
                    pac[f, i] = input("Ingrese el peso: ")
                elif i == 4:
                    pac[f, i] = input("Ingrese la raza: ")
                elif i == 5:
                    pac[f, i] = input("Ingrese la especie: ")
                elif i == 6:
                    pac[f, i] = input("Ingrese el diagnóstico: ")
                elif i == 7:
                    pac[f, i] = input("Ingrese medicamentos recetados: ")
            f += 1
            print("Mascota ingresada con éxito.")
            guardarDatos()
        
        case 2:
            x = input("Ingrese el código a buscar: ")
            paciente_encontrado = False
            for i in range(f):
                if x == pac[i, 1]:
                    paciente = {
                        'Nombre': pac[i, 0],
                        'Código Mascota': pac[i, 1],
                        'Edad Mascota': pac[i, 2],
                        'Peso': pac[i, 3],
                        'Raza': pac[i, 4],
                        'Especie': pac[i, 5],
                        'Diagnostico': pac[i, 6],
                        'Medicamentos': pac[i, 7]
                    }
                    showPacient(paciente)
                    paciente_encontrado = True
                    break
            if not paciente_encontrado:
                print("Paciente no encontrado.")
        
        case 3:
            x = input("Ingrese el código a eliminar: ")
            des = input('¿Está seguro de eliminarlo?(S/N): ')
            if des == 'S':
                paciente_encontrado = False
                for i in range(f):
                    if x == pac[i, 1]:
                        pac = np.delete(pac, i, axis=0)
                        f -= 1
                        guardarDatos()
                        print("Paciente eliminado con éxito.")
                        paciente_encontrado = True
                        break
                if not paciente_encontrado:
                    print("Paciente no encontrado.")
            elif des == 'n':
                continue
            
        
        case 4:
            for i in range(f):
                print("\nPaciente:")
                paciente = {
                    'Nombre': pac[i, 0],
                    'Código Mascota': pac[i, 1],
                    'Edad Mascota': pac[i, 2],
                    'Peso': pac[i, 3],
                    'Raza': pac[i, 4],
                    'Especie': pac[i, 5],
                    'Diagnostico': pac[i, 6],
                    'Medicamentos': pac[i, 7]
                }
                showPacient(paciente)

        case 5:
            break