from pypro.modulos.models import Modulo, Aula
from typing import List
from django.db.models import Prefetch

def lista_modulos_ordenados() -> List[Modulo]:
    """
    Lista modulos ordenados por titulos

    :return:
    
    """
    return list(Modulo.objects.order_by('order').all())

def encontrar_modulo(slug: str) -> Modulo:
    return Modulo.objects.get(slug=slug)

def listar_aulas_de_modulo_ordenadas(modulo: Modulo):
    return list(modulo.aula_set.order_by('order').all())

def encontrar_aula(slug):
    return Aula.objects.select_related('modulo').get(slug=slug) # Só funciona quando tentamos acessar N para 1

def listar_modulos_com_aulas():
    aulas_ordenadas = Aula.objects.order_by('order')
    return Modulo.objects.order_by('order').prefetch_related(Prefetch('aula_set', queryset=aulas_ordenadas, to_attr='aulas')).all() # Só funciona para acessar 1 para N