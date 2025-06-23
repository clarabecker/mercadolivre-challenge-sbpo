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
+ Número de Iterações: maxIters = 1000
+ Taxa de consideração da Harmony Memory: hmcr = 0.9
+ Taxa de ajuste de tom: par = 0.1
+ Para passar parâmetros específicos usar "--" e nome do parâmetro. Exemplo:

```bash
python3 main.py --instance a/instance_0003.txt --maxIters 5000 --hms 200 --hmcr 0.7 --par 0.3
```
## Heurística Construtiva

A construção  possui um tamanho alvo da wave, valor aleatório que respeita os limites mínimos e máximos. Primeiro a construção tenta adicionar os pedidos que exigem menos corredores, para isso a lista de pedidos candidatos é ordenada conforme corredores associados ao pedido. A wave é construida iterativamente, sempre verificando a restrição de armazenamento dos corredores. Se a restrição for violada, a adição do pedido é desfeita. Os corredores necessários por esse pedido que antes eram abrangidos pela solução, não são mais utilizados. 

## Geração de Nova Harmonia 

A estratégia de geração consiste nos seguintes passos: geração de um número aleatório (r1), se este for menor que o parâmetros HMCR o algoritmo busca na Harmony Memory (HM) elementos que foram utilizados em boas soluções já existentes. Se a HM é considerada, é realizado um ajustem de tom segundo parâmetro PAR.

Se novo número aleatório gerado (r2) é menor que PAR, o ajuste é um "flip" de bit, o valor é invertido. Isso funciona como pequena perturbação, explorando a vizinhança das soluções presentes na HM. 

Caso contrário o algoritmo seleciona um elemento aleatório diferente, sem considerar HM. 

## Estratégia de reparação da solução

A estratégia de reparação cria uma solução temporária separando o vetor de harmonia, se o número de pedidos selecionados for menor que o número mínimo de pedidos, o algoritmo entra em um looping para adição de candidatos que ainda não estão na solução. Sempre verificando a viabilidade da solução com o pedido adicionado. Após isso, ele entra em um segundo looping para garantir que o número de pedidos não ultrapasse o limite máximo, tentando remover candidatos mantendo a viabilidade da solução. No final do método de reparação a solução é verficada novamente, se ainda não é viável é chamada a construção gulosa para nova solução. 



