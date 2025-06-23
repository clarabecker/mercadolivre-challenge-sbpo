import sys
from solution import Solution
from harmony_search import reparar_harmonia

def avaliar_harmonia(harmony_vector, instance):
    n_pedidos = len(instance.orders)

    harmony_reparada = reparar_harmonia(harmony_vector, instance)

    sol = Solution(instance)
    sol.x = harmony_reparada[:n_pedidos]
    sol.y = harmony_reparada[n_pedidos:]

    if not sol.verificacao_solucao():
        sys.exit("Sem solução viável após reparação múltipla")

    return sol.calculo_ofv()


