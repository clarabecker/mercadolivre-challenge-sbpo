import random
import numpy as np
from solution import Solution

def iniciar_harmony_memory(n, hms_size, ofv, construtor_solucao=None):
    harmony_memory = np.zeros((hms_size, n + 1), dtype=float)

    for i in range(hms_size):
        if construtor_solucao:
            harmony_vector = construtor_solucao()
        else:
            harmony_vector = np.array([random.choice([0, 1]) for _ in range(n)], dtype=int)

        harmony_memory[i, :-1] = harmony_vector
        harmony_memory[i, -1] = ofv(harmony_vector)

    harmony_memory = harmony_memory[harmony_memory[:, -1].argsort()[::-1]]
    return harmony_memory

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
    # procedimento de reparação
    new_harmony = reparar_harmonia(new_harmony, instance)
    return new_harmony

def atualizar_harmony_memory(harmony_memory, new_harmony, ofv):
    new_ofv = ofv(new_harmony)
    new_harmony_avaliado = np.append(new_harmony, new_ofv)

    if new_ofv > harmony_memory[-1, -1]:
        harmony_memory[-1] = new_harmony_avaliado
        harmony_memory = harmony_memory[harmony_memory[:, -1].argsort()[::-1]]

    return harmony_memory

def reparar_harmonia(harmony, instance):
    n_pedidos = len(instance.orders)

    # Garantir int
    harmony = [int(val) for val in harmony]

    x = harmony[:n_pedidos]
    y = harmony[n_pedidos:]

    sol_temp = Solution(instance)
    sol_temp.x = x.copy()
    sol_temp.y = y.copy()
    sol_temp.atualizar_corredores()

    # Garantir pelo menos lb pedidos
    while sum(sol_temp.x) < sol_temp.lb:
        candidatos = [i for i in range(n_pedidos) if sol_temp.x[i] == 0]
        if not candidatos:
            break
        random.shuffle(candidatos)
        added = False
        for c in candidatos:
            sol_temp.x[c] = 1
            sol_temp.atualizar_corredores()
            if sol_temp.verificacao_solucao():
                added = True
                break
            else:
                sol_temp.x[c] = 0
        if not added:
            break

    # Garantir no máximo ub pedidos
    while sum(sol_temp.x) > sol_temp.ub:
        candidatos = [i for i in range(n_pedidos) if sol_temp.x[i] == 1]
        if not candidatos:
            break
        random.shuffle(candidatos)
        removed = False
        for c in candidatos:
            sol_temp.x[c] = 0
            sol_temp.atualizar_corredores()
            if sol_temp.verificacao_solucao():
                removed = True
                break
            else:
                sol_temp.x[c] = 1
        if not removed:
            break

    # Verificação final
    if not sol_temp.verificacao_solucao():
        # Você pode tentar reconstruir solução inicial aqui
        try:
            sol_temp.construcao_inicial()
        except Exception:
            print("Falha ao reparar solução, mantendo a melhor tentativa atual.")

    # Atualiza harmony com a solução reparada
    harmony[:n_pedidos] = sol_temp.x
    harmony[n_pedidos:] = sol_temp.y

    return harmony


def execute(n, hms, maxIters, hmcr, par, ofv, construtor_solucao=None):
    harmony_memory = iniciar_harmony_memory(n, hms, ofv, construtor_solucao)
    instance = ofv.keywords['instance']

    best_harmony = harmony_memory[0, :-1].astype(int).copy()
    best_ofv = harmony_memory[0, -1]

    for _ in range(maxIters):
        new_harmony = geracao_harmonia(n, harmony_memory, hmcr, par, instance)
        harmony_memory = atualizar_harmony_memory(harmony_memory, new_harmony, ofv)

        if harmony_memory[0, -1] > best_ofv:
            best_ofv = harmony_memory[0, -1]
            best_harmony = harmony_memory[0, :-1].astype(int).copy()

    n_pedidos = len(instance.orders)
    n_corredores = len(instance.aisles)

    sol = Solution(instance)
    sol.x = best_harmony[:n_pedidos]
    sol.y = best_harmony[n_pedidos:]
    sol.of = best_ofv

    return sol



