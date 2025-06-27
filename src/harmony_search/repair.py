from .solution import Solution


def reparar_harmonia(harmony, instance):
    n_pedidos = len(instance.orders)
    n_corredores = len(instance.aisles)

    sol = Solution(instance)
    sol.x = harmony[:n_pedidos].copy()
    sol.atualizar_corredores()

    # Defina a função antes de usar no sorted
    def pseudo_utilidade(i):
        corredores_necessarios = instance.order_aisles[i]
        custo = len([c for c in corredores_necessarios if sol.y[c] == 1])
        beneficio = sum(instance.orders[i].values())
        return beneficio / custo if custo > 0 else beneficio

    pedidos_ativos = [i for i in range(n_pedidos) if sol.x[i] == 1]

    while not (sol.lb <= sum(sum(instance.orders[i].values()) for i in range(n_pedidos) if sol.x[i] == 1) <= sol.ub and sol.armazenamento_suficiente()):
        if not pedidos_ativos:
            break

        i_remove = min(pedidos_ativos, key=pseudo_utilidade)
        sol.x[i_remove] = 0
        sol.atualizar_corredores()
        pedidos_ativos.remove(i_remove)

    pedidos_inativos = [i for i in range(n_pedidos) if sol.x[i] == 0]
    # Aqui já funciona pois a função está definida
    pedidos_inativos = sorted(pedidos_inativos, key=lambda i: -pseudo_utilidade(i))

    for i in pedidos_inativos:
        sol.x[i] = 1
        sol.atualizar_corredores()

        total_unidades = sum(sum(instance.orders[j].values()) for j in range(n_pedidos) if sol.x[j] == 1)

        if total_unidades > sol.ub or not sol.armazenamento_suficiente():
            sol.x[i] = 0
            sol.atualizar_corredores()

        if sol.lb <= total_unidades <= sol.ub and sol.armazenamento_suficiente():
            break

    harmony[:n_pedidos] = sol.x
    harmony[n_pedidos:n_pedidos + n_corredores] = sol.y

    if not sol.verificacao_solucao():
        raise Exception("Reparação falhou: solução inviável")

    return harmony