# O Problema da Seleção de Pedidos Ótima

O objetivo do problema de coleta de pedidos em waves é selecionar um subconjunto de pedidos do backlog, ou seja, a wave, e um subconjunto de corredores
(locais de coleta) que maximizem a produtividade do processo de coleta. Isso
é conseguido ao criar condções favoráveis à geração de rotas de coleta eficientes. Para este desafio, vamos explorar uma dessas condições, que é concentrar
os itens da wave na menor quantidade possível de corredores, respeitando as
restrições.

## Harmony Search

O Harmony Search (HS) é um algoritmo baseado em população, inspirado na improvisação de músicos. Onde a solução é representada por uma harmonia. O algorimo possui os seguintes passos: 

![image](https://github.com/user-attachments/assets/a8828d7a-9c7d-4e8f-b97d-1e9dcd23551b)

**1. Inicialição dos parâmetros:**
+ Dimensão da variável N;
+ Harmony Memory Size (HMS);
+ Número Máximo de Iterações (maxIters);
+ Harmony Memory Considering Rate (HMCR);
+ Pitch Adjusting Rate (PAR);

Os primeiros parâmetros são relacionados a Harmony Memory (HM) que armazena as melhores soluções encontradas até a iteração atual. O HMS é o número de soluções armazenadas na Harmony Memory. O HMCR é a probabilidade de escolha dos valores das soluções armazenadas na memória, determina a frequência com que o algoritmo se baseia nas soluções existentes na memória para criar outra solução. O PAR é a probabilidade de ajuste de um valor escolhido presenta na memória, semelhante a ajustar o tom de uma nota musical. 
  
**2. Inicialização da Harmony Memory:**

O algoritmo começa criando um conjunto inicial de soluções. Cada solução passa por uma avaliação, segundo cálculo da função objetivo. As soluções armazenadas na HM, são ordenadas, no caso de maximização da maior para menor. 

**3. Improvisação de Nova Harmonia:**
Uma nova solução candidata é criada com base nas soluções existentes na HM e na aleatoriedade. Para cada elemento da solução o algoritmo usa um valor de uma das soluções existentes na HM, com base no parâmetro HMCR ou aleatoriedade. Após a criação, a qualidade da nova harmonia também é calculada através da função objetivo. 

**4. Atualização da Harmony Memory:**
A nova harmonia é comparada com a pior harmonia na HM. Se a nova harmonia gerada é melhor, ela substitui a pior na memória. 

**5. Verificação do critério de parada:**
Se o número da iteração atual for menor que o número máximo de iteraçõs, então os passos 3 e 4 são repetidos. Caso contrário o algoritmo para. 
