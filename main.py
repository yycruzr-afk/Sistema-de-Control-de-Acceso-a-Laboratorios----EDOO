from sistema_acceso import SistemaAcceso
from laboratorio import Laboratorio
from persona import Persona
def registrar_datos_iniciales(sistema: SistemaAcceso) -> None:
    laboratorios = [
        Laboratorio("LAB01", "Laboratorio de Programacion", 30, "Pabellon A"),
        Laboratorio("LAB02", "Laboratorio de Redes", 25, "Pabellon B"),
        Laboratorio("LAB03", "Laboratorio de IA", 35, "Pabellon C"),
        Laboratorio("LAB04", "Laboratorio de Hardware", 20, "Pabellon D"),
        Laboratorio("LAB05", "Laboratorio de Bases de Datos", 30, "Pabellon E")
    ]
    personas = [
        Persona("P001", "Delgado Varas", "Jeyson"),
        Persona("P002", "Aguero Zelada", "Teffo"),
        Persona("P003", "Cruz Rojales", "Yordin")
    ]
    for laboratorio in laboratorios:
        sistema.registrar_laboratorio(laboratorio)
    for persona in personas:
        sistema.registrar_persona(persona)
    sistema.autorizar_laboratorio("P001", "LAB01")
    sistema.autorizar_laboratorio("P001", "LAB02")
    sistema.autorizar_laboratorio("P001", "LAB03")
    sistema.autorizar_laboratorio("P002", "LAB02")
    sistema.autorizar_laboratorio("P002", "LAB03")
    sistema.autorizar_laboratorio("P002", "LAB05")
    sistema.autorizar_laboratorio("P003", "LAB01")
    sistema.autorizar_laboratorio("P003", "LAB05")
def demostracion_map(sistema: SistemaAcceso) -> None:
    print("\n" + "=" * 60)
    print("PARTE A - MAP")
    print("=" * 60)
    print("\n1. REGISTRO DE LABORATORIOS")
    print("-" * 60)
    try:
        laboratorio = Laboratorio(
            "LAB06",
            "Laboratorio de Sistemas",
            25,
            "Pabellon F"
        )
        sistema.registrar_laboratorio(laboratorio)
        print("Laboratorio LAB06 registrado correctamente.")
    except ValueError as e:
        print("Error:", e)

    print("\n2. INTENTO DE REGISTRAR UNA CLAVE DUPLICADA")
    print("-" * 60)
    try:
        laboratorio_duplicado = Laboratorio(
            "LAB06",
            "Otro Laboratorio",
            40,
            "Pabellon G"
        )
        sistema.registrar_laboratorio(laboratorio_duplicado)
    except ValueError as e:
        print("Error controlado:", e)

    print("\n3. BUSQUEDA DE UNA CLAVE EXISTENTE")
    print("-" * 60)
    laboratorio = sistema.buscar_laboratorio("LAB01")
    if laboratorio is not None:
        print("Laboratorio encontrado:")
        print(laboratorio)
    else:
        print("Laboratorio no encontrado.")

    print("\n4. BUSQUEDA DE UNA CLAVE INEXISTENTE")
    print("-" * 60)
    laboratorio = sistema.buscar_laboratorio("LAB99")
    if laboratorio is not None:
        print(laboratorio)
    else:
        print("LAB99 no existe en el Map.")

    print("\n5. MODIFICACION DEL VALOR ASOCIADO A UNA CLAVE")
    print("-" * 60)
    laboratorio = sistema.buscar_laboratorio("LAB01")
    if laboratorio is not None:
        print("ANTES:")
        print(laboratorio)
        laboratorio.nombre = "Laboratorio de Programacion Avanzada"
        laboratorio.capacidad = 35
        print("\nDESPUÉS:")
        print(laboratorio)

    print("\n6. LISTADO DE CLAVES DEL MAP")
    print("-" * 60)
    sistema.listar_codigos_laboratorios()

    print("\n7. LISTADO DE ASOCIACIONES")
    print("-" * 60)
    sistema.listar_laboratorios()

    print("\n8. ELIMINACION DE UNA CLAVE EXISTENTE")
    print("-" * 60)
    try:
        sistema.eliminar_laboratorio("LAB06")
        print("LAB06 eliminado correctamente.")
    except ValueError as e:
        print("Error:", e)

    print("\n9. INTENTO DE ELIMINAR UNA CLAVE INEXISTENTE")
    print("-" * 60)
    try:
        sistema.eliminar_laboratorio("LAB99")
    except ValueError as e:
        print("Error controlado:", e)

def demostracion_set(sistema: SistemaAcceso) -> None:
    print("\n" + "=" * 60)
    print("PARTE B - SET")
    print("=" * 60)
    persona_a = sistema.buscar_persona("P001")
    persona_b = sistema.buscar_persona("P002")

    if persona_a is None or persona_b is None:
        print("No se encontraron las personas necesarias.")
        return
    conjunto_a = persona_a.laboratorios_autorizados
    conjunto_b = persona_b.laboratorios_autorizados
    print("\nConjunto A - Autorizaciones de P001:")
    print(conjunto_a)

    print("\nConjunto B - Autorizaciones de P002:")
    print(conjunto_b)

    print("\n1. UNION A U B")
    print("-" * 60)

    union = conjunto_a | conjunto_b
    print(union)

    print("\n2. INTERSECCION A ∩ B")
    print("-" * 60)
    interseccion = conjunto_a & conjunto_b
    print(interseccion)

    print("\n3. DIFERENCIA A - B")
    print("-" * 60)
    diferencia_ab = conjunto_a - conjunto_b
    print(diferencia_ab)

    print("\n4. DIFERENCIA B - A")
    print("-" * 60)
    diferencia_ba = conjunto_b - conjunto_a
    print(diferencia_ba)

    print("\n5. PERTENENCIA DE UN ELEMENTO EXISTENTE")
    print("-" * 60)
    if persona_a.tiene_acceso("LAB01"):
        print("LAB01 pertenece al conjunto de autorizaciones de P001.")

    print("\n6. PERTENENCIA DE UN ELEMENTO INEXISTENTE")
    print("-" * 60)
    if not persona_a.tiene_acceso("LAB05"):
        print("LAB05 no pertenece al conjunto de autorizaciones de P001.")

    print("\n7. INTENTO DE AGREGAR UN DUPLICADO")
    print("-" * 60)
    print("ANTES:")
    print(persona_a.laboratorios_autorizados)
    persona_a.agregar_laboratorio("LAB01")
    print("DESPUES:")
    print(persona_a.laboratorios_autorizados)
    print("El elemento no se duplica porque el Set trabaja con elementos unicos.")

    print("\n8. ELIMINACION DE UN ELEMENTO")
    print("-" * 60)
    print("ANTES:")
    print(persona_a.laboratorios_autorizados)
    persona_a.retirar_laboratorio("LAB03")
    print("DESPUES:")
    print(persona_a.laboratorios_autorizados)

    print("\n9. INTERPRETACION DE LA INTERSECCION")
    print("-" * 60)
    print(
        "Los elementos de la interseccion representan los laboratorios "
        "a los que ambas personas tienen autorizacion."
    )


def demostracion_frecuencia() -> None:
    print("\n" + "=" * 60)
    print("PARTE C - FRECUENCIA")
    print("=" * 60)
    datos = [
        "LAB01",
        "LAB02",
        "LAB01",
        "LAB03",
        "LAB02",
        "LAB01",
        "LAB05"
    ]
    frecuencia: dict[str, int] = {}
    print("\nDatos:")
    print(datos)
    for elemento in datos:
        if elemento in frecuencia:
            valor_actual = frecuencia[elemento]
            frecuencia[elemento] = valor_actual + 1
        else:
            frecuencia[elemento] = 1
    print("\nFrecuencia de cada laboratorio:")
    for clave, valor in frecuencia.items():
        print(f"{clave} -> {valor}")
def leer_entero(mensaje: str) -> int:
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: debe ingresar un numero entero.")

def registrar_laboratorio_menu(sistema: SistemaAcceso) -> None:
    print("\n--- REGISTRAR LABORATORIO ---")
    codigo = input("Codigo: ").strip()
    nombre = input("Nombre: ").strip()
    capacidad = leer_entero("Capacidad: ")
    pabellon = input("Pabellon: ").strip()
    if not codigo or not nombre or not pabellon:
        print("Error: los datos de texto no pueden estar vacios.")
        return
    if capacidad <= 0:
        print("Error: la capacidad debe ser mayor que cero.")
        return
    try:
        laboratorio = Laboratorio(
            codigo,
            nombre,
            capacidad,
            pabellon
        )
        sistema.registrar_laboratorio(laboratorio)
        print("Laboratorio registrado correctamente.")
    except ValueError as e:
        print("Error:", e)

def buscar_laboratorio_menu(sistema: SistemaAcceso) -> None:
    print("\n--- BUSCAR LABORATORIO ---")
    codigo = input("Ingrese codigo: ").strip()
    laboratorio = sistema.buscar_laboratorio(codigo)
    if laboratorio is None:
        print("El laboratorio no existe.")
    else:
        print(laboratorio)

def eliminar_laboratorio_menu(sistema: SistemaAcceso) -> None:
    print("\n--- ELIMINAR LABORATORIO ---")
    codigo = input("Ingrese código: ").strip()
    try:
        sistema.eliminar_laboratorio(codigo)
        print("Laboratorio eliminado correctamente.")
    except ValueError as e:
        print("Error:", e)

def registrar_persona_menu(sistema: SistemaAcceso) -> None:
    print("\n--- REGISTRAR PERSONA ---")
    codigo = input("Código: ").strip()
    apellidos = input("Apellidos: ").strip()
    nombres = input("Nombres: ").strip()
    if not codigo or not apellidos or not nombres:
        print("Error: todos los campos son obligatorios.")
        return
    try:
        persona = Persona(
            codigo,
            apellidos,
            nombres
        )
        sistema.registrar_persona(persona)
        print("Persona registrada correctamente.")
    except ValueError as e:
        print("Error:", e)

def buscar_persona_menu(sistema: SistemaAcceso) -> None:
    print("\n--- BUSCAR PERSONA ---")
    codigo = input("Ingrese codigo: ").strip()
    persona = sistema.buscar_persona(codigo)
    if persona is None:
        print("La persona no existe.")
    else:
        print(persona)

def eliminar_persona_menu(sistema: SistemaAcceso) -> None:
    print("\n--- ELIMINAR PERSONA ---")
    codigo = input("Ingrese codigo: ").strip()
    try:
        sistema.eliminar_persona(codigo)
        print("Persona eliminada correctamente.")
    except ValueError as e:
        print("Error:", e)

def autorizar_laboratorio_menu(sistema: SistemaAcceso) -> None:
    print("\n--- AUTORIZAR LABORATORIO ---")
    codigo_persona = input("Codigo de persona: ").strip()
    codigo_laboratorio = input("Codigo de laboratorio: ").strip()
    try:
        sistema.autorizar_laboratorio(
            codigo_persona,
            codigo_laboratorio
        )
        print("Laboratorio autorizado correctamente.")
    except ValueError as e:
        print("Error:", e)


def revocar_autorizacion_menu(sistema: SistemaAcceso) -> None:
    print("\n--- REVOCAR AUTORIZACIÓN ---")
    codigo_persona = input("Codigo de persona: ").strip()
    codigo_laboratorio = input("Codigo de laboratorio: ").strip()
    try:
        sistema.revocar_autorizacion(
            codigo_persona,
            codigo_laboratorio
        )
        print("Autorizacion revocada correctamente.")
    except ValueError as e:
        print("Error:", e)

def consultar_acceso_menu(sistema: SistemaAcceso) -> None:
    print("\n--- CONSULTAR ACCESO ---")
    codigo_persona = input("Codigo de persona: ").strip()
    codigo_laboratorio = input("Codigo de laboratorio: ").strip()
    try:
        if sistema.puede_acceder(
            codigo_persona,
            codigo_laboratorio
        ):
            print("ACCESO PERMITIDO.")
        else:
            print("ACCESO DENEGADO.")
    except ValueError as e:
        print("Error:", e)

def comparar_autorizaciones_menu(sistema: SistemaAcceso) -> None:
    print("\n--- COMPARAR AUTORIZACIONES ---")
    codigo_persona_a = input("Codigo de persona A: ").strip()
    codigo_persona_b = input("Codigo de persona B: ").strip()
    persona_a = sistema.buscar_persona(codigo_persona_a)
    persona_b = sistema.buscar_persona(codigo_persona_b)
    if persona_a is None or persona_b is None:
        print("Error: una o ambas personas no existen.")
        return
    conjunto_a = persona_a.laboratorios_autorizados
    conjunto_b = persona_b.laboratorios_autorizados
    print("\nAutorizaciones de A:")
    print(conjunto_a)

    print("\nAutorizaciones de B:")
    print(conjunto_b)

    print("\nUnion A U B:")
    print(conjunto_a | conjunto_b)

    print("\nInterseccion A ∩ B:")
    print(conjunto_a & conjunto_b)

    print("\nDiferencia A - B:")
    print(conjunto_a - conjunto_b)

    print("\nDiferencia B - A:")
    print(conjunto_b - conjunto_a)

def mostrar_menu() -> None:
    print("\n" + "=" * 60)
    print("SISTEMA DE CONTROL DE ACCESO A LABORATORIOS")
    print("=" * 60)

    print("0. Salir")
    print("1. Registrar laboratorio")
    print("2. Buscar laboratorio")
    print("3. Eliminar laboratorio")
    print("4. Listar laboratorios")
    print("5. Registrar persona")
    print("6. Buscar persona")
    print("7. Eliminar persona")
    print("8. Listar personas")
    print("9. Autorizar laboratorio")
    print("10. Revocar autorización")
    print("11. Consultar acceso")
    print("12. Comparar autorizaciones")

def main() -> None:
    sistema = SistemaAcceso()
    registrar_datos_iniciales(sistema)
    while True:
        mostrar_menu()
        opcion = leer_entero("\nSeleccione una opcion: ")
        if opcion == 0:
            print("\nPrograma finalizado.")
            break
        elif opcion == 1:
            registrar_laboratorio_menu(sistema)
        elif opcion == 2:
            buscar_laboratorio_menu(sistema)
        elif opcion == 3:
            eliminar_laboratorio_menu(sistema)
        elif opcion == 4:
            print("\n--- LISTA DE LABORATORIOS ---")
            sistema.listar_laboratorios()
        elif opcion == 5:
            registrar_persona_menu(sistema)
        elif opcion == 6:
            buscar_persona_menu(sistema)
        elif opcion == 7:
            eliminar_persona_menu(sistema)
        elif opcion == 8:
            print("\n--- LISTA DE PERSONAS ---")
            sistema.listar_personas()
        elif opcion == 9:
            autorizar_laboratorio_menu(sistema)
        elif opcion == 10:
            revocar_autorizacion_menu(sistema)
        elif opcion == 11:
            consultar_acceso_menu(sistema)
        elif opcion == 12:
            comparar_autorizaciones_menu(sistema)
        else:
            print("Error: opcion no valida.")
if __name__ == "__main__":
    main()