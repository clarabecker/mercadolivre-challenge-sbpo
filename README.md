# O Problema da Seleção de Pedidos Ótima

O objetivo do problema de coleta de pedidos em waves é selecionar um subconjunto de pedidos do backlog, ou seja, a wave, e um subconjunto de corredores
(locais de coleta) que maximizem a produtividade do processo de coleta. Isso
é conseguido ao criar condções favoráveis à geração de rotas de coleta eficientes. Para este desafio, vamos explorar uma dessas condições, que é concentrar
os itens da wave na menor quantidade possível de corredores, respeitando as
restrições.

## Harmony Search

![image](https://github.com/user-attachments/assets/d469a7fb-16c9-48a9-964c-93f709165310)

O Harmony Search (HS) é um algoritmo baseado em população, inspirado na improvisação de músicos. Possui os seguintes passos: 

**1.Inicialição dos parâmetros:**
+ Dimensão da variável N;
+ Limites inferior e superior do domínio de busca (LB, UB);
+ Harmony Memory Considering Rate (HMCR);
+ Pitch Adjusting Rate (PAR);
+ Bandwidth (bw).
  
**2.Inicialização da Harmony Memory:**
Matriz (N*HMS), cujo valor inicial consiste em N vetores aleatórios entre os limiter inferior e superios (LB, UB) do domínio de busca do problema. 

Os primeiros parâmetros são relacionados a Harmony Memory (HS) que armazena as melhores soluções encontradas até a iteração atual. O HMS é o número de soluções armazenadas na Harmony Memory. O HMCR é a probabilidade de escolha dos valores das soluções armazenadas na memória.
O PAR é a probabilidade de ajuste de um valor escolhido presenta na memória, semelhante a ajustar o tom de uma nota musical. O bw controla a intensidade do auste do tom, define o quão longe o novo valor pode estar do antigo. 
