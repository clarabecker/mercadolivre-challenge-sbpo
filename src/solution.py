import random

class Solution:

    x = None  # Pedidos escolhidos
    y = None  # Corredores escolhidos
    lb = None  # Limite inferior
    ub = None  # Limite superior

    def __init__(self, I, S=None):
        self.I = I

        if S is not None:
            self.x = S.x.copy()
            self.y = S.y.copy()
            self.lb = S.lb
            self.ub = S.ub
        else:
            self.x = [0] * len(I.orders)
            self.y = [0] * len(I.aisles)
            self.lb = I.wave_size_lb
            self.ub = I.wave_size_ub

    def construcao_inicial(self):
        num_pedidos = len(self.I.orders)
        lb = min(self.lb, num_pedidos)
        ub = min(self.ub, num_pedidos)

        self.x = [0] * len(self.I.orders)
        self.y = [0] * len(self.I.aisles)

        # Tamanho da onda a ser montada
        tamanho_wave = random.randint(lb, ub)

        # Ordena os pedidos com menos corredores primeiro (heurística gulosa)
        pedidos_candidatos = list(range(num_pedidos))
        pedidos_candidatos.sort(key=lambda p: len(self.I.order_aisles[p]))

        pedidos_adicionados = 0

        for pedido_candidato in pedidos_candidatos:
            if pedidos_adicionados >= tamanho_wave:
                break

            self.x[pedido_candidato] = 1

            corredores_necessarios = []
            for a in self.I.order_aisles[pedido_candidato]:
                if self.y[a] == 0:
                    self.y[a] = 1
                    corredores_necessarios.append(a)

            if self.armazenamento_suficiente():
                pedidos_adicionados += 1
            else:
                self.x[pedido_candidato] = 0
                for a in corredores_necessarios:
                    self.y[a] = 0

        if pedidos_adicionados < lb:
            raise Exception("Sem solução viável.")

    def armazenamento_suficiente(self):

        itens_pedidos = set()

        for o, pedido_selecionado in enumerate(self.x):
            if pedido_selecionado:
                itens_pedidos.update(self.I.orders[o].keys())

        if not itens_pedidos:
            return True

        # para cada item confere estoque
        for item in itens_pedidos:
           # demanda do item
            demanda_total = 0
            for o, pedido_selecionado in enumerate(self.x):
                if pedido_selecionado:
                    demanda_total += self.I.orders[o].get(item, 0)

            # calcula o estoque total do item nos corredores selecionados
            estoque_total = 0
            for a, pedido_selecionado in enumerate(self.y):
                if pedido_selecionado:
                    estoque_total += self.I.aisles[a].get(item, 0)

            if demanda_total > estoque_total:
                return False

        return True

    def verificacao_solucao(self):

        num_pedidos_selecionados = sum(self.x)

        if not (self.lb <= num_pedidos_selecionados <= self.ub):
            return False

        if not self.armazenamento_suficiente():
            return False

        return True

    def calculo_ofv(self):
        numerador = 0
        denominador = sum(self.y)

        if denominador == 0:
            return 0

        for o, pedidos_selecionados in enumerate(self.x):
            if pedidos_selecionados:
                for a in self.I.order_aisles[o]:
                    numerador += self.I.u[a][o]

        return numerador / denominador