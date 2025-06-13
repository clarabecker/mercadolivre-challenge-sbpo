# O Problema da Seleção de Pedidos Ótima

O objetivo do problema de coleta de pedidos em waves é selecionar um subconjunto de pedidos do backlog, ou seja, a wave, e um subconjunto de corredores
(locais de coleta) que maximizem a produtividade do processo de coleta. Isso
é conseguido ao criar condções favoráveis à geração de rotas de coleta eficientes. Para este desafio, vamos explorar uma dessas condições, que é concentrar
os itens da wave na menor quantidade possível de corredores, respeitando as
restrições.

## Harmony Search

![image](https://github.com/user-attachments/assets/a8828d7a-9c7d-4e8f-b97d-1e9dcd23551b)

O Harmony Search (HS) é um algoritmo baseado em população, inspirado na improvisação de músicos. Onde a solução é representada por uma harmonia. O algorimo possui os seguintes passos: 

**1. Inicialição dos parâmetros:**
+ Dimensão da variável N;
+ Harmony Memory Considering Rate (HMCR);
+ Pitch Adjusting Rate (PAR);
  
**2. Inicialização da Harmony Memory:**
Matriz (N*HMS), cujo valor inicial consiste em N vetores aleatórios entre os limiter inferior e superios (LB, UB) do domínio de busca do problema. 

Os primeiros parâmetros são relacionados a Harmony Memory (HS) que armazena as melhores soluções encontradas até a iteração atual. O HMS é o número de soluções armazenadas na Harmony Memory. O HMCR é a probabilidade de escolha dos valores das soluções armazenadas na memória.
O PAR é a probabilidade de ajuste de um valor escolhido presenta na memória, semelhante a ajustar o tom de uma nota musical. O bw controla a intensidade do auste do tom, define o quão longe o novo valor pode estar do antigo. 

**3. Improvisação de Nova Harmonia:**
Uma nova harmonia (xnew) é gerada com base no parâmetros (HMCR), taxa de ajuste de tom (PR) e uma escolha aleatória. Um novo valor de r1 pertencente (0,1) é gerado, ele é comparado com o HMCR. Se r1 < HMCR, cada componente da nova harmonia é ecolhido aleatoriamente a partir da Harmony Memory. Um novo número alatório r2 pertencente (0,1) é gerado, se r2 < PAR o componente escolhido na etapa anterior pe ajustado de acordo com bw. 

**4. Atualização da Harmony Memory:**
Se o valor de adequação da nova harmonia (xnew) for melhor do que o valor de adequação da pior harmonia (xworst) na HM, a pior solução na HM será substituida pela nova harmonia. 

**5. Verificação do critério de parada:**
Se o número da iteração atual (t) for menor que o número máximo de iteraçõs, então os passos 3 e 4 são repetidos. Caso contrário o algoritmo para. 
