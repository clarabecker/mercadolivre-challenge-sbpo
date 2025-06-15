from solution import Solution

def avaliar_harmonia(harmony_vector, instance):

    sol = Solution(instance)
    sol.x = [int(val) for val in harmony_vector[:len(instance.orders)]]

    sol.y = [0] * len(instance.aisles)
    for o, is_selected in enumerate(sol.x):
        if is_selected:
            for aisle_index in instance.order_aisles[o]:
                sol.y[aisle_index] = 1

    if not sol.verificacao_solucao():
        return -float('inf')

    return sol.calculo_ofv()