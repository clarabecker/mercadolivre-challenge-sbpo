import random
import timeit
import numpy as np
from .solution import Solution
from .repair import reparar_harmonia

def calcular_probabilidades(harmony_memory):
    n_bits = harmony_memory.shape[1] - 1
    prob = np.mean(harmony_memory[:, :n_bits], axis=0)
    prob = np.clip(prob, 0.1, 0.9)
    return prob

def pitch_adjustment(harmony, harmony_memory, par):
    n = len(harmony)
    h1 = harmony_memory[random.randint(0, len(harmony_memory) - 1), :-1].astype(int)
    h2 = harmony_memory[random.randint(0, len(harmony_memory) - 1), :-1].astype(int)
    for i in range(n):
        if h1[i] != h2[i] and random.random() < par:
            harmony[i] = 1 - harmony[i]
    return harmony

def verificar_timeout(start, timeout=900):
    current_time = timeit.default_timer() - start
    return current_time > timeout

def geracao_harmonia(n, harmony_memory, instance, par, start, timeout=60):
    prob = calcular_probabilidades(harmony_memory)
    new_harmony = np.zeros(n, dtype=int)

    for i in range(n):
        if verificar_timeout(start, timeout):
            break
        new_harmony[i] = 1 if random.random() < prob[i] else 0

    new_harmony = pitch_adjustment(new_harmony, harmony_memory, par)
    new_harmony = reparar_harmonia(new_harmony, instance)
    return new_harmony

def iniciar_harmony_memory(n, hms_size, ofv, construtor_solucao=None, start=None, timeout=60):
    harmony_memory = np.zeros((hms_size, n + 1), dtype=float)

    for i in range(hms_size):
        if verificar_timeout(start, timeout):
            return harmony_memory

        if construtor_solucao:
            harmony_vector = construtor_solucao()
        else:
            harmony_vector = np.array([random.choice([0, 1]) for _ in range(n)], dtype=int)

        harmony_memory[i, :-1] = harmony_vector
        harmony_memory[i, -1] = ofv(harmony_vector)

    harmony_memory = harmony_memory[harmony_memory[:, -1].argsort()[::-1]]
    return harmony_memory

def atualizar_harmony_memory(harmony_memory, new_harmony, ofv):
    new_ofv = ofv(new_harmony)
    new_harmony_avaliado = np.append(new_harmony, new_ofv)

    if new_ofv > harmony_memory[-1, -1]:
        harmony_memory[-1] = new_harmony_avaliado
        harmony_memory = harmony_memory[harmony_memory[:, -1].argsort()[::-1]]

    return harmony_memory

def execute(n, hms, maxIters, ofv, construtor_solucao, par):
    timeout = 60
    start = timeit.default_timer()

    harmony_memory = iniciar_harmony_memory(n, hms, ofv, construtor_solucao, start, timeout)
    instance = ofv.keywords['instance']

    best_harmony = harmony_memory[0, :-1].astype(int).copy()
    best_ofv = harmony_memory[0, -1]

    for i in range(maxIters):
        if verificar_timeout(start, timeout):
            print(f"Melhor solução parcial encontrada com OFV = {best_ofv}")
            break

        new_harmony = geracao_harmonia(n, harmony_memory, instance, par, start, timeout)
        harmony_memory = atualizar_harmony_memory(harmony_memory, new_harmony, ofv)

        if harmony_memory[0, -1] > best_ofv:
            best_ofv = harmony_memory[0, -1]
            best_harmony = harmony_memory[0, :-1].astype(int).copy()

    n_pedidos = len(instance.orders)
    sol = Solution(instance)
    sol.x = best_harmony[:n_pedidos]
    sol.y = best_harmony[n_pedidos:]
    sol.of = best_ofv

    return sol
