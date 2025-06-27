def geracao_harmonia(n, harmony_memory, hmcr, par, instance):
    new_harmony = np.zeros(n, dtype=int)

    for i in range(n):
        r1 = random.random()
        r2 = random.random()

        if r1 < hmcr:
            rand_idx = random.randint(0, len(harmony_memory) - 1)
            new_harmony[i] = int(harmony_memory[rand_idx, i])

            # flip bit
            if r2 < par:
                new_harmony[i] = 1 - new_harmony[i]
        else:
            new_harmony[i] = random.choice([0, 1])

    new_harmony = reparar_harmonia(new_harmony, instance)
    return new_harmony

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

        #pedido com maior custo
        i_remove = max(pedidos_sol, key=lambda i: sum(instance.orders[i].values()))

        sol.x[i_remove] = 0
        sol.atualizar_corredores()
        total_pedidos -= sum(instance.orders[i_remove].values())

    #inclui pedido candidato na solução
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