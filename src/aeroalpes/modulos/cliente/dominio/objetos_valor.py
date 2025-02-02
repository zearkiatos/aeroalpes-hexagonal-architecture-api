"""Objetos valor del dominio de cliente

En este archivo usted encontrará los objetos valor del dominio de cliente

"""

from aeroalpes.seedwork.dominio.objetos_valor import ObjetoValor, Ciudad
from dataclasses import dataclass
from enum import Enum
from uuid import UUID
import datetime

@dataclass(frozen=True)
class Nombre(ObjetoValor):
    nombres: str
    apellidos: str

@dataclass(frozen=True)
class Email(ObjetoValor):
    address: str
    dominio: str
    es_empresarial: bool

@dataclass(frozen=True)
class Cedula(ObjetoValor):
    numero: int
    ciudad: Ciudad

@dataclass(frozen=True)
class Rut(ObjetoValor):
    numero: int
    ciudad: Ciudad

@dataclass(frozen=True)
class MetodosPago(ObjetoValor):
    id: UUID
    tipo: 'TipoDeMetodoDePago'
    numero: str
    cvv: str
    salt: str
    nombre: str
    fecha_expiracion: datetime.date


class TipoDeMetodoDePago(Enum):
    TARJETA_DE_CREDITO = "Tarjeta de crédito"
    TARJETA_DE_DEBITO = "Tarjeta de débito"
    TRANSFERENCIA_BANCARIA = "Transferencia bancaria"
    PAYPAL = "PayPal"
    GOOGLE_PAY = "Google Pay"
    APPLE_PAY = "Apple Pay"
    MERCADO_PAGO = "Mercado Pago"
    BITCOIN = "Bitcoin"

