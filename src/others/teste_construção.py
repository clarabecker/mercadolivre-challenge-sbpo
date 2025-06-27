from src.harmony_search.solution import Solution
from src.harmony_search.instance import Instance
import os

instance_file = os.path.join("../..", "instances", "a", "instance_0001.txt")

inst = Instance(instance_file)
sol = Solution(inst)
sol.construcao_inicial()

print("Pedidos:", sol.x)
print("Corredores:", sol.y)

if sol.verificacao_solucao():
    print("ofv:", sol.calculo_ofv())
else:
    print("Solução inválida.")