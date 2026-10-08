from laboratorio import Laboratorio
from persona import Persona
from sistema_acceso import SistemaAcceso


def probar_map():
    print("\n========== PRUEBAS MAP ==========")

    # 1. Map vacío
    sistema = SistemaAcceso()
    print("1. Map vacío:", sistema.buscar_laboratorio("LAB01") is None)

    # 2. Una entrada
    lab1 = Laboratorio("LAB01", "Laboratorio de Programación", 30, "A")
    sistema.registrar_laboratorio(lab1)
    print("2. Una entrada:", sistema.existe_laboratorio("LAB01"))

    # 3. Varias entradas
    sistema.registrar_laboratorio(
        Laboratorio("LAB02", "Laboratorio de Redes", 25, "B")
    )
    sistema.registrar_laboratorio(
        Laboratorio("LAB03", "Laboratorio de IA", 20, "C")
    )
    print(
        "3. Varias entradas:",
        sistema.existe_laboratorio("LAB01")
        and sistema.existe_laboratorio("LAB02")
        and sistema.existe_laboratorio("LAB03")
    )

    # 4. Clave nueva
    sistema.registrar_laboratorio(
        Laboratorio("LAB04", "Laboratorio de Hardware", 20, "D")
    )
    print("4. Clave nueva:", sistema.existe_laboratorio("LAB04"))

    # 5. Clave existente
    print("5. Clave existente:", sistema.existe_laboratorio("LAB01"))

    # 6. Consulta existente
    print("6. Consulta existente:", sistema.buscar_laboratorio("LAB01") is not None)

    # 7. Consulta inexistente
    print("7. Consulta inexistente:", sistema.buscar_laboratorio("LAB99") is None)

    # 8. Eliminar existente
    sistema.eliminar_laboratorio("LAB04")
    print("8. Eliminar existente:", not sistema.existe_laboratorio("LAB04"))

    # 9. Eliminar inexistente
    try:
        sistema.eliminar_laboratorio("LAB99")
        print("9. Eliminar inexistente: ERROR")
    except ValueError:
        print("9. Eliminar inexistente: CORRECTO")

    # 10. Clave duplicada
    try:
        sistema.registrar_laboratorio(
            Laboratorio("LAB01", "Laboratorio duplicado", 20, "A")
        )
        print("10. Clave duplicada: ERROR")
    except ValueError:
        print("10. Clave duplicada: CORRECTO")


def probar_set():
    print("\n========== PRUEBAS SET ==========")

    sistema = SistemaAcceso()

    sistema.registrar_laboratorio(
        Laboratorio("LAB01", "Programación", 30, "A")
    )
    sistema.registrar_laboratorio(
        Laboratorio("LAB02", "Redes", 25, "B")
    )
    sistema.registrar_laboratorio(
        Laboratorio("LAB03", "IA", 20, "C")
    )
    sistema.registrar_laboratorio(
        Laboratorio("LAB05", "Bases de Datos", 30, "D")
    )

    persona = Persona("PER01", "Perez", "Juan")
    sistema.registrar_persona(persona)

    # 1. Set vacío
    print(
        "1. Set vacío:",
        len(persona.laboratorios_autorizados) == 0
    )

    # 2. Agregar primer elemento
    sistema.autorizar_laboratorio("PER01", "LAB01")
    print(
        "2. Agregar primer elemento:",
        "LAB01" in persona.laboratorios_autorizados
    )

    # 3. Agregar varios
    sistema.autorizar_laboratorio("PER01", "LAB02")
    sistema.autorizar_laboratorio("PER01", "LAB03")

    print(
        "3. Agregar varios:",
        persona.laboratorios_autorizados == {
            "LAB01", "LAB02", "LAB03"
        }
    )

    # 4. Agregar duplicado
    sistema.autorizar_laboratorio("PER01", "LAB01")
    print(
        "4. Agregar duplicado:",
        len(persona.laboratorios_autorizados) == 3
    )

    # 5. Pertenencia
    print(
        "5. Pertenencia:",
        "LAB01" in persona.laboratorios_autorizados
    )

    # 6. Ausencia
    print(
        "6. Ausencia:",
        "LAB99" not in persona.laboratorios_autorizados
    )

    # 7. Eliminar
    sistema.revocar_autorizacion("PER01", "LAB01")
    print(
        "7. Eliminar:",
        "LAB01" not in persona.laboratorios_autorizados
    )

    # 8. Unión
    A = {"LAB01", "LAB02", "LAB03"}
    B = {"LAB02", "LAB03", "LAB05"}

    print(
        "8. Unión:",
        A | B == {"LAB01", "LAB02", "LAB03", "LAB05"}
    )

    # 9. Intersección
    print(
        "9. Intersección:",
        A & B == {"LAB02", "LAB03"}
    )

    # 10. Diferencias
    print(
        "10. Diferencias:",
        A - B == {"LAB01"} and B - A == {"LAB05"}
    )

    # 11. Eliminar elemento ausente
    try:
        persona.retirar_laboratorio("LAB99")
        print("11. Eliminar ausente: ERROR")
    except ValueError:
        print("11. Eliminar ausente: CORRECTO")


def main():
    probar_map()
    probar_set()


if __name__ == "__main__":
    main()