from pypro.modulos.models import Modulo
from typing import List

def lista_modulos_ordenados() -> List[Modulo]:
    """
    Lista modulos ordenados por titulos

    :return:
    
    """
    return list(Modulo.objects.order_by('order').all())