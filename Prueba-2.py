import re

class Router:
    def __init__(self, nombre, direcciones_ip, protocolos, capa):
        self.nombre = nombre
        self.direcciones_ip = direcciones_ip
        self.protocolos = protocolos
        self.capa = capa

    def __repr__(self):
        return f"Router: {self.nombre}, IPs: {self.direcciones_ip}, Protocolos: {self.protocolos}, Capa: {self.capa}"

class GrupoRed:
    def __init__(self, nombre, rango_ip, protocolo):
        self.nombre = nombre
        self.rango_ip = rango_ip
        self.protocolo = protocolo
        self.routers = []

    def agregar_router(self, router):
        self.routers.append(router)

    def eliminar_router(self, router_nombre):
        for router in self.routers:
            if router.nombre == router_nombre:
                self.routers.remove(router)
                return True
        return False

    def __repr__(self):
        return f"Grupo: {self.nombre}, Rango IP: {self.rango_ip}, Protocolo: {self.protocolo}, Routers: {[router.nombre for router in self.routers]}"

grupos = []

grupo_internet = GrupoRed("Internet", "8.8.8.0/24", "BGP 63000")
router_isp = Router("ISP", ["8.8.8.1/24"], ["BGP 63000"], "Capa de Acceso a Internet (Capa Core hacia el proveedor ISP)")
grupo_internet.agregar_router(router_isp)
grupos.append(grupo_internet)

grupo_backbone = GrupoRed("Backbone MPLS", "172.16.100.0/24", "OSPF Área 0")
router_r9 = Router("R9", ["172.16.100.9/24", "172.16.101.9/24"], ["OSPF Área 0", "BGP 12345"], "Capa Core")
router_r10 = Router("R10", ["172.16.100.10/24", "172.16.101.10/24"], ["OSPF Área 0"], "Capa Core")
grupo_backbone.agregar_router(router_r9)
grupo_backbone.agregar_router(router_r10)
grupos.append(grupo_backbone)

grupo_ospf_123 = GrupoRed("OSPF Área 123", "172.16.102.0/24", "OSPF Área 123")
router_r12 = Router("R12", ["172.16.102.12/24"], ["OSPF Área 123"], "Capa Distribución")
router_r13 = Router("R13", ["172.16.102.13/24"], ["OSPF Área 123"], "Capa Distribución")
grupo_ospf_123.agregar_router(router_r12)
grupo_ospf_123.agregar_router(router_r13)
grupos.append(grupo_ospf_123)

def validar_ip(ip):
    patron = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]{1,2}$")
    return patron.match(ip)

def mostrar_grupos():
    print("\n--- Grupos de Red ---")
    for grupo in grupos:
        print(grupo)

def mostrar_routers():
    print("\n--- Routers y detalles ---")
    for grupo in grupos:
        for router in grupo.routers:
            print(f"Grupo: {grupo.nombre}")
            print(f"  - {router}")

def generar_documento():
    print("\n--- Documento de Dispositivos de Red Documentados ---")
    for grupo in grupos:
        for router in grupo.routers:
            print(f"Dispositivo: {router.nombre}")
            print(f"  a. Dirección IP: {', '.join(router.direcciones_ip)}")
            print(f"  b. Servicios de red comprometidos: {', '.join(router.protocolos)}")
            print(f"  c. Capa a la que pertenece (Modelo jerárquico): {router.capa}")
            print("---")

def mostrar_grupos_disponibles():
    print("\n--- Grupos Disponibles ---")
    for grupo in grupos:
        print(f"- {grupo.nombre}")

def agregar_router():
    mostrar_grupos_disponibles()
    grupo_nombre = input("Ingrese el nombre del grupo al que se agregará el router: ")
    for grupo in grupos:
        if grupo.nombre == grupo_nombre:
            nombre_router = input("Ingrese el nombre del router: ")
            if any(r.nombre == nombre_router for r in grupo.routers):
                print("Ya existe un router con ese nombre en el grupo.")
                return
            ip_router = input("Ingrese las direcciones IP del router (separadas por comas): ").split(",")
            if not all(validar_ip(ip.strip()) for ip in ip_router):
                print("Una o más direcciones IP no tienen el formato correcto.")
                return
            protocolos_router = input("Ingrese los protocolos del router (separados por comas): ").split(",")
            capa_router = input("Ingrese la capa a la que pertenece el router: ")
            nuevo_router = Router(nombre_router, ip_router, protocolos_router, capa_router)
            grupo.agregar_router(nuevo_router)
            print(f"Router {nombre_router} agregado al grupo {grupo_nombre}.")
            return
    print("Grupo no encontrado.")

def eliminar_router():
    nombre_router = input("Ingrese el nombre del router a eliminar: ")
    for grupo in grupos:
        if grupo.eliminar_router(nombre_router):
            print(f"Router {nombre_router} eliminado del grupo {grupo.nombre}.")
            return
    print("Router no encontrado.")

def buscar_router():
    nombre_router = input("Ingrese el nombre del router a buscar: ")
    for grupo in grupos:
        for router in grupo.routers:
            if router.nombre == nombre_router:
                print(f"Router encontrado en el grupo {grupo.nombre}:")
                print(f"  - {router}")
                return
    print("Router no encontrado.")

def resumen_red():
    print("\n--- Resumen de la Red ---")
    total_routers = sum(len(grupo.routers) for grupo in grupos)
    print(f"Total de routers: {total_routers}")
    for grupo in grupos:
        print(f"{grupo.nombre}: {len(grupo.routers)} routers")
    protocolos = {}
    for grupo in grupos:
        for router in grupo.routers:
            for protocolo in router.protocolos:
                if protocolo in protocolos:
                    protocolos[protocolo] += 1
                else:
                    protocolos[protocolo] = 1
    print("Protocolos más utilizados:")
    for protocolo, cantidad in protocolos.items():
        print(f"  {protocolo}: {cantidad} uso(s)")

def menu():
    while True:
        print("\n--- Menú de Red ---")
        print("1. Mostrar Grupos de Red")
        print("2. Mostrar Routers y detalles")
        print("3. Generar documento de dispositivos")
        print("4. Agregar un router")
        print("5. Eliminar un router")
        print("6. Buscar un router")
        print("7. Resumen de la red")
        print("8. Salir")
        opcion = input("Seleccione una opción (1-8): ")

        if opcion.isdigit() and 1 <= int(opcion) <= 8:
            opcion = int(opcion)
            if opcion == 1:
                mostrar_grupos()
            elif opcion == 2:
                mostrar_routers()
            elif opcion == 3:
                generar_documento()
            elif opcion == 4:
                agregar_router()
            elif opcion == 5:
                eliminar_router()
            elif opcion == 6:
                buscar_router()
            elif opcion == 7:
                resumen_red()
            elif opcion == 8:
                print("Saliendo del programa.")
                break
        else:
            print("Opción no válida, por favor ingrese un número entre 1 y 8.")

menu()
