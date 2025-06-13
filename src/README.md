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
