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
+ Taxa de ajuste de tom: par = 0.3
+ Para passar parâmetros específicos usar "--" e nome do parâmetro. Exemplo:

```bash
python3 main.py --instance a/instance_0003.txt --maxIters 5000 --hms 200 --hmcr 0.7 --par 0.3
```
## Heurística Construtiva

Esse método tenta construir uma solução inicial para um problema de seleção de pedidos e corredores, respeitando um limite inferior (lb) e um limite superior (ub) de unidades. Ele prioriza pedidos que oferecem maior quantidade itens com menor número de corredores ainda não utilizados, tentando montar uma solução viável (que tenha armazenamento suficiente e respeite os limites) que atinja pelo menos o limite inferior de unidades. O looping do algoritmo para quando a quantidade de pedidos selecionados atinge o limite superior. 

## Geração de Nova Harmonia 

Para cada posição i da harmonia, escolhe 1 com base na probabilidade, ou 0 caso contrário. Isso faz com que o novo vetor combine características das soluções anteriores,componentes com alta probabilidade de 1 tendem a ser escolhidos. Logo após, a geração realiza um (pitch ajustment) ajuste fino da solução. Para cada posição i, verifica se os valores de h1[i] e h2[i] são diferentes. Se forem diferentes, há chance de fazer o pitch adjustment naquela posição:

Com probabilidade par, o valor de harmony[i] é invertido (1 - harmony[i]).


```markdown
for i in range(n):
    if h1[i] != h2[i]:
        if random.random() < par:
            harmony[i] = 1 - harmony[i]
```

## Estratégia de reparação da solução

A estratégia começa com a solução gerada pelo Harmony Search, entra em looping até a solução ser viável, ou seja, respeitar os limites superior e inferior e armazeamento dos corredores. Dentro do looping a reparação remove pedidos que utilizam maios corredore. Logo após, a reparação tenta melhorar a solução adicionando pedidos candidatos. Os pedidos candidatos são ordenados de acordo com o número de itens, do menor para o maior. Para a adição de pedidos candidatos ainda é verificado a viabilidade da solução. O processo continua até que todos os pedidos candidatos tenham sido incluídos no lugar dos removidos.




