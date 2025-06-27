import argparse
import random
import functools
import subprocess
import numpy as np
from pathlib import Path
from harmony_search.instance import Instance
from harmony_search.solution import Solution
from harmony_search.harmony_search import execute
from harmony_search.avaliacao import avaliar_harmonia

if __name__ == '__main__':
    SCRIPT_DIR = Path(__file__).parent
    BASE_INSTANCES_DIR = SCRIPT_DIR / '..' / 'instances'
    #integração com o cheker 
    #avaliação experimental com dois últimos parâmetros
    parser = argparse.ArgumentParser(description='Parâmetros Harmony Search.')
    parser.add_argument('--instance', type=str, required=True, help='Caminho da instância')
    parser.add_argument('--seed', type=int, default=0, help='Seed')
    parser.add_argument('--hms', type=int, default=500, help='Tamanho da Harmony Memory')
    parser.add_argument('--maxIters', type=int, default=1000, help='Número de iterações')
    args = parser.parse_args()

    full_instance_path = BASE_INSTANCES_DIR / args.instance
    instance = Instance(full_instance_path)
    random.seed(args.seed)

    #define dimensão n do algoritmo
    n_pedidos = len(instance.orders)
    n_corredores = len(instance.aisles)
    n = n_pedidos + n_corredores
    ofv = functools.partial(avaliar_harmonia, instance=instance)

    #vetor de solução conforme dimensão definida
    def construtor_de_solucao():
        sol = Solution(instance)
        sol.construcao_inicial()

        return sol.x + sol.y

    sol = execute(
        n=n,
        hms=args.hms,
        maxIters=args.maxIters,
        ofv=ofv,
        construtor_solucao=construtor_de_solucao
    )

    pedidos = [i for i, v in enumerate(sol.x) if v == 1]
    corredores = [i for i, v in enumerate(sol.y) if v == 1]

    ofv_1 = sol.calculo_ofv()

    print("Função Objetivo:", ofv_1)

    print(f"Validando solução")

    output_path = SCRIPT_DIR / 'results/output.txt'
    sol.salvar_solucao_em_arquivo(np.concatenate([sol.x, sol.y]), n_pedidos, n_corredores, output_path)

    def rodar_checker(input_file, output_file):
        result = subprocess.run(
            ['python3', 'checker.py', input_file, output_file],
            capture_output=True,
            text=True
        )
        print(result.stdout)
        if result.returncode != 0:
            print("Checker terminou com erro:")
            print(result.stderr)


    rodar_checker(str(full_instance_path), str(output_path))




