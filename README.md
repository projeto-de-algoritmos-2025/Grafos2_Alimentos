# Grafos2_Alimentos

**Número da Lista**: 2<br>
**Conteúdo da Disciplina**: Grafos 2<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 22/2022000 |  Milena Fernandes Rocha |
| 20/2045348  |  Ingrid Alves Rocha |

## Sobre 
O objetivo deste projeto é treinar e aprofundar a compreensão dos algoritmos de Strongly Connected Components (SCC) e Dijkstra, estudados nas últimas semanas. Para isso, o projeto propõe a implementação prática desses algoritmos e a resolução de questões selecionadas da plataforma LeetCode, que apresentam desafios relevantes e aplicados. Essa abordagem permite reforçar o aprendizado teórico por meio da prática, além de desenvolver a capacidade de resolução de problemas em contextos variados.

## Screenshots

![2360](./screenshots/2360.png)

## Instalação 
**Linguagem**: Python<br>
**Sites**: LeetCode<br>
<br>

Aqui está a explicação corrigida e mais concisa:

---

### Questão 2360 - [Longest Cycle in a Graph](https://leetcode.com/problems/longest-cycle-in-a-graph/description/)

* **Solução:** [2360](./Questoes/2360.py)
* **Nível:** Hard
* **Conteúdo usado:** DFS Numbering

**Explicação:**

O **DFS Numbering** é uma técnica utilizada para explorar grafos e detectar ciclos. Durante a execução do DFS, cada nó recebe um número de visitação, o que ajuda a rastrear a ordem em que os nós são visitados.
Quando um nó é visitado, seu número de visitação é registrado. Se, ao explorar um vizinho, descobrirmos que ele já foi visitado (ou seja, seu número de visitação não é mais -1), um ciclo foi encontrado. A diferença entre o número de visitação do nó atual e o vizinho revela o tamanho do ciclo.
No código, o array `visit_id` armazena os números de visitação. O mapa `tmap` é usado para rastrear os nós visitados durante o processo de DFS, e a comparação dos números de visitação é crucial para identificar ciclos.

**Resumo:** O **DFS Numbering** permite identificar ciclos ao registrar a ordem de visitação dos nós e calcular o tamanho do ciclo com base nos números de visitação.







