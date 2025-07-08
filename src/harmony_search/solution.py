import random

import numpy as np
from pathlib import Path
import timeit


class Solution:
    def __init__(self, I, S=None):
        self.I = I
        self.lb = I.wave_size_lb
        self.ub = I.wave_size_ub

        if S is not None:
            self.x = S.x.copy()
            self.y = S.y.copy()
        else:
            self.x = [0] * len(I.orders)
            self.y = [0] * len(I.aisles)

    def construcao_inicial(self):
        num_pedidos = len(self.I.orders)
        self.x = [0] * num_pedidos
        self.y = [0] * len(self.I.aisles)

        total_unidades = 0

        pedidos_candidatos = list(range(num_pedidos))

        def score(pedido):
            unidades = sum(self.I.orders[pedido].values())
            novos_corredores = [a for a in self.I.order_aisles[pedido] if self.y[a] == 0]
            return unidades / (1 + len(novos_corredores))

        pedidos_candidatos.sort(key=score, reverse=True)

        for pedido_candidato in pedidos_candidatos:
            unidades_pedido = sum(self.I.orders[pedido_candidato].values())

            if total_unidades + unidades_pedido > self.ub:
                continue

            self.x[pedido_candidato] = 1
            corredores_novos = []
            for a in self.I.order_aisles[pedido_candidato]:
                if self.y[a] == 0:
                    self.y[a] = 1
                    corredores_novos.append(a)

            if self.armazenamento_suficiente():
                total_unidades += unidades_pedido
            else:
                self.x[pedido_candidato] = 0
                for a in corredores_novos:
                    self.y[a] = 0

            if total_unidades >= self.lb:
                break

        if total_unidades < self.lb:
            raise Exception("Sem solução viável inicial.")

    def armazenamento_suficiente(self):
        itens_pedidos = set()

        for o, pedido_selecionado in enumerate(self.x):
            if pedido_selecionado:
                itens_pedidos.update(self.I.orders[o].keys())

        if not itens_pedidos:
            return True

        for item in itens_pedidos:
            demanda_total = sum(self.I.orders[o].get(item, 0) for o, selected in enumerate(self.x) if selected)
            estoque_total = sum(self.I.aisles[a].get(item, 0) for a, selected in enumerate(self.y) if selected)

            if demanda_total > estoque_total:
                return False

        return True

    def verificacao_solucao(self):
        total_unidades = sum(
            sum(self.I.orders[o].values()) for o, selected in enumerate(self.x) if selected
        )

        if not (self.lb <= total_unidades <= self.ub):
            return False

        if not self.armazenamento_suficiente():
            return False

        return True

    def calculo_ofv(self):
        total_unidades = 0
        pedidos = [i for i, v in enumerate(self.x) if v == 1]
        corredores = [i for i, v in enumerate(self.y) if v == 1]

        for o in pedidos:
            total_unidades += sum(self.I.orders[o].values())

        if len(corredores) == 0:
            return 0

        return total_unidades / len(corredores)

    def atualizar_corredores(self):
        self.y = [0] * len(self.y)
        for i, pedido_ativo in enumerate(self.x):
            if pedido_ativo == 1:
                for corredor in self.I.order_aisles[i]:
                    self.y[corredor] = 1

    def salvar_solucao_em_arquivo(self, solution_vector, n_pedidos, n_corredores, filepath):
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)

        pedidos_selecionados = [i for i in range(n_pedidos) if solution_vector[i] == 1]
        corredores_selecionados = [
            i - n_pedidos for i in range(n_pedidos, n_pedidos + n_corredores)
            if solution_vector[i] == 1
        ]

        with open(filepath, 'w') as f:
            f.write(f"{len(pedidos_selecionados)}\n")
            for p in pedidos_selecionados:
                f.write(f"{p}\n")
            f.write(f"{len(corredores_selecionados)}\n")
            for c in corredores_selecionados:
                f.write(f"{c}\n")


