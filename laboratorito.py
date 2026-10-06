class Laboratorio:
    def __init__(self, codigo: str, nombre: str, capacidad: int, pabellon: str) -> None:
        self.__codigo = codigo
        self.__nombre = nombre
        self.__capacidad = capacidad
        self.__pabellon = pabellon

    @property
    def codigo(self) -> str:
        return self.__codigo

    @codigo.setter
    def codigo(self, valor: str) -> None:
        self.__codigo = valor

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        self.__nombre = valor

    @property
    def capacidad(self) -> int:
        return self.__capacidad

    @capacidad.setter
    def capacidad(self, valor: int) -> None:
        self.__capacidad = valor

    @property
    def pabellon(self) -> str:
        return self.__pabellon

    @pabellon.setter
    def pabellon(self, valor: str) -> None:
        self.__pabellon = valor

    def __str__(self) -> str:
        return f"Laboratorio[{self.__codigo}] {self.__nombre} | Capacidad: {self.__capacidad} | Pabellón: {self.__pabellon}"