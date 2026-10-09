from laboratorio import Laboratorio
from persona import Persona

class SistemaAcceso:
    def __init__(self):
        self.__personas : dict[str, Persona] = {}
        self.__laboratorios : dict[str, Laboratorio] = {}


    #OPERACIONES DE LABORATORIO

    def registrar_laboratorio(self, laboratorio : Laboratorio) -> None:
        if laboratorio is None:
            raise ValueError("El laboratorio no puede ser nulo")
            
        # Validación Sección 10: Clave vacía o inválida
        if not laboratorio.codigo or not laboratorio.codigo.strip():
            raise ValueError("El código de laboratorio no puede estar vacío o contener solo espacios")
        
        
        if self.existe_laboratorio(laboratorio.codigo):
            raise ValueError("El codigo de laboratorio ingresado ya existe")

        self.__laboratorios[laboratorio.codigo] = laboratorio

    def buscar_laboratorio(self, codigo : str) -> Laboratorio | None:
        if not codigo or not codigo.strip():
            return None
        
        for i in self.__laboratorios.keys():
            if i == codigo:
                return self.__laboratorios[i]

        return None

    def eliminar_laboratorio(self, codigo : str) -> None:
        # Validación Sección 10: Clave vacía o inexistente
        if not codigo or not codigo.strip():
            raise ValueError("El código de laboratorio a eliminar no puede estar vacío")

        if not self.existe_laboratorio(codigo):
            raise ValueError("El codigo de laboratorio no existe")

        self.__laboratorios.pop(codigo)

    def existe_laboratorio(self, codigo: str) -> bool:
            for i in self.__laboratorios.keys():
                if codigo == i:
                    return True
    
            return False


    #OPERACIONES DE PERSONAS

    def registrar_persona(self, persona : Persona) -> None:
        if persona is None:
            raise ValueError("La persona no puede ser nula")

        # Validación Sección 10: Clave vacía o inválida
        if not persona.codigo or not persona.codigo.strip():
            raise ValueError("El código de persona no puede estar vacío o contener solo espacios")

        if self.existe_persona(persona.codigo):
            raise ValueError("Ya existe el codigo de la persona a registrar")

        self.__personas[persona.codigo] = persona

    def buscar_persona(self, codigo: str) -> Persona | None:
        # Validación Sección 10: Clave vacía
        if not codigo or not codigo.strip():
            return None

        for i in self.__personas.keys():
            if i == codigo:
                return self.__personas[i]
        return None

    def eliminar_persona(self, codigo: str) -> None:
        # Validación Sección 10: Clave vacía o inexistente
        if not codigo or not codigo.strip():
            raise ValueError("El código de persona a eliminar no puede estar vacío")

        if not self.existe_persona(codigo):
            raise ValueError("El codigo de persona no existe")

        self.__personas.pop(codigo)

    def existe_persona(self, codigo: str) -> bool:
        if not codigo or not codigo.strip():
            return False

        for i in self.__personas.keys():
            if i == codigo:
                return True

        return False


    #OPERACIONES CONJUNTAS

    def autorizar_laboratorio(self, codigoPersona: str, codigoLaboratorio: str) -> None:
        # Validación Sección 10: Entradas vacías
        if not codigoPersona or not codigoPersona.strip() or not codigoLaboratorio or not codigoLaboratorio.strip():
            raise ValueError("Los códigos no pueden estar vacíos")

        if not self.existe_persona(codigoPersona) or not self.existe_laboratorio(codigoLaboratorio):
            raise ValueError("Los codigos enviado no estan registrados")

        self.buscar_persona(codigoPersona).agregar_laboratorio(codigoLaboratorio)

    def revocar_autorizacion(self, codigoPersona: str, codigoLaboratorio: str) -> None:
        # Validación Sección 10: Entradas vacías
        if not codigoPersona or not codigoPersona.strip() or not codigoLaboratorio or not codigoLaboratorio.strip():
            raise ValueError("Los códigos no pueden estar vacíos")

        if not self.existe_persona(codigoPersona) or not self.existe_laboratorio(codigoLaboratorio):
            raise ValueError("Los codigos enviado no estan registrados")

        self.buscar_persona(codigoPersona).retirar_laboratorio(codigoLaboratorio)
    def puede_acceder(self, codigoPersona : str, codigoLaboratorio : str) -> bool:
        if not self.existe_persona(codigoPersona) or not self.existe_laboratorio(codigoLaboratorio):
            raise ValueError("Los codigos enviado no estan registrados")

        return self.buscar_persona(codigoPersona).tiene_acceso(codigoLaboratorio)



    #LISTADOS

    def listar_laboratorios(self) -> None:
        for i in self.__laboratorios.values():
            print(i)

    def listar_personas(self) -> None:
        for i in self.__personas.values():
            print(i)
    def listar_codigos_laboratorios(self) -> None:
        for codigo in self.__laboratorios.keys():
            print(codigo)