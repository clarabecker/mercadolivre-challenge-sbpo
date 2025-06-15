# Aspectos gerais do algoritmo

## Execução do algoritmo 

+ Para execução do algoritmo a pasta src deve ser aberta no terminal. 
+ O script "main.py" deve ser executado
+ No parâmetro "--instance" deve ser passado a pasta de destino das instâncias "a" ou "b" + "/" nome da instância desejada. Exemplo:

```bash
python3 main.py --instance a/instance_0003.txt
```

## Valor default dos parâmetros

+ seed = 0
+ Tamanho da Harmony Memory: hms = 100
+ Número de Iterações: maxIters = 200
+ Taxa de consideração da Harmony Memory: hmcr = 0.9
+ Taxa de ajuste de tom: par = 0.1
+ Para passar parâmetros específicos usar "--" e nome do parâmetro. Exemplo:

```bash
python3 main.py --instance a/instance_0003.txt --maxIters 5000 --hms 200 --hmcr 0.7 --par 0.3
```
## Heurística Construtiva

Através de múltiplas tentativas (1000), o componente seleciona um tamanho aleatório para a o tamanho da onda, dentro dos limites mínimo e máximo. A seleção do tamanho da onda é feita para garantir a restrição dos limites. A lista dos candidatos é "embaralhada". A heurística construtiva itera sobre a lista de pedidos candidatos e tenta adicionar um por um. É verificada a viabilidade do pedido, se o estoque nos corredores selecionados é suficiente. Se esta condição for verdadeira o pedido é adicionado na solução, caso contrário itera para o próximo candidato na lista. A construção termina quando atingir o tamanho escolhido para onda ou esgotar o número de candidatos. Devido ao caso da última alternativa, é feita uma última verificação, se os pedidos adicionados respeitam o número mínimo. 
