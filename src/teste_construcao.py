from solution import Solution
from instance import Instance
import os

# Caminho relativo da instância
instance_file = os.path.join("..", "instances", "a", "instance_0001.txt")

inst = Instance(instance_file)
sol = Solution(inst)
sol.construcao_inicial()

print("Pedidos selecionados:", sol.x)
print("Corredores selecionados:", sol.y)

if sol.solucao_viavel() and sol.aisles_storage():
    print("Solução inicial construída com sucesso!")
    print("OFV:", sol.calculate_ofv())
else:
    print("Solução inválida.")
