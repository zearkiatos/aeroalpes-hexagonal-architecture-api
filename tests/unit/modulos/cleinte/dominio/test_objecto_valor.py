import pytest
from faker import Faker
from uuid import uuid4
from aeroalpes.modulos.cliente.dominio.objetos_valor import MetodosPago, TipoDeMetodoDePago
from aeroalpes.utils.encryption import get_salt, generate_key_from_phrase, encrypt_data
from aeroalpes.config.config import Config

config = Config()

def test_entidad_cliente_metodo_de_pago_objeto_valor():
    id = uuid4()
    salt = get_salt()
    numero = Faker().credit_card_number()
    cvv = Faker().credit_card_security_code()
    key = generate_key_from_phrase(config.PHRASE_KEY, salt)
    numero_encrypted = encrypt_data(numero, key)
    cvv_encrypted = encrypt_data(cvv, key)
    nombre = Faker().word()
    fecha_expiracion = Faker().date_time_this_decade()
    metodo_pago = MetodosPago(
        id=id,
        tipo=TipoDeMetodoDePago.TARJETA_DE_CREDITO,
        numero=numero_encrypted,
        cvv=cvv_encrypted,
        salt=salt,
        nombre=nombre,
        fecha_expiracion=fecha_expiracion
    )

    assert metodo_pago is not None
    assert metodo_pago.id == id
    assert metodo_pago.tipo == TipoDeMetodoDePago.TARJETA_DE_CREDITO
    assert metodo_pago.numero == numero_encrypted
    assert metodo_pago.cvv == cvv_encrypted
    assert metodo_pago.salt == salt
    assert metodo_pago.nombre == nombre
    assert metodo_pago.fecha_expiracion == fecha_expiracion
