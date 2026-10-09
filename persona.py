class Persona:
    def __init__(self, codigo: str, apellidos: str, nombres: str) -> None:
        self.__codigo = codigo
        self.__apellidos = apellidos
        self.__nombres = nombres
        self.__laboratorios_autorizados: set[str] = set()

    @property
    def codigo(self) -> str:
        return self.__codigo

    @codigo.setter
    def codigo(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("El código no puede estar vacío.")
        self.__codigo = valor

    @property
    def apellidos(self) -> str:
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, valor: str) -> None:
        self.__apellidos = valor

    @property
    def nombres(self) -> str:
        return self.__nombres

    @nombres.setter
    def nombres(self, valor: str) -> None:
        self.__nombres = valor

    @property
    def laboratorios_autorizados(self) -> set[str]:
        return self.__laboratorios_autorizados

    def agregar_laboratorio(self, codigo_lab: str) -> None:
        # Validación Sección 10: Clave o elemento vacío
        if not codigo_lab or not codigo_lab.strip():
            raise ValueError("El código de laboratorio no puede estar vacío.")

        # Validación Sección 10: Intento de agregar un elemento duplicado al Set
        if codigo_lab in self.__laboratorios_autorizados:
            raise ValueError(f"El laboratorio '{codigo_lab}' ya se encuentra autorizado para {self.__codigo}.")

        self.__laboratorios_autorizados.add(codigo_lab)

    def retirar_laboratorio(self, codigo_lab: str) -> None:
        if not codigo_lab or not codigo_lab.strip():
            raise ValueError("El código de laboratorio no puede estar vacío.")

        # Validación Sección 10: Eliminación de un elemento que no pertenece al Set
        if codigo_lab in self.__laboratorios_autorizados:
            self.__laboratorios_autorizados.remove(codigo_lab)
        else:
            raise ValueError(f"Error: El laboratorio '{codigo_lab}' no pertenece a los accesos autorizados de {self.__codigo}.")

    def tiene_acceso(self, codigo_lab: str) -> bool:
        if not codigo_lab or not codigo_lab.strip():
            return False
        return codigo_lab in self.__laboratorios_autorizados

    def __str__(self) -> str:
        labs = ", ".join(sorted(self.__laboratorios_autorizados)) if self.__laboratorios_autorizados else "Ninguno"
        return f"Persona[{self.__codigo}] {self.__apellidos}, {self.__nombres} | Autorizaciones: {{ {labs} }}"