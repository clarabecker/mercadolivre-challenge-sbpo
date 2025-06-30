from .solution import Solution

def reparar_harmonia(harmony, instance):
    n_pedidos = len(instance.orders)

    harmony = [int(val) for val in harmony]
    x = harmony[:n_pedidos]

    sol = Solution(instance)
    sol.x = x.copy()
    sol.atualizar_corredores()

    total_pedidos = sum(sum(instance.orders[i].values()) for i in range(n_pedidos) if sol.x[i] == 1)

    while not (sol.lb <= total_pedidos <= sol.ub and sol.armazenamento_suficiente()):
        pedidos_sol = [i for i in range(n_pedidos) if sol.x[i] == 1]

        if not pedidos_sol:
            break

        # Remover pedido que usa mais corredores distintos
        i_remove = max(pedidos_sol, key=lambda i: sum(1 for q in instance.orders[i].values() if q > 0))

        sol.x[i_remove] = 0
        sol.atualizar_corredores()
        total_pedidos -= sum(instance.orders[i_remove].values())

    pedidos_candidatos = [i for i in range(n_pedidos) if sol.x[i] == 0]

    pedidos_candidatos = sorted(pedidos_candidatos, key=lambda i: sum(instance.orders[i].values()))

    for i in pedidos_candidatos:
        unidades = sum(instance.orders[i].values())
        if total_pedidos + unidades > sol.ub:
            continue

        sol.x[i] = 1
        sol.atualizar_corredores()

        if sol.armazenamento_suficiente():
            total_pedidos += unidades
        else:
            sol.x[i] = 0
            sol.atualizar_corredores()

        if sol.lb <= total_pedidos <= sol.ub and sol.armazenamento_suficiente():
            break

    if not sol.verificacao_solucao():
        raise Exception("Reparação falhou.")

    sol.atualizar_corredores()
    harmony[:n_pedidos] = sol.x
    harmony[n_pedidos:] = sol.y

    return harmony
