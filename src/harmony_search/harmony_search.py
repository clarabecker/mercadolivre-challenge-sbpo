import random
import numpy as np
from .solution import Solution
from .repair import reparar_harmonia

def calcular_probabilidades(harmony_memory):
    n_bits = harmony_memory.shape[1] - 1  # exclui OFV
    prob = np.mean(harmony_memory[:, :n_bits], axis=0)
    return prob

def gerar_mean_harmony(probabilidades):
    return np.array([1 if p > 0.5 else 0 for p in probabilidades], dtype=int)

def pitch_adjustment(harmony, harmony_memory):
    n = len(harmony)
    h1 = harmony_memory[random.randint(0, len(harmony_memory)-1), :-1].astype(int)
    h2 = harmony_memory[random.randint(0, len(harmony_memory)-1), :-1].astype(int)

    for i in range(n):
        if h1[i] != h2[i]:  # se há diversidade
            if random.random() < 0.5:  # aplica ajuste com base na diferença
                harmony[i] = 1 - harmony[i]

    return harmony

def geracao_harmonia(n, harmony_memory, instance):
    prob = calcular_probabilidades(harmony_memory)
    new_harmony = np.zeros(n, dtype=int)

    for i in range(n):
        new_harmony[i] = 1 if random.random() < prob[i] else 0

    new_harmony = pitch_adjustment(new_harmony, harmony_memory)
    new_harmony = reparar_harmonia(new_harmony, instance)
    return new_harmony

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


def atualizar_harmony_memory(harmony_memory, new_harmony, ofv):
    new_ofv = ofv(new_harmony)
    new_harmony_avaliado = np.append(new_harmony, new_ofv)

    if new_ofv > harmony_memory[-1, -1]:
        harmony_memory[-1] = new_harmony_avaliado
        harmony_memory = harmony_memory[harmony_memory[:, -1].argsort()[::-1]]

    return harmony_memory

def execute(n, hms, maxIters, ofv, construtor_solucao=None):
    harmony_memory = iniciar_harmony_memory(n, hms, ofv, construtor_solucao)
    instance = ofv.keywords['instance']

    best_harmony = harmony_memory[0, :-1].astype(int).copy()
    best_ofv = harmony_memory[0, -1]

    for _ in range(maxIters):
        new_harmony = geracao_harmonia(n, harmony_memory, instance)
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





