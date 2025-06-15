import random
import numpy as np

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

def geracao_harmonia(n, harmony_memory, hmcr, par):
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

    return new_harmony

def atualizar_harmony_memory(harmony_memory, new_harmony, ofv):
    new_ofv = ofv(new_harmony)
    new_harmony_avaliado = np.append(new_harmony, new_ofv)

    if new_ofv > harmony_memory[-1, -1]:
        harmony_memory[-1] = new_harmony_avaliado
        harmony_memory = harmony_memory[harmony_memory[:, -1].argsort()[::-1]]

    return harmony_memory

def execute(n, hms, maxIters, hmcr, par, ofv, construtor_solucao=None):
    harmony_memory = iniciar_harmony_memory(n, hms, ofv, construtor_solucao)

    best_harmony = harmony_memory[0, :-1].astype(int).copy()
    best_ofv = harmony_memory[0, -1]

    for _ in range(maxIters):
        new_harmony = geracao_harmonia(n, harmony_memory, hmcr, par)
        harmony_memory = atualizar_harmony_memory(harmony_memory, new_harmony, ofv)

        if harmony_memory[0, -1] > best_ofv:
            best_ofv = harmony_memory[0, -1]
            best_harmony = harmony_memory[0, :-1].astype(int).copy()

    return {
        'solution': best_harmony,
        'of': best_ofv
    }