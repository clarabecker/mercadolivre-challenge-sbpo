import sys
from solution import Solution
from harmony_search import reparar_harmonia  # importa a função


def avaliar_harmonia(harmony_vector, instance):
    n_pedidos = len(instance.orders)
    n_corredores = len(instance.aisles)

    # Chama reparação do vetor harmony
    harmony_reparada = reparar_harmonia(harmony_vector, instance)

    sol = Solution(instance)
    sol.x = [int(val) for val in harmony_reparada[:n_pedidos]]
    sol.y = [int(val) for val in harmony_reparada[n_pedidos:]]

    if not sol.verificacao_solucao():
        print("Não foi possível reparar a solução.")
        sys.exit("Encerrando devido a solução inviável após tentativa de reparo.")

    return sol.calculo_ofv()


