import os
campus = {
    "Campus Uno": [
        {
            "nombre": "SERVICIOS",
            "capa": "Núcleo",
            "vlan": "N/A",
            "ip": "192.168.1.1",
            "servicios": ["Enrutamiento", "Conectividad inter-VLAN"]
        },
        {
            "nombre": "PROCESOS",
            "capa": "Distribución",
            "vlan": "VLAN 20",
            "ip": "192.168.20.1",
            "servicios": ["Conmutación de VLAN"]
        },
        {
            "nombre": "IMPRESIÓN FOTOCOPIADORAS",
            "capa": "Acceso",
            "vlan": "VLAN 30",
            "ip": "192.168.30.1",
            "servicios": ["Acceso a la red"]
        },
        {
            "nombre": "SITELOCAL",
            "capa": "Distribución",
            "vlan": "N/A",
            "ip": "192.168.40.1",
            "servicios": ["OSPF Área 0"]
        }
    ],
    "Campus Matriz": [
        {
            "nombre": "VENTAS",
            "capa": "Acceso",
            "vlan": "VLAN 10",
            "ip": "192.168.10.1",
            "servicios": ["Conmutación de VLAN"]
        },
        {
            "nombre": "PROCESOS",
            "capa": "Distribución",
            "vlan": "VLAN 20",
            "ip": "192.168.20.2",
            "servicios": ["Conmutación de VLAN"]
        },
        {
            "nombre": "FINANZAS",
            "capa": "Distribución",
            "vlan": "VLAN 30",
            "ip": "192.168.30.2",
            "servicios": ["Conmutación de VLAN"]
        },
        {
            "nombre": "BACK BONE MATRIZ",
            "capa": "Núcleo",
            "vlan": "N/A",
            "ip": "192.168.1.2",
            "servicios": ["Enrutamiento", "Conectividad inter-VLAN"]
        }
    ],
    "Sector Outsourcing": [
        {
            "nombre": "RRPP",
            "capa": "Acceso",
            "vlan": "VLAN 40",
            "ip": "192.168.40.1",
            "servicios": ["Acceso a la red"]
        }
    ],
    "Internet Data Center Externo": [
        {
            "nombre": "DUAL STACK",
            "capa": "Acceso",
            "vlan": "N/A",
            "ip": "acad.de:fe:30::/64",
            "servicios": ["Dual Stack (IPv4/IPv6)"]
        }
    ]
}

def mostrar_dispositivos(campus_name):
    campus_name_lower = campus_name.strip().lower()  
    found = False
    for key in campus:
        if key.lower() == campus_name_lower:
            print(f"\nDispositivos en {key}:")
            for dispositivo in campus[key]:
                print(f"\nNombre: {dispositivo['nombre']}")
                print(f"Capa: {dispositivo['capa']}")
                print(f"VLAN: {dispositivo['vlan']}")
                print(f"Dirección IP: {dispositivo['ip']}")
                print(f"Servicios: {', '.join(dispositivo['servicios'])}")
            found = True
            break
    
    if not found:
        print(f"Campus '{campus_name}' no encontrado. Por favor, ingrese un nombre válido.")

def listar_campus():
    print("Campus disponibles:")
    for key in campus:
        print(f" - {key}")

def agregar_dispositivo(campus_name, dispositivo):
    campus_name_lower = campus_name.strip().lower()  
    for key in campus:
        if key.lower() == campus_name_lower:
            campus[key].append(dispositivo)
            print(f"Dispositivo '{dispositivo['nombre']}' agregado al {key}.")
            return
    print(f"Campus '{campus_name}' no encontrado.")

def agregar_campus(nuevo_campus):
    if nuevo_campus not in campus:
        campus[nuevo_campus] = []
        print(f"Nuevo campus '{nuevo_campus}' agregado.")
    else:
        print("El campus ya existe.")

def eliminar_dispositivo(campus_name, dispositivo_nombre):
    campus_name_lower = campus_name.strip().lower()  
    for key in campus:
        if key.lower() == campus_name_lower:
            for dispositivo in campus[key]:
                if dispositivo["nombre"].lower() == dispositivo_nombre.lower():
                    campus[key].remove(dispositivo)
                    print(f"Dispositivo '{dispositivo_nombre}' eliminado de {key}.")
                    return
            print("Dispositivo no encontrado en este campus.")
            return
    print(f"Campus '{campus_name}' no encontrado.")

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Ver dispositivos en un campus")
        print("2. Agregar dispositivo a un campus")
        print("3. Agregar un nuevo campus")
        print("4. Eliminar dispositivo de un campus")
        print("5. Listar campus disponibles")
        
        opcion = input("Elige una opción (o escribe 'salir'): ")

        if opcion == "1":
            listar_campus()  
            campus_name = input("Ingrese el nombre del campus (o escribe 'salir' para volver al menú): ")
            if campus_name.lower() == 'salir':
                continue
            mostrar_dispositivos(campus_name)
        elif opcion == "2":
            listar_campus()
            campus_name = input("Ingrese el nombre del campus (o escribe 'salir' para volver al menú): ")
            if campus_name.lower() == 'salir':
                continue
            dispositivo = {
                "nombre": input("Nombre del dispositivo (o escribe 'salir' para volver al menú): "),
                "capa": input("Capa (Núcleo, Distribución, Acceso) (o escribe 'salir' para volver al menú): "),
                "vlan": input("VLAN (si aplica) (o escribe 'salir' para volver al menú): "),
                "ip": input("Dirección IP (o escribe 'salir' para volver al menú): "),
                "servicios": input("Servicios (separados por comas) (o escribe 'salir' para volver al menú): ").split(", ")
            }
            if dispositivo["nombre"].lower() == 'salir' or dispositivo["capa"].lower() == 'salir' or dispositivo["vlan"].lower() == 'salir' or dispositivo["ip"].lower() == 'salir':
                continue
            agregar_dispositivo(campus_name, dispositivo)
        elif opcion == "3":
            nuevo_campus = input("Ingrese el nombre del nuevo campus (o escribe 'salir' para volver al menú): ")
            if nuevo_campus.lower() == 'salir':
                continue
            agregar_campus(nuevo_campus)
        elif opcion == "4":
            listar_campus()
            campus_name = input("Ingrese el nombre del campus (o escribe 'salir' para volver al menú): ")
            if campus_name.lower() == 'salir':
                continue
            dispositivo_nombre = input("Ingrese el nombre del dispositivo a eliminar (o escribe 'salir' para volver al menú): ")
            if dispositivo_nombre.lower() == 'salir':
                continue
            eliminar_dispositivo(campus_name, dispositivo_nombre)
        elif opcion == "5":
            listar_campus()
        elif opcion == "6" or opcion.lower() == "salir":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()

