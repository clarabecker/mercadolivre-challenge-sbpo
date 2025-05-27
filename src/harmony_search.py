import random
import numpy as np

def execute(n, hms, maxIters, hmcr, par):
    # Inicialização da harmony memory (vetores binários)
    harmony_memory = np.array([random.randint(0, 1) for _ in range(n)])

    # Iterações do algoritmo
    for iter in range(maxIters):
        # Geração de uma nova harmonia
        new_harmony = geracao_harmonia(n, harmony_memory, hms, boundary=int(hms * 0.2), hmcr=hmcr, par=par)

        # Avaliação do fitness da nova harmonia
        new_harmony[-1] = avaliar_fitness(new_harmony[:-1])

        # Atualização da Harmony Memory
        harmony_memory = atualizar_harmony_memory(harmony_memory, new_harmony)

        # Exibir a melhor harmonia (melhor solução até agora)
        print(f"Iteração {iter + 1}: Melhor acurácia = {harmony_memory[0][-1]}")
        print("Features selecionadas:", harmony_memory[0][:-1])

    return harmony_memory[0]

def geracao_harmonia(n, harmony_memory, hms, boundary, hmcr, par):
    new_harmony = []

    for i in range(n):
        r1 = random.random()
        r2 = random.random()

        if r1 < hmcr:
            # Escolhe um valor da memória de harmonia (HM) com base em probabilidade
            harmony_index = np.random.randint(hms)  # Índice aleatório
            new_harmony.append(harmony_memory[harmony_index, i])

            # Ajuste de pitch (refinamento do valor)
            if r2 < par:
                new_harmony[-1] = 1 - new_harmony[-1]
        else:
            # Se não escolher da memória, gera aleatoriamente
            new_harmony.append(random.randint(0, 1))

    # Adiciona um espaço para o valor de fitness (que será calculado depois)
    new_harmony.append(0.0)
    return np.array(new_harmony)

def avaliar_fitness(harmony):
    # Simulação do cálculo de fitness (por enquanto apenas retornando um valor aleatório)
    # Aqui você pode colocar o código que calcula a acurácia, por exemplo.
    return random.random()

def atualizar_harmony_memory(harmony_memory, new_harmony):
    # Adiciona a nova harmonia à memória
    harmony_memory = np.vstack([harmony_memory, new_harmony])

    # Ordena a memória com base no fitness (última coluna) e mantém as melhores soluções
    harmony_memory = sorted(harmony_memory, key=lambda x: x[-1], reverse=True)

    # Remove o pior (último da lista)
    harmony_memory = np.array(harmony_memory[:-1])

    return harmony_memory
