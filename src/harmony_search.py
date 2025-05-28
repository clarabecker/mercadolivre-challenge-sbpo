import random
import numpy as np

def iniciarHarmonyMemory(n, hms_size, bounds, ofv):

    # matriz, cada linha é uma harmonia e a última coluna é o valor do valor da função objetivo (ofv)
    harmony_memory = np.zeros((hms_size, n + 1), dtype=float)

    for i in range(hms_size):
        # gera uma harmonia aleatória (valores contínuos)
        harmony_vector = np.array([random.uniform(bounds[j][0], bounds[j][1]) for j in range(n)], dtype=float)

        # atribui o vetor da harmonia e calcula seu fitness
        harmony_memory[i, :-1] = harmony_vector
        harmony_memory[i, -1] = ofv(harmony_vector)

    # ordena a memória pela coluna de ofv em ordem decrescente(para maximização)
    harmony_memory = harmony_memory[harmony_memory[:, -1].argsort()[::-1]]
    return harmony_memory


def geracaoHarmonia(n, harmony_memory, hmcr, par, bw, bounds):
    new_harmony = np.zeros(n)

    for i in range(n):
        r1 = random.random()
        r2 = random.random()

        # escolhe um valor da harmony_memory
        if r1 < hmcr:
            random_harmony_index = random.randint(0, len(harmony_memory) - 1)
            harmony_from_memory = harmony_memory[random_harmony_index, :-1]

            new_harmony[i] = harmony_from_memory[i]
            # ajuste de tom (refinamento do valor)
            if r2 < par:
                if random.random() < 0.5:
                    new_harmony[i] += random.random() * bw
                else:
                    new_harmony[i] -= random.random() * bw

                # valor dentro dos limites
                LB_i, UB_i = bounds[i]
                new_harmony[i] = max(LB_i, min(UB_i, new_harmony[i]))
        else:
            # gera valor aleatório
            LB_i, UB_i = bounds[i]
            new_harmony[i] = random.uniform(LB_i, UB_i)

    return new_harmony

def atualizarHarmonyMemory(harmony_memory, new_harmony, ofv):
    # avalia a harmonia (calcula nova função objetivo -fazer-)
    new_ofv = ofv(new_harmony)

    # combina o vetor da harmonia com ofv
    new_harmony_avaliado = np.append(new_harmony, new_ofv)

    if new_ofv > harmony_memory[-1, -1]:
        harmony_memory[-1] = new_harmony_avaliado

        harmony_memory = harmony_memory[harmony_memory[:, -1].argsort()[::-1]]

    return harmony_memory

# looping principal do algoritmo
def execute(n, bounds, hms, maxIters, hmcr, par, bw, ofv):
    harmony_memory = iniciarHarmonyMemory(n, hms, bounds, ofv)
    best_harmony = harmony_memory[0, :-1].copy()
    best_avaliacao = harmony_memory[0, -1]

    for t in range(maxIters):
        new_harmony = geracaoHarmonia(n, harmony_memory, hmcr, par, bw, bounds)

        harmony_memory = atualizarHarmonyMemory(harmony_memory, new_harmony, ofv)

        if harmony_memory[0, -1] > best_ofv:
            best_ofv = harmony_memory[0, -1]
            best_harmony = harmony_memory[0, :-1].copy()

    return {
        'solution': best_harmony,
        'of': best_ofv
    }


