import argparse
import random

from src import harmony_search


def run(inst, seed=0, maxIters=200, n=10, hms=100, hmcr=0.9, par=0.1):
    random.seed(seed)
    #no return ele também tem que ler a instância
    return harmony_search.execute(maxIters, n, hms, hmcr, par)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parâmetros PSO.')
    parser.add_argument('--instance', type=str, help='Instância')
    parser.add_argument('--seed', type=int, default=0, help='Seed')
    parser.add_argument('--maxIters', type=int, default=200, help='Número de iterações')
    #variável do problema
    parser.add_argument('--n', type=int, default=10, help='N')
    parser.add_argument('--hms', type=int, default=100, help='Tamanho da Harmony Memory')
    parser.add_argument('--hmcr', type=float, default=0.9, help='Harmony Memory Considering Rate')
    parser.add_argument('--par', type=float, default= 0.1, help='Pitch Ajusting Rate')
    args = parser.parse_args()

    sol = run(
        args.instance,
        seed=args.seed,
        maxIters=args.maxIters,
        n=args.n,
        hms=args.hms,
        hmcr=args.hmcr,
        par=args.par
    )

    print(sol['of'])