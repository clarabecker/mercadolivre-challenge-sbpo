import argparse
import random

from src import harmony_search

def run(inst, seed=0, maxIters=200, n=10, bounds=10,  hms=100, hmcr=0.9, par=0.1, bw=0.9):
    random.seed(seed)

    # Solução inicial(fazer)
    obj = 0

    return harmony_search.execute(n, bounds, hms, maxIters, hmcr, par, bw, obj)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parâmetros Harmony Search.')
    parser.add_argument('--instance', type=str, help='Instância')
    parser.add_argument('--seed', type=int, default=0, help='Seed')
    parser.add_argument('--n', type=int, default=10, help='Dimensões do problema')
    parser.add_argument('--bounds', type=int, help='Limite das variáveis')
    parser.add_argument('--hms', type=int, default=100, help='Tamanho da Harmony Memory')
    parser.add_argument('--maxIters', type=int, default=200, help='Número de iterações')
    parser.add_argument('--hmcr', type=float, default=0.9, help='Harmony Memory Considering Rate')
    parser.add_argument('--par', type=float, default= 0.1, help='Pitch Ajusting Rate')
    parser.add_argument('--bw', type=float, default=0.1, help='Bandwidth')
    args = parser.parse_args()

    sol = run(
        args.instance,
        seed=args.seed,
        n=args.n,
        bounds=args.bounds,
        maxIters=args.maxIters,
        hms=args.hms,
        hmcr=args.hmcr,
        par=args.par,
        bw=args.bw
    )

    print(sol['of'])