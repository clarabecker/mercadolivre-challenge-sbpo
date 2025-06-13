import argparse
import random
import functools
from harmony_search import execute
from avaliacao import avaliar_harmonia
from instance import Instance
from pathlib import Path  # 1. Importar a classe Path

if __name__ == '__main__':
    SCRIPT_DIR = Path(__file__).parent
    BASE_INSTANCES_DIR = SCRIPT_DIR / '..' / 'instances'

    parser = argparse.ArgumentParser(description='Parâmetros Harmony Search.')
    parser.add_argument('--instance', type=str, required=True,
                        help='Caminho da instância a partir da pasta "instances" (ex: a/instance_0003.txt)')
    parser.add_argument('--seed', type=int, default=0, help='Seed')
    parser.add_argument('--hms', type=int, default=100, help='Tamanho da Harmony Memory')
    parser.add_argument('--maxIters', type=int, default=200, help='Número de iterações')
    parser.add_argument('--hmcr', type=float, default=0.9, help='Harmony Memory Considering Rate')
    parser.add_argument('--par', type=float, default=0.1, help='Pitch Ajusting Rate')
    args = parser.parse_args()

    full_instance_path = BASE_INSTANCES_DIR / args.instance

    instance = Instance(full_instance_path)

    # Dimensão da solução do vetor no algortimo de busca Harmony Search
    n_pedidos = len(instance.orders)
    n_corredores = len(instance.aisles)
    n = n_pedidos + n_corredores

    random.seed(args.seed)

    ofv = functools.partial(avaliar_harmonia, instance=instance)

    sol = execute(
        n=n,
        hms=args.hms,
        maxIters=args.maxIters,
        hmcr=args.hmcr,
        par=args.par,
        ofv=ofv
    )

    print(sol['of'])