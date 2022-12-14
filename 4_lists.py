#4 - Vetores / Listas

# 4_1
# Escreva um programa para ler um vetor de inteiros com n elementos. O valor n deve ser fornecido em tempo de execução. Retorne o maior elemento do vetor.

# Entrada:
# Um valor n;
# n valores inteiros.

# Saída:
# O maior valor no vetor lido.

n=int(input())

a=int(input())
b=int(input())

if a>b:
    maior=a
else:
    maior=b

for i in range(3,n+1):
    c=int(input())
    if maior<c:
        maior=c
print(maior)

# 4_2
# Escreva um programa para ler a nota e o nome dos alunos de uma classe, considerando n alunos. 
# Calcular a média da classe a partir da nota de seus n alunos. 
# Finalmente, escrever quais alunos conseguiram nota acima da média da classe.

# Entrada:
# Um valor n (quantidade de alunos);
# n nomes e notas de alunos.

# Exemplo:
# 5
# Ana 6 Maria 1 Paula 8 Raul 2 Vitor 3

# Saída:
# Nomes dos alunos com notas acima da média (um nome por linha).

# Exemplo:

# Ana
# Paula

n=int(input())
nomes = []
notas = []

for i in range(0,n):
    nome=input()
    nomes.append(nome)
    nota=int(input())
    notas.append(int(nota))

soma = sum(notas)
med=soma/n
for i in range(len(notas)):
    if notas[i]>med:
        print(nomes[i])    

# 4_3
# Escreva um programa que leia um valor n e então leia n números inteiros e armazene em um vetor. Ao final, o programa deve imprimir a quantidade de valores que são pares e quantidade de valores que são ímpares.

# Entrada:
# Um valor n (tamanho do vetor)
# n números inteiros (elementos vetor)

# Saída:
# Quantidade de números pares no vetor
# Quantidade de números ímpares no vetor

t= int(input())
v=[]
par=0
impar=0
for i in range(0,t):
    n=int(input())
    v.append(n)
for i in range(len(v)):
    if v[i]%2==0:
        par=par+1
    else:
        impar=impar+1
print(par)
print(impar)    

# 4_4
# Escreva um programa que leia um vetor de inteiros com n elementos. Depois some todos os valores que são vizinhos aos elementos com valor 1.
# Por exemplo, para o vetor [12, 1, 50, 60, 70, 1], o programa deve imprimir 132, que é o resultado da soma 12 + 50 + 70 (os valores vizinhos aos elementos com valor 1 no vetor.

# Entrada:
# Um valor n (quantidade de elemento do vetor);
# n inteiros

# Saída:
# Somatório dos valores vizinhos aos elementos com valor 1

t=int(input())
v=[]
sum=0

for i in range(0,t):
    n=int(input())
    v.append(n)

v.append(0)
for i in range(len(v)):
    if v[i]==1:
        a=0
        p=0
        a=v[i-1]
        p=v[i+1]
        sum=sum+a+p    
print(sum)    

# 4_5
# Escreva um programa que leia um vetor de inteiros com n elementos. Depois faça uma função que receba o vetor e duas posições i e j, e então efetue a troca dos valores das posições i e j no vetor. Importante: a função deve validar os argumentos, ou seja, se i e j são índices válidos (dentro dos limites do vetor) antes de realizar a troca. Neste exercício, o índice do primeiro elemento de um vetor é o 0 (zero). Se algum índice for inválido, não realize a troca.

# Entrada:
# Um valor n (0 <= n <= 50);
# n inteiros
# índices i e j

# Saída:
# Vetor gerado de acordo com a especificação do enunciado.

n = int(input())
v=[]

for i in range(0,n):
    a = int(input())
    v.append(a)
i = int(input())
j = int(input())

def funcao (v,i,j):
    a = v[i]
    b = v[j]
    v[i] = b
    v[j] = a
    return(v)
if j>n-1:
    for i in range(len(v)):
        print(v[i])
else:
    f=funcao(v,i,j)
    for i in range(len(f)):
        print(f[i])

# 4_6
# Escreva um programa que leia um vetor de inteiros com n elementos. Depois ordene todos os elementos em ordem crescente. Importante: não utilize funções prontas da linguagem para ordenação! Escreva o seu algoritmo de ordenação.

# Entrada:
# Um valor n (0 <= n <= 50);
# n inteiros

# Saída:
# Vetor ordenado (ordem crescente).

n = int(input())
v=[]

for i in range(0,n):
    a= int(input())
    v.append(a)

for i in range(0,n):
    for a in range(0,n):
        if v[i]<v[a]:
            valora= v[a]
            valori=v[i]
            v[a]=valori
            v[i]=valora    

for i in range(0,n):
    print(v[i])

# 4_7
# Escreva um programa que leia um vetor de inteiros com n elementos. Depois verifique se o vetor é "espelhado", ou seja, a primeira metade é igual ao inverso da segunda. Por exemplo, os vetores a seguir são "espelhados": [5 9 7 8 8 7 9 5], [1 2 3 2 1], mas o vetor [1 2 3 4 5] não é.

# Entrada:
# Um valor n (0 <= n <= 50); n inteiros

# Saída:
# Imprima "SIM" se o vetor for "espelhado" e "NAO" caso contrário (observe que não há um til no NAO)

n=int(input())
v=[]
cont=0
for i in range(0,n):
    a= int(input())
    v.append(a)
tam=n//2
for i in range(0,tam):
    a=n-1-i
    vi=v[i]
    va=v[a]
    if vi==va:
        cont=cont+1
if cont==tam:
    print("SIM")
else: 
    print("NAO")

# 4_8
# Escreva um programa que leia um vetor de inteiros com n elementos. Depois verifique se o vetor está ordenado em ordem crescente.
# Observação: após a leitura do valor n, os elementos do vetor estão todos dispostos em apenas uma linha. Por exemplo:

# 3
# 3 1 2

# Dica (Python): para ler elementos em uma mesma linha, pode ser usado o método split após a leitura. Veja exemplo a seguir:

# Entrada:
# Um valor n (0 <= n <= 50);
# n inteiros

# Saída:
# Imprima "SIM" se o vetor estiver ordenado e "NAO" caso contrário (observe que não há um til no NAO)

n = int(input())
v = [0] * n
r=0
a = input().split(" ")
for i in range(n):
    v[i] = int(a[i])

for i in range(n-1):
    a=v[i]
    b=v[i+1]
    if a>b:
        r=1
if r==1:
    print("NAO")
else:
    print("SIM")    

# 4_9
# Escreva um programa que leia dois vetores (A e B) de mesmo comprimento n. Para isso, o programa deve ler um valor inteiro n (comprimento), ler o n valores de um dos vetores e depois os n valores do outro vetor. Ao final, o programa deve imprimir "SIM" se um vetor for o resultado de uma multiplicação de todos os elementos do outro pelo mesmo valor, ou "NAO" caso contrário (não há til ~ em NAO).
# Por exemplo, considere os vetores A = [1, 2, 5, 10] e B = [3, 6, 15, 30]. Neste caso, o programa deve imprimir "SIM", pois o vetor B é resultado da multiplicação de todos os elementos de A por 3.
# Outro exemplo: considere os vetores A = [1, 2, 5, 10] e B = [3, 6, 15, 90]. Neste caso, o programa deve imprimir "NAO", pois o vetor B não é resultado da multiplicação de todos os elementos de A por um mesmo valor. Os três primeiros números foram multiplicados por 3, mas o quarto foi multiplicado por 9.
# Observação: após a leitura do valor n, os elementos de cada vetor estão todos dispostos em apenas uma linha. Por exemplo:
# 4
# 1 2 5 10
# 3 6 15 30
# Para ler elementos em uma mesma linha em Python ou em Java, pode ser usada uma estratégia similar àquela apresentada no enunciado do EP4_8 - Vetor crescente.

# Entrada
# Comprimento (n)
# n elementos do primeiro vetor
# n elementos do segundo vetor

# Saída
# SIM/NAO (dependendo se um vetor for o resultado de uma múltiplicação de todos os elementos do outro por um mesmo valor)

n = int(input())

a=[0]*n
b=[0]*n

la=input().split(" ")
lb=input().split(" ")
m=0

for i in range(0,n):
    a[i] = int(la[i])

for i in range(n):
    b[i] = int(lb[i])

div_1=b[0]/a[0]
for i in range(n):
    div=b[i]/a[i]
    if div!=div_1:
        m=1
if m==1:
    print("NAO")
else:
    print("SIM")

# 4_10
# Escreva um programa que leia um valor n e depois os n elementos de um vetor de inteiros.
# Observação: após a leitura do valor n, os elementos do vetor estão todos dispostos em apenas uma linha. Por exemplo:
# 8
# 10 5 8 5 5 36 10 9
# Para ler elementos em uma mesma linha em Python ou em Java, pode ser usada uma estratégia similar àquela apresentada no enunciado do EP4_8 - Vetor crescente.
# Depois imprima apenas a primeira ocorrência de cada número, ou seja, se um número aparece mais de uma vez no vetor, apenas a primeira ocorrência dele ser impressa.
# Por exemplo, para o vetor [10, 5, 8, 5, 5, 36, 10, 9], o programa deve imprimir (nesta ordem):
# 10 5 8 36 9

# Entrada:
# Comprimento do vetor (n);
# n inteiros

# Saída:
# Primeira ocorrência de cada número no vetor lido

n = int(input())
v=[0]*n
h=[None]*n
c=0
a=input().split(" ")

for i in range(n):
    v[i] = int(a[i])

def busca(v,n,x):
    b=False
    for i in range(0,n):
        if v[i]==x:
            b=True
    return(b)

for i in range(0,n):
    b=busca(h,n,v[i])
    if b==False:
        h[i]=v[i]
        if h[i]!=None:
            print(h[i], end=" ")
