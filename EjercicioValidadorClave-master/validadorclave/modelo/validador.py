from modelo.errores import *
from abc import ABC

class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada):
        self._longitud_esperada = longitud_esperada
    
    @ABC
    def es_valida(self, clave: str) -> bool:
        self.clave = clave

    def _validar_longitud(self, clave):
        if len(clave) <= self._longitud_esperada:
            raise NoCumpleLongitudMinimaError("La clave no cumple con la longitud esperada")

    def _contiene_mayuscula(self, clave):
        if not any(c.isupper() for c in clave):
            raise NoTieneLetraMayusculaError("La clave debe contener al menos una letra mayúscula")

    def _contiene_minuscula(self, clave):
        if not any(c.islower() for c in clave):
            raise NoTieneLetraMinusculaError("La clave debe contener al menos una letra minúscula")

    def _contiene_numero(self, clave):
        if not any(c.isdigit() for c in clave):
            raise NoTieneNumeroError("La clave debe contener al menos un número")


class ReglaValidacionGanimedes(ReglaValidacion):
    def _contiene_caracter_especial(self, clave):
        if not any(c in "@_#$%" for c in clave):
            raise NoTieneCaracterEspecialError("La clave debe contener al menos un caracter especial")

    def es_valida(self, clave):
        self._validar_longitud(clave)
        self._contiene_mayuscula(clave)
        self._contiene_minuscula(clave)
        self._contiene_numero(clave)
        self._contiene_caracter_especial(clave)
        return True


class ReglaValidacionCalisto(ReglaValidacion):
    def _contiene_calisto(self, clave):
        if str.find(clave.islower() or clave.isupper()):
            raise ValidadorError("La clave debe contener la palabra 'calisto' en algún formato")
        else:
            return True
            

    def es_valida(self, clave):
        self._validar_longitud(clave)
        self._contiene_numero(clave)
        self._contiene_calisto(clave)
        return True
