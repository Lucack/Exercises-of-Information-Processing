#5 - Matrizes


# 5_1
# Escreva um programa que leia uma matriz para armazenar as C notas de uma turma e calcular a média de cada um dos L alunos. Portanto, será lida uma matriz com L linhas (uma para cada aluno) e C colunas (cada coluna terá uma nota).
# Para ler a matriz, primeiro será informado o número de linhas e depois o número de colunas. Após a leitura das dimensões da matriz, os elementos de cada linha da matriz estão dispostos linha por linha. Por exemplo (as duas primeiras linhas são as dimensões da matriz: número de linhas (2) e número de colunas(3)):
# 2
# 3
# 6 9 6
# 7 8 9
# Após isso, calcule a média (aritmética) das C notas para cada aluno e adicione a coluna C+1 com a média. Após isso, imprima a matriz completa, com L linhas e C+1 colunas.
# Dica (Python): exemplo de código para ler os elementos de uma matriz no formato descrito no enunciado:

# CODIGO DE AJUDA
# n_linhas = int(input())
# n_colunas = int(input())
# matriz = [[0 for c in range(n_colunas)] for l in range(n_linhas)]
# for linha in range(n_linhas):
#     itens_linha = input().split(" ")
#     for coluna in range(n_colunas):
#         matriz[linha][coluna] = float(itens_linha[coluna])     

# Entrada:
# L (número de alunos)
# C (quantidade de notas)
# Elementos da matriz
# Exemplo:

# 2
# 3
# 6 9 6
# 7 8 9

# Saída:
# Matriz com dimensões L x C+1
# Observação: Imprima os valores da matriz com duas casas decimais.

# Exemplo:

# 6.00 9.00 6.00 7.00
# 7.00 8.00 9.00 8.00

n_linhas = int(input())
n_colunas = int(input())
s=0
matriz = [[0 for c in range(n_colunas + 1)] for l in range(n_linhas)]
for linha in range(n_linhas):
    itens_linha = input().split(" ")

    for coluna in range(n_colunas):
        matriz[linha][coluna] = float(itens_linha[coluna])
        s=s+(float(itens_linha[coluna]))
    if n_colunas-1 == coluna:
        med=s/n_colunas
        matriz[linha][coluna+1] = med
        s=0

for i in range(n_linhas):
    for j in range(n_colunas+1):
        m=matriz[i][j]
        if j == n_colunas:
            print(f"{m:.2f}",end=" \n")

        else:
            print(f"{m:.2f}",end=" ")

# 5_2
# Escreva um programa que leia uma matriz com L linhas e C colunas.
# Para ler a matriz, primeiro será informado o número de linhas e depois o número de colunas. Após a leitura das dimensões da matriz, os elementos de cada linha da matriz estão dispostos linha por linha. Por exemplo (as duas primeiras linhas são as dimensões da matriz: número de linhas (2) e número de colunas(3)):
# 2
# 3
# 5 6 2
# 7 2 1
# Dica (Python): exemplo de código para ler os elementos de uma matriz no formato descrito no enunciado:

#  CODIGO DE AJUDA
# n_linhas = int(input())
# n_colunas = int(input())
# matriz = [[0 for c in range(n_colunas)] for l in range(n_linhas)]
# for linha in range(n_linhas):
#     itens_linha = input().split(" ")
#     for coluna in range(n_colunas):
#         matriz[linha][coluna] = int(itens_linha[coluna])    

# Depois de ler a matriz, multiplique por 3 todos os elementos nas colunas de índice ímpar na matriz (considere que a primeira coluna tem índice 0, a segunda tem índice 1, e assim por diante). Ao final, imprima a matriz obtida.

# Por exemplo, para o caso da matriz a seguir:

# 10 20 30 40
# 11 22 33 44
# 40 30 20 10

# O programa deve imprimir a seguinte matriz (em cada linha impressa, há um caractere espaço entre cada número impresso):

# 10 60 30 120
# 11 66 33 132
# 40 90 20 30


# Entrada
# Número de linhas da matriz
# Número de colunas da matriz
# Valores dos elementos da matriz

# Saída
# Matriz com os valores das colunas de índice ímpar multiplicados por 3

l=int(input())
c=int(input())
m=[[0 for i in range(c)]for i in range(l)]

for i in range(l):
    a=input().split(" ")
    for j in range(c):
        m[i][j]=int(a[j])
        if j%2!=0:
            m[i][j]=3*(m[i][j])

for i in range(l):
    for j in range(c):
        print(m[i][j],end=" ")
        if j==c-1:
            print()

# 5_3
# Escreva um programa que leia as dimensões de uma matriz e então imprima uma matriz que contém uma sequência de números ordenados linha a linha formando um zig-zag. Exemplo para uma matriz com 4 linhas e 3 colunas:

# Entrada:
# L (número de linhas)
# C (número de colunas)

# Exemplo:

# 3
# 5

# Saída:
# Matriz com dimensões L x C com os múltiplos de 10 (em cada linha impressa, há um caractere espaço entre cada número impresso)

# Exemplo:
# 1 2 3 4 5
# 10 9 8 7 6
# 11 12 13 14 15


l=int(input())
c=int(input())

count=0

m=[[0 for i in range(c)]for i in range(l)]
for i in range(l):
    for j in range(c):
        count = count + 1
        if i%2==0:
            m[i][j] = count
        else:
            m[i][(c-1)-j] = count

for i in range(l):
    for j in range(c):
        print(m[i][j],end=" ")
        if j==c-1:
            print()

# 5_4
# Escreva um programa que leia uma matriz com n linhas e m colunas. Após isso, ordene os elementos em cada linha (ordem crescente). Importante: não utilize funções prontas da linguagem para ordenação! Escreva o seu algoritmo de ordenação.
# Para ler a matriz, primeiro será informado o número de linhas e depois o número de colunas. Após a leitura das dimensões da matriz, os elementos de cada linha da matriz estão dispostos linha por linha. Por exemplo (as duas primeiras linhas são as dimensões da matriz: número de linhas (2) e número de colunas(3)):
# 2
# 3
# 5 6 2
# 7 2 1

# Dica para Python ou Java: a leitura dos elementos da matriz da forma descrita aqui pode ser realizada com uma estratégia similar àquela apresentada no enunciado dos dois primeiros exercícios sobre matrizes (EP5_1 e EP5_2).

l=int(input())
c=int(input())
result=0
m=[[0 for i in range(c)]for i in range(l)]

for i in range(l):
    valores=input().split(" ")
    for j in range(c):
        m[i][j] = int(valores[j]) 
def crescente(matriz,linha):
    v=matriz[linha]
    tam=len(matriz[0])
    for i in range(tam):
        for a in range(tam):
            if v[i]<v[a]:
                maior= v[a]
                menor= v[i]
                v[a]=menor
                v[i]=maior
    return(v)
for i in range(l):
    resultado=crescente(m,i)
    for j in range(c):
        m[i][j]=resultado[j]
        print(m[i][j],end=" ")
    print()

# 5_5
# Escreva um programa que leia uma matriz com dimensões n x n. Depois, calcule a soma de todos os valores pares abaixo da diagonal principal.
# Para ler a matriz, primeiro será informada a dimensão n. Após isso, os elementos de cada linha da matriz estão dispostos linha por linha. Por exemplo (a primeira linha é o valor de n):
# 3
# 6 3 2
# 7 8 9
# 2 8 1

# Dica para Python ou Java: a leitura dos elementos da matriz da forma descrita aqui pode ser realizada com uma estratégia similar àquela apresentada no enunciado dos dois primeiros exercícios sobre matrizes (EP5_1 e EP5_2).

# Entrada:
# n
# Dados da matriz
# Exemplo:
# 3
# 6 3 2
# 7 8 9
# 2 8 1


# Saída:
# Soma dos valores pares abaixo da diagonal principal.

n = int(input())
m=[[0 for c in range(n)]for l in range(n)]
s=0
for i in range(0,n):
    valores= input().split(" ")
    for j in range(0,n):
        m[i][j]= int(valores[j])
        if int(valores[j])%2==0 and j<i:
            s=s+int(valores[j])
print(s)

# 5_6
# Escreva um programa que leia uma matriz de dimensões n x n (assuma que n é par). Após isso, imprima o resultado da matriz dobrada da seguinte forma:
# Para ler a matriz, primeiro será informada a dimensão n. Após isso, os elementos de cada linha da matriz estão dispostos linha por linha. Por exemplo (a primeira linha é o valor de n):
# 3
# 6 3 2
# 7 8 9
# 2 8 1
# Dica para Python ou Java: a leitura dos elementos da matriz da forma descrita aqui pode ser realizada com uma estratégia similar àquela apresentada no enunciado dos dois primeiros exercícios sobre matrizes (EP5_1 e EP5_2).

# Entrada:
# n
# Dados da matriz

# Saída:
# Matriz após as dobras

n = int(input())
m=[[0 for c in range(n)]for l in range(n)]
for i in range(0,n):
    valores= input().split(" ")
    for j in range(0,n):
        m[i][j]= int(valores[j])

met=n//2
for i in range(0,n):
    for j in range(0,n):
        if j>=met:
            m[i][(met-(j-met)-1)]=m[i][(met-(j-met)-1)]+m[i][j]
for i in range(0,n):
    for j in range(0,n):
        if i>=met:
            m[(met-(i-met)-1)][j]=m[(met-(i-met)-1)][j]+m[i][j]


for i in range(0,met):
    for j in range(0,met):
        print(m[i][j],end=" ")
    print()

# 5_7
# Escreva um programa que leia um valor n e então imprima uma matriz de tamanho n x n de acordo com o exemplo a seguir (veja que os números seguem uma ordem):
# Para n = 5:
# 1 2 3 4 5
# 2 3 4 5 6
# 3 4 5 6 7
# 4 5 6 7 8
# 5 6 7 8 9


# Entrada:
# n (inteiro)

# Saída:
# Matriz n x n de acordo com a especificação do enunciado

n = int(input())
m=[[0 for i in range(n)]for j in range(n)]
for i in range(n):
    for j in range(n):
        m[i][j]=i+j+1
        if j!=n-1:
            print(m[i][j],end=" ")
        else: 
            print(m[i][j],end=" ")
            print()

# 5_8
# Escreva um programa que leia duas matrizes: A e B. Depois mostre o resultado da seguinte operação: 3 x A x B.
# Observação: após a leitura das dimensões de uma matriz, os elementos de cada linha da matriz estão dispostos linha por linha. Por exemplo (as duas primeiras linhas são as dimensões da matriz: número de linhas (2) e número de colunas(3)):
# 2
# 3
# 5 6 2
# 7 2 1


# Dica para Python ou Java: a leitura dos elementos das matrizes da forma descrita aqui pode ser realizada com uma estratégia similar àquela apresentada no enunciado dos dois primeiros exercícios sobre matrizes (EP5_1 e EP5_2).

# Entrada:
# Número de linhas da matriz A
# Número de colunas da matriz A
# Elementos da matriz A
# Número de linhas da matriz B
# Número de colunas da matriz B
# Elementos da matriz B

# Saída:
# Matriz resultado da operação 3 x A x B, isto é, o escalar 3 que multiplica a matriz AxB.

#criando matriz a
la= int(input())
ca= int(input())
a=[[0 for i in range(ca)]for j in range(la)]
for i in range(la):
    valores=input().split(" ")
    for j in range(ca):
        a[i][j]= int(valores[j])

#criando matriz b       
lb= int(input())
cb= int(input())
b=[[0 for i in range(cb)]for j in range(lb)]
for i in range(lb):
    valores=input().split(" ")
    for j in range(cb):
        b[i][j]= int(valores[j])

#processamento AxB

m=[[0 for i in range(cb)]for j in range(la)] # m:  matriz resultado A(linha)xB(coluna)

for i in range(la):
    for j in range(cb):
        for n in range(0,ca):
            m[i][j]=m[i][j]+a[i][n]*b[n][j]

for i in range(la):
    for j in range(cb):
        m[i][j]=3*m[i][j]
        print(m[i][j],end=" ")
    print()

# 5_9
# Escreva um programa que leia uma matriz e então verifique se a matriz possui somente múltiplos de 10 e se cada uma das linhas está ordenada (seja em ordem crescente ou decrescente).
# Observação: após a leitura das dimensões da matriz, os elementos de cada linha da matriz estão dispostos linha por linha. Por exemplo (as duas primeiras linhas são as dimensões da matriz: número de linhas (2) e número de colunas(3)):
# 2
# 3
# 5 6 2
# 7 2 1

# Dica para Python ou Java: a leitura dos elementos da matriz da forma descrita aqui pode ser realizada com uma estratégia similar àquela apresentada no enunciado dos dois primeiros exercícios sobre matrizes (EP5_1 e EP5_2).

# Entrada:
# L (número de linhas)
# C (número de colunas)
# Elementos da matriz

# Saída:
# Imprima "SIM" se a matriz atende ao critério e "NAO" caso contrário (observe que não há um til no NAO)

# Exemplo:
# SIM
# Neste exemplo, a saída foi sim, pois todos os valores são múltiplos de 10 e todas as linhas estão ordenadas (a primeira linha em ordem decrescente, e as outras duas linhas em ordem crescente)

l = int(input())
c = int(input())
r=True
cresc=False
dec=False
m=[[0 for i in range(c)]for j in range(l)]
for i in range(l):
    valores=input().split(" ")
    for j in range(c):
        m[i][j]=int(valores[j])
        conta=m[i][j]%10
        if conta!=0:
            r=False
if r:
    for i in range(l):
        if m[i][0]<m[i][2]:
            cresc=True
            for j in range(c-1):
                if m[i][j+1]<m[i][j]:
                    r=False
        else:
            dec=True
            for j in range(c-1):
                if m[i][j+1]>m[i][j]:
                    r=False
if r:
    print("SIM")
else:
    print("NAO")            

# 5_10
# Escreva um programa que leia uma matriz que contém o mapa de um campo minado. Nesta matriz, o valor 1 indica que há uma bomba na célula e o valor 0 indica que não há uma bomba na célula. A matriz é composta apenas pelos valores 0 e 1. Exemplo de mapa do campo minado seguindo esse formato:
# Observação: após a leitura das dimensões da matriz, os elementos de cada linha da matriz estão dispostos linha por linha. Por exemplo (as duas primeiras linhas são as dimensões da matriz: número de linhas (2) e número de colunas(3)):
# 2
# 3
# 1 0 1
# 0 0 1

# Dica para Python ou Java: a leitura dos elementos da matriz da forma descrita aqui pode ser realizada com uma estratégia similar àquela apresentada no enunciado dos dois primeiros exercícios sobre matrizes (EP5_1 e EP5_2).

# Após ler a matriz com o mapa, o programa irá ler as coordenadas de uma célula (linha e coluna) e então deverá imprimir quantas bombas há na vizinhança da célula (desconsiderando a própria célula). Por exemplo, para o mapa apresentado anteriormente, na célula (linha=2; coluna=3), há 3 bombas na vizinhança. Portanto, o programa deverá imprimir o valor 3 neste caso.
# Importante: considere que os índices das linhas e colunas iniciam no zero. Portanto, a coluna 2 é a terceira coluna na matriz, assim como a linha 3 é a quarta linha na matriz.

# Entrada
# Quantidade de linhas na matriz
# Quantidade de colunas na matriz
# Valores da matriz (mapa do campo minado)
# Linha da célula a ser consultada
# Coluna da célula a ser consultada

# Saída
# Quantidade de bombas na vizinhança da célula

l = int(input())
c = int(input())
m=[[0 for i in range(c)]for j in range(l)]
for i in range(l):
    valores=input().split(" ")
    for j in range(c):
        m[i][j]=int(valores[j])

ci=int(input())
cj=int(input())

def somar_vizinhos(matriz, linha, coluna):
    s=-matriz[linha][coluna]
    l=len(matriz)-1
    c=len(matriz[0])-1
    for i in range(linha-1,linha+2):
        for j in range(coluna-1,coluna+2):
            if 0<linha<l and 0<coluna<c:
                s=s+matriz[i][j]
            elif (linha==0 or linha ==l) or (coluna==0 or coluna==c):
                if (0<=i<=l) and (0<=j<=c):
                    s=s+matriz[i][j]
    return(s)
print(somar_vizinhos(m,ci,cj))
