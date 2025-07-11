# O Problema da Seleção de Pedidos Ótima

O objetivo do problema de coleta de pedidos em waves é selecionar um subconjunto de pedidos do backlog, ou seja, a wave, e um subconjunto de corredores
(locais de coleta) que maximizem a produtividade do processo de coleta. Isso
é conseguido ao criar condções favoráveis à geração de rotas de coleta eficientes. Para este desafio, vamos explorar uma dessas condições, que é concentrar
os itens da wave na menor quantidade possível de corredores, respeitando as
restrições.

## Harmony Search

O Harmony Search (HS) é um algoritmo baseado em população, inspirado na improvisação de músicos. Onde a solução é representada por uma harmonia. O algorimo possui os seguintes passos: 

<img src="https://github.com/user-attachments/assets/a8828d7a-9c7d-4e8f-b97d-1e9dcd23551b" width="500"/>

**1. Inicialição dos parâmetros:**
+ Dimensão da variável N;
+ Harmony Memory Size (HMS);
+ Número Máximo de Iterações (maxIters);
+ Pitch Adjusting Rate (PAR);

Os primeiros parâmetros são relacionados a Harmony Memory (HM) que armazena as melhores soluções encontradas até a iteração atual. O HMS é o número de soluções armazenadas na Harmony Memory. O PAR é a probabilidade de ajuste de um valor escolhido presenta na memória, semelhante a ajustar o tom de uma nota musical. 
  
**2. Inicialização da Harmony Memory:**

O algoritmo começa criando um conjunto inicial de soluções. Cada solução passa por uma avaliação, segundo cálculo da função objetivo. As soluções armazenadas na HM, são ordenadas, no caso de maximização da maior para menor. 

**3. Improvisação de Nova Harmonia:**

 Após a criação, a qualidade da nova harmonia também é calculada através da função objetivo. 

**4. Atualização da Harmony Memory:**

A nova harmonia é comparada com a pior harmonia na HM. Se a nova harmonia gerada é melhor, ela substitui a pior na memória. 

**5. Verificação do critério de parada:**

Se o número da iteração atual for menor que o número máximo de iteraçõs, então os passos 3 e 4 são repetidos. Caso contrário o algoritmo para. 

## Mean Harmony e Distribuição de Probabilidade

Como nova abordagem para resoluçá̃o de problemas da mochila multidimensionais de grande escala, foi desenvolvido um algoritmo de busca harmônica binária. Em vez de realizar alterações no velor de solução, o algoritmo calcula, para cada variável a frequência com que o valor 1 aparece na memória.

<img src="https://github.com/user-attachments/assets/293270d1-37a8-4484-9672-62996153edda" width="300"/>

Em seguida, é realizada a construção da Mean Harmony (MH) que presenta a tendência mais forte da memória para cada bit. A MH substitui a Harmony Memory tradicional que armazenava soluções completas. O parâmetro da taxa de consideração do uso da memória é substituído pelo valor da média, ou seja, nessa versão não é considerado esse parâmetro.

<img src="https://github.com/user-attachments/assets/856b52a8-7256-4701-8c57-a68cadc85ea4" width="300"/>

O ajuste de tom  é baseado na divergência entre pares de valores da memória de harmonia. Quando dois valores em uma mesma posição são diferentes, há uma chance — no caso da nossa implementação, determinada pelo parâmetro PAR (pitch adjustment rate) — de inverter o valor correspondente na nova solução. 

