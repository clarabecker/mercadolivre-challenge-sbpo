import argparse
import random
import functools
import subprocess
import numpy as np
from pathlib import Path
from instance import Instance
from solution import Solution
from harmony_search import execute
from avaliacao import avaliar_harmonia

if __name__ == '__main__':
    SCRIPT_DIR = Path(__file__).parent
    BASE_INSTANCES_DIR = SCRIPT_DIR / '..' / 'instances'
    #integração com o cheker 
    #avaliação experimental com dois últimos parâmetros
    parser = argparse.ArgumentParser(description='Parâmetros Harmony Search.')
    parser.add_argument('--instance', type=str, required=True, help='Caminho da instância')
    parser.add_argument('--seed', type=int, default=0, help='Seed')
    parser.add_argument('--hms', type=int, default=100, help='Tamanho da Harmony Memory')
    parser.add_argument('--maxIters', type=int, default=1000, help='Número de iterações')
    parser.add_argument('--hmcr', type=float, default=0.9, help='Harmony Memory Considering Rate')
    parser.add_argument('--par', type=float, default=0.1, help='Pitch Ajusting Rate')
    args = parser.parse_args()

    full_instance_path = BASE_INSTANCES_DIR / args.instance
    instance = Instance(full_instance_path)
    random.seed(args.seed)

    # Define dimensão n do algoritmo HS
    n_pedidos = len(instance.orders)
    n_corredores = len(instance.aisles)
    n = n_pedidos + n_corredores
    ofv = functools.partial(avaliar_harmonia, instance=instance)

    # Vetor de solução conforme dimensão definida
    def construtor_de_solucao():
        sol = Solution(instance)
        sol.construcao_inicial()

        return sol.x + sol.y

    sol = execute(
        n=n,
        hms=args.hms,
        maxIters=args.maxIters,
        hmcr=args.hmcr,
        par=args.par,
        ofv=ofv,
        construtor_solucao=construtor_de_solucao
    )
    sol = execute(
        n=n,
        hms=args.hms,
        maxIters=args.maxIters,
        hmcr=args.hmcr,
        par=args.par,
        ofv=ofv,
        construtor_solucao=construtor_de_solucao
    )

    vetor_solucao = np.concatenate([sol.x, sol.y])
    valor_ofv = ofv(vetor_solucao)

    print(f"Valor da função objetivo (OFV): {valor_ofv}")

    print(f"Validando solução")

    # Salvar solução para checker
    output_path = SCRIPT_DIR / 'output.txt'
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


    # Depois de gerar o output.txt:
    rodar_checker(str(full_instance_path), str(output_path))
