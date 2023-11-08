class ValidadorError(Exception):
    pass


class NoCumpleLongitudMinimaError(ValidadorError):
    pass


class NoTieneLetraMayusculaError(ValidadorError):
    pass


class NoTieneLetraMinusculaError(ValidadorError):
    pass


class NoTieneNumeroError(ValidadorError):
    pass


class NoTieneCaracterEspecialError(ValidadorError):
    pass


class NoTienePalabraSecretaError(ValidadorError):
    pass