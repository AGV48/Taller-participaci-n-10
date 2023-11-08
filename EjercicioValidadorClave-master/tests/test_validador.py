import random
import pytest
from validadorclave.modelo.errores import NoTieneLetraMayusculaError, NoTieneLetraMinusculaError, NoTieneNumeroError, \
    NoTieneCaracterEspecialError, NoCumpleLongitudMinimaError, NoTienePalabraSecretaError
from validadorclave.modelo.validador import Validador, ReglaValidacionGanimedes, ReglaValidacionCalisto




@pytest.fixture
def regla():
    reglas = (ReglaValidacionGanimedes(), ReglaValidacionCalisto())
    return reglas[random.randint(0, 1)]


@pytest.fixture
def regla_ganimedes():
    return ReglaValidacionGanimedes()


@pytest.fixture
def regla_calisto():
    return ReglaValidacionCalisto()


@pytest.fixture
def validador_ganimedes():
    return Validador(ReglaValidacionGanimedes())


@pytest.fixture
def validador_calisto():
    return Validador(ReglaValidacionCalisto())


@pytest.mark.parametrize("clave, esperado", [
    ("ASDDS234_-@", True),
    ("Ae5_", True),
    ("4_ader56p", False)
])
def test_regla_identifica_que_clave_contiene_mayuscula(regla, clave, esperado):
    assert regla._contiene_mayuscula(clave) == esperado


@pytest.mark.parametrize("clave, esperado", [
    ("ASDDS234_-@", False),
    ("Ae5_", True),
    ("4_ader56p", True)
])
def test_regla_identifica_que_clave_contiene_minuscula(regla, clave, esperado):
    assert regla._contiene_minuscula(clave) == esperado


@pytest.mark.parametrize("clave, esperado", [
    ("ASDDS234_-@", True),
    ("Aez_", False),
    ("4_ader56p", True)
])
def test_regla_identifica_que_clave_contiene_numero(regla, clave, esperado):
    assert regla._contiene_numero(clave) == esperado


@pytest.mark.parametrize("clave, esperado", [
    ("ASDDS234_-@", True),
    ("Aez_", False),
    ("4_ader56", False)
])
def test_regla_valida_longitud_clave(regla_ganimedes, clave, esperado):
    assert regla_ganimedes._validar_longitud(clave) == esperado


@pytest.mark.parametrize("clave, esperado", [
    ("CaliSto123", True),
    ("as2caListO", True),
    ("calisto", False),
    ("12ascalisto", False),
    ("12CALISTO_", False),
    ("calistoCaLiSto123", True)
])
def test_regla_calisto_verifica_palabra(regla_calisto, clave, esperado):
    assert regla_calisto.contiene_calisto(clave) == esperado


@pytest.mark.parametrize("clave, esperado", [
    ("_ASd3", True),
    ("tren0@", True),
    ("4-adEr56p", False),
    ("4$adEr56p", True),
    ("4-adE%56p", True),
    ("4-adE#56p", True),
])
def test_regla_ganimedes_verifica_caracter_especial(regla_ganimedes, clave, esperado):
    assert regla_ganimedes.contiene_caracter_especial(clave) == esperado


def test_clave_invalida_sin_longitud_genera_error_con_ganimedes(validador_ganimedes):
    clave = "asd3_-"
    with pytest.raises(NoCumpleLongitudMinimaError):
        validador_ganimedes.es_valida(clave)


def test_clave_invalida_sin_mayuscula_genera_error_con_ganimedes(validador_ganimedes):
    clave = "asdds234_-@"
    with pytest.raises(NoTieneLetraMayusculaError):
        validador_ganimedes.es_valida(clave)


def test_clave_invalida_sin_minuscula_genera_error_con_ganimedes(validador_ganimedes):
    clave = "ASDDS234_-@"
    with pytest.raises(NoTieneLetraMinusculaError):
        validador_ganimedes.es_valida(clave)


def test_clave_invalida_sin_numero_genera_error_con_ganimedes(validador_ganimedes):
    clave = "ASDDSassd_-@"
    with pytest.raises(NoTieneNumeroError):
        validador_ganimedes.es_valida(clave)


def test_clave_invalida_sin_caracter_especial_genera_error_con_ganimedes(validador_ganimedes):
    clave = "ASDDSassd-3"
    with pytest.raises(NoTieneCaracterEspecialError):
        validador_ganimedes.es_valida(clave)


@pytest.mark.parametrize("clave", [
    "ASdDS234_-@",
    "Ae5_tren0",
    "4_adEr56p"
])
def test_es_clave_valida_con_ganimedes(clave):
    validador = Validador(ReglaValidacionGanimedes())
    assert validador.es_valida(clave) is True


def test_clave_invalida_sin_longitud_genera_error_con_calisto(validador_calisto):
    clave = "asd3_-"
    with pytest.raises(NoCumpleLongitudMinimaError):
        validador_calisto.es_valida(clave)


def test_clave_invalida_sin_numero_genera_error_con_calisto(validador_calisto):
    clave = "ASDDSassd_-@"
    with pytest.raises(NoTieneNumeroError):
        validador_calisto.es_valida(clave)


@pytest.mark.parametrize("clave", [
    "1calisto",
    "caListo23",
    "2CALISTO"
])
def test_clave_invalida_sin_palabra_secreta_genera_error_con_calisto(validador_calisto, clave):
    with pytest.raises(NoTienePalabraSecretaError):
        validador_calisto.es_valida(clave)


@pytest.mark.parametrize("clave", [
    "CaLisTo95",
    "_3caLISto",
    "a3CALIStO_"
])
def test_es_clave_valida_con_calisto(clave):
    validador = Validador(ReglaValidacionCalisto())
    assert validador.es_valida(clave) is True
