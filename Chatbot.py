# Proyecto: Chatbot IT - UTN

import json
import os
import random
from datetime import datetime

# Constante global para definir la ruta del archivo de la base de datos
DB_FILE = 'tickets.json'


# CAPA DE ACCESO A DATOS (PERSISTENCIA)


def inicializar_base_datos():
    """Crea el archivo JSON si no existe en el sistema."""
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, 'w') as file:
            json.dump({"tickets": {}}, file)

def cargar_datos():
    """Lee y retorna los datos actuales de la base de datos JSON."""
    with open(DB_FILE, 'r') as file:
        return json.load(file)

def guardar_datos(data):
    """Sobrescribe el archivo JSON con los datos actualizados."""
    with open(DB_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def crear_ticket(legajo, tipo_solicitud, estado):
    """Genera un nuevo ticket, lo persiste en el JSON y retorna el ID generado."""
    data = cargar_datos()
    ticket_id = str(random.randint(10000, 99999))
    
    data['tickets'][ticket_id] = {
        "legajo": legajo,
        "tipo": tipo_solicitud,
        "estado": estado,
        "fecha_creacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    guardar_datos(data)
    return ticket_id

def obtener_ticket(ticket_id):
    """Busca un ticket por su ID. Retorna el diccionario o None si no existe."""
    data = cargar_datos()
    return data['tickets'].get(ticket_id)


# CAPA DE LÓGICA DE NEGOCIO (EL CHATBOT)


def fase_autenticacion():
    """Maneja el estado inicial con validación estricta usando try/except."""
    while True:
        ingreso = input("\n[Sistema]: Por favor, ingrese su numero de legajo para comenzar: ").strip()
        
        try:
            # Se intenta convertir la entrada a entero. Si tiene letras, lanza ValueError
            legajo_num = int(ingreso)
            
            if legajo_num <= 0:
                # Se lanza el propio error si ingresan números negativos
                raise ValueError("El legajo debe ser un número positivo.")
                
            print(f"[Sistema]: Autenticación exitosa. Bienvenido, usuario {ingreso}.")
            return ingreso # Se retorna el string original válidado
            
        except ValueError as e:
            # Captura tanto el error de int() como el que se levanta en el código
            print(f"[Error]: Entrada no válida. Debe ingresar únicamente números enteros. ({e})")

def gestionar_incidente(legajo, tipo_incidente):
    """Procesa la creación de tickets con validación estricta de caracteres."""
    print(f"\n[Sistema]: Ha seleccionado: {tipo_incidente}.")
    print("[Sistema]: ¿Desea intentar una resolución automática en este momento (A) o derivar el ticket para revisión técnica manual (B)?")
    
    decision = input("[Usuario] (A/B): ").strip().upper()

    try:
        if decision not in ['A', 'B']:
            # Se fuerza un ValueError si ingresan numeros u otras letras
            raise ValueError("La opción ingresada no es reconocida.")
            
        if decision == 'A':
            print("[Sistema]: Ejecutando protocolos de resolución automática...")
            estado = "Resuelta"
            ticket_id = crear_ticket(legajo, tipo_incidente, estado)
            print(f"[Sistema]: Operación finalizada con éxito. Su número de ticket es: {ticket_id}")
            
        elif decision == 'B':
            estado = "Pendiente"
            ticket_id = crear_ticket(legajo, tipo_incidente, estado)
            print(f"[Sistema]: Solicitud derivada al equipo de Soporte Nivel 2. Su número de ticket es: {ticket_id}")

    except ValueError as e:
        print(f"[Error]: {e} Por favor, ingrese únicamente la letra 'A' o 'B'. Operación cancelada.")

def consultar_estado():
    """Procesa la consulta asegurando que el ID buscado sea un número."""
    ticket_id = input("\n[Sistema]: Ingrese el número de ticket que desea consultar: ").strip()
    
    try:
        # Se valida que el ID no contenga letras antes de ir a buscarlo
        int(ticket_id)
        
        ticket_data = obtener_ticket(ticket_id)
        
        if ticket_data:
            print("\n--- DETALLES DEL TICKET ---")
            print(f"ID del Ticket   : {ticket_id}")
            print(f"Legajo Asociado : {ticket_data['legajo']}")
            print(f"Tipo de Falla   : {ticket_data['tipo']}")
            print(f"Fecha de Alta   : {ticket_data['fecha_creacion']}")
            print(f"Estado Actual   : {ticket_data['estado'].upper()}")
            print("---------------------------")
        else:
            print(f"[Error]: No se encontraron registros para el ticket ID '{ticket_id}'.")
            
    except ValueError:
        print("[Error]: El formato del ID es incorrecto. Los tickets contienen únicamente números y no palabras.")

def fase_menu_principal(legajo):
    """Gestiona el ruteo validando que el usuario ingrese opciones numéricas válidas."""
    while True:
        print("\n" + "=" * 30)
        print("MENÚ PRINCIPAL")
        print("=" * 30)
        print("1. Solicitar restablecimiento de contraseña")
        print("2. Solicitar desbloqueo de cuenta")
        print("3. Consultar estado de solicitud")
        print("4. Salir del sistema")

        entrada_opcion = input("\n[Usuario]: ").strip()

        try:
            # Se valida que la opción del menú sea un número
            opcion = int(entrada_opcion)
            
            if opcion == 1:
                gestionar_incidente(legajo, "Restablecimiento de contraseña")
            elif opcion == 2:
                gestionar_incidente(legajo, "Desbloqueo de cuenta")
            elif opcion == 3:
                consultar_estado()
            elif opcion == 4:
                print("\n[Sistema]: Cerrando sesión. Gracias por utilizar el Chatbot.")
                break
            else:
                print("[Error]: Opción no reconocida. Ingrese un número del 1 al 4.")
                
        except ValueError:
            print("[Error]: Entrada inválida. Por favor, ingrese un NÚMERO (1, 2, 3 o 4) sin letras ni símbolos.")

def ejecutar_chatbot():
    """Método coordinador para iniciar el ciclo de vida del chatbot."""
    print("-" * 50)
    print("SISTEMA DE SOPORTE TÉCNICO IT - NIVEL 1")
    print("-" * 50)
    
    inicializar_base_datos()
    legajo_activo = fase_autenticacion()
    fase_menu_principal(legajo_activo)


# PUNTO DE ENTRADA DEL PROGRAMA

if __name__ == "__main__":
    ejecutar_chatbot()