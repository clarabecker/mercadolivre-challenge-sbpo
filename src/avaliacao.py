from solution import Solution


# Em avaliacao.py

def avaliar_harmonia(harmony_vector, instance):
    # ... (código anterior para definir x e y) ...
    x = [int(val) for val in harmony_vector[:len(instance.orders)]]
    y = [int(val) for val in harmony_vector[len(instance.orders):]]

    sol = Solution(instance)
    sol.x = x
    sol.y = y

    viavel = sol.solucao_viavel()
    armazenamento_ok = sol.aisles_storage()

    if viavel and armazenamento_ok:
        ofv = sol.calculate_ofv()
        return ofv
    else:
        return -float('inf')
