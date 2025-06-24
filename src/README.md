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

A construção  possui um tamanho alvo da wave, valor aleatório que respeita os limites mínimos e máximos. Primeiro a construção tenta adicionar os pedidos que possuem itens que exigem menos corredores, para isso a lista de pedidos candidatos é ordenada conforme corredores associados ao pedido. A wave é construida iterativamente, sempre verificando a restrição de armazenamento dos corredores. Se a restrição for violada, a adição do pedido é desfeita. Os corredores necessários por esse pedido que antes eram abrangidos pela solução, não são mais utilizados. 

## Geração de Nova Harmonia 

A estratégia de geração consiste nos seguintes passos: geração de um número aleatório (r1), se este for menor que o parâmetros HMCR o algoritmo busca na Harmony Memory (HM) elementos que foram utilizados em boas soluções já existentes. Se a HM é considerada, é realizado um ajustem de tom segundo parâmetro PAR.

Se novo número aleatório gerado (r2) é menor que PAR, o ajuste é um "flip" de bit, o valor é invertido. Isso funciona como pequena perturbação, explorando a vizinhança das soluções presentes na HM. 

Caso contrário o algoritmo seleciona um elemento aleatório diferente, sem considerar HM. 

## Estratégia de reparação da solução

A estratégia começa com a solução gerada pelo Harmony Search, entra em looping até a solução ser viável, ou seja, respeitar os limites superior e inferior e armazeamento dos corredores. Dentro do looping a reparação remove pedidos com as maiores quantidades de itens. Logo após, a reparação tenta melhorar a solução adicionando pedidos candidatos. Os pedidos candidatos são ordenados de acordo com o número de itens, do menor para o maior. Para a adição de pedidos candidatos ainda é verificado a viabilidade da solução. O processo continua até que todos os pedidos candidatos tenham sido incluídos no lugar dos removidos.




