<h1 align="center">📝Otimização de Rotas com Lucro Baseada 
em Algoritmos de Colônia de Formigas </h1>
<p align="center">
<img src="./apresentacao/tela_inical.png" alt="capa do projeto" width="700"><br>
<p align="center">
Luan Medrado Moreira, Lucas Rego Da Silva <br>
Centro Universitário Euro Americano (Unieuro), Brasília, Brasil <br>
Email: luan61449@unieuro.com.com, lucas60899 @unieuro.com.com <br>
<br>Orientador <br>
Dr. Aldo Henrique Dias Mendes <br>
Centro Universitário Euro Americano (Unieuro), Brasília, Brasil <br>
Email: aldoh.ti@gmail.com <br>
<p>
<p align="center">
<br strong >Resumo <br>
Este artigo apresenta uma aplicação do algoritmo de Colônia de Formigas (Ant Colony Optimization, 
ACO) para a otimização de rotas visando maximizar lucros em um cenário de transporte de combustíveis 
entre cidades brasileiras. A abordagem utiliza dados de compra e venda de combustíveis para calcular 
diferenças de preços como heurísticas. A implementação segue tendências recentes da literatura, adaptando 
estratégias do ACO para problemas de roteamento e maximização de lucros. Os resultados obtidos 
demonstram a eficácia do método proposto e destacam oportunidades para aprimoramento, como a inclusão 
de restrições temporais e dinâmicas no modelo. <p>
<br>
<p align="center">
INTRODUÇÃO
 1.1. Contextualização <br>
A otimização de rotas é um problema clássico com impacto direto em operações logísticas. 
Algoritmos metaheurísticos, como o ACO, têm se destacado em aplicações como o roteamento de 
veículos capacitados (CVRP) e problemas com múltiplas restrições, incluindo janelas de tempo e 
múltiplos depósitos, devido à sua robustez na busca por soluções eficientes em problemas 
complexos (Jinsi Cai et al., 2022).<br> 
No contexto do transporte de combustíveis, identificar rotas que maximizem lucros baseando-se 
nas diferenças de preços entre cidades oferece um novo campo de estudo. Estratégias híbridas de 
ACO, que combinam heurísticas locais e métodos como busca de vizinhança variável, 
mostraram-se eficazes na literatura para lidar com problemas de otimização onde múltiplas 
variáveis influenciam as decisões de roteamento (Petr Stodola, 2020). <p>
<p align="center">
<br>1.2. Objetivo <br>
O objetivo deste trabalho é implementar uma solução baseada no ACO para maximizar lucros no 
transporte de combustíveis entre cidades, utilizando diferenças de preços de compra e venda 
como heurísticas e feromônios como guia.  <p>
<p align="center">
<br>2. Fundamentação Teórica 
<br>2.1. Algoritmos de Colônia de Formigas 
<br>O ACO é um método bioinspirado que simula o comportamento de formigas ao depositar 
feromônios em caminhos durante a busca por comida. Este método tem sido amplamente aplicado 
em problemas de roteamento devido à sua capacidade de explorar iterativamente o espaço de 
soluções. Estudos recentes adaptaram o ACO para diversos problemas, como roteamento com 
janelas de tempo (Ashima Gupta & Sanjay Saini, 2017) e roteamento de veículos elétricos, onde 
limitações de autonomia e pontos de recarga devem ser considerados (Michalis Mavrouniotis et 
al., 2018). 
<br>2.2. Aplicação no Roteamento de Veículos 
<br>O ACO é frequentemente combinado com estratégias híbridas para melhorar a eficiência e evitar 
convergência prematura. Por exemplo, a estratégia de "redução dinâmica de espaço" reduz o 
espaço de busca ao longo das iterações, permitindo que o algoritmo explore soluções mais 
refinadas (Jinsi Cai et al., 2022). <br>
Além disso, operações de mutação e resfriamento simulado ajudam a diversificar a busca e 
melhorar a precisão das soluções, como no caso de problemas com múltiplos depósitos ou 
restrições temporais (Petr Stodola, 2020). <br><p>