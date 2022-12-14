#3 - Repetição


# 3_1
# Escreva um programa para ler um número inteiro positivo n e escrever os n primeiros múltiplos de 3 (e que são maiores que zero).
# Entrada:
# Um número inteiro n

# Saída:
# Os n primeiros múltiplos de 3, cada número deverá ser exibido na mesma linha, separado por um caractere espaço.

n=int(input())
c=1
mult = 3%c

while n>0:
            n=n-1
            if mult == 0:
                print(c*3," ",end="",sep="")
                c=c+1
            else:
                c=c+1    

# 3_2
# Escreva um programa que leia um inteiro n e então leia n números inteiros. Ao final, o programa deve imprimir os seguintes valores sobre a sequência de n valores lidos:

# Soma (dos n números)
# Média
# Mínimo
# Máximo


# Entrada:
# Um número inteiro n
# n números inteiros

# Saída:
# Soma
# Média (imprima com duas casas decimais após a vírgula)
# Mínimo
# Máximo

n=int(input())
s=0
med=0
mini=0
maxi=0
c=0
abacaxi=0

if n>0:
            valor=float(input())
            mini=valor
            maxi=valor
            ant=valor
            while n>0:
                valor=float(valor)
                n=n-1
                c=c+1
                s=s+valor

                med=s/c
                if valor-mini<0:
                    mini=valor

                if valor-maxi>0:
                    maxi=valor       

                if abacaxi==0:
                    valor=input()
print(int(s))
print("{:.2f}".format(med))
print(int(mini))
print(int(maxi))

# 3_3
# Uma empresa vende apenas um produto e recebe diversos pedidos. A medida que os pedidos chegam, a empresa verifica se tem estoque para atender o pedido e entrega o pedido completo. Caso a empresa não tenha estoque para atender o pedido integral, o pedido não é atendido (ou seja, a empresa não faz entrega parcial). Por exemplo, se a empresa tem 50 unidades em estoque e recebe um pedido de 80 unidades, a empresa não entrega nenhuma unidade (nem as 50 que possui em estoque).
# Escreva um programa para contar quantos pedidos são atendidos nesta empresa. O programa deve ler a quantidade em estoque inicial, um inteiro n e então lerá a quantidade requisitada por n pedidos.

# Entrada:
# Quantidade em estoque
# Um número inteiro n
# n quantidades solicitadas (sobre os n pedidos realizados)

# Saída:
# Quantidade de pedidos atendidos

q =int(input())
n=int(input())

c = 0
v = 0

if n>0:

    while n>0:
        p=int(input())
        if p<=q:
            v=v+1
            c=c+1
            q=q-p

            n=n-1
        else:
            c=c+1
            n=n-1          
print(v)        

# 3_4
# Faça um programa que leia um inteiro n e imprima um "triângulo" com os números. Por exemplo, para n=8, a saída seria:

# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888

# Entrada:
# Um número inteiro n.

# Saída:
# Triângulo com os números.

n=int(input())
num=0
cont=0

while num!=n:
            num=num+1
            c=0
            while c!=num:
                if c+1==num:
                    print(num,"",sep="")
                    c=c+1
                    cont=cont+1
                else:
                    print(num,"",end="",sep="")
                    c=c+1
                    cont=cont+1   

# 3_5
# Faça um programa que fique lendo números do usuário até que ele digite 0. Quando isso ocorrer, mostre o valor da soma de todos os números lidos.

# Entrada:
# Uma sequência de números inteiros. A leitura é encerrada quando o usuário digitar 0 (zero).

# Saída:
# Soma de todos os valores lidos.

n=int(input())
soma=0

while n!=0:
            soma=soma+n
            n=int(input())
if n==0:
            print(soma)

# 3_6
# Faça um programa que leia um valor inteiro n e então calcule o valor de f( n ), conforme definição a seguir:

# Entrada:
# Valor inteiro n.

# Saída:
# Valor de f( n ).

n=int(input())
f=0
i=1
j=0
func1=0
func2=0
s1=0
s2=0

while j<=8:
            j=j+1
            func1=(i+1)*j
            s1=s1+func1

            if j==8:
                func2=func2+s1
                s1=0
                j=0
                if i<n:
                    i=i+1
                else:
                    break

print(func2)

# 3_7
# Faça um programa que fique lendo números do usuário até que ele digite 0 . Quando isso ocorrer, mostre quantos números são múltiplos de 3 e quantos são múltiplos de 5.

# Entrada:
# Uma sequência de números inteiros. A leitura é encerrada quando o usuário digitar 0 (zero).

# Saída:
# Quantidade de múltiplos de 3 digitados;
# Quantidade de múltiplos de 5 digitados.

n=int(input())
m3=0
m5=0

while n!=0:
            mult3 = n%3
            mult5 = n%5
            if mult3 == 0:
                m3=m3+1
            if mult5 == 0:
                m5=m5+1    
            n=int(input())
if n==0:
            print(m3,m5)

# 3_8
# Faça um programa que leia um valor inteiro N e então mostre os N primeiros números primos (o primeiro número primo é o 2).

# Entrada:
# Valor inteiro N.
# Exemplo:
# 5

# Saída:
# N primeiros números primos.

# Exemplo:
# 2
# 3
# 5
# 7
# 11

n=int(input())
c=0
number=1
i=0
count=0

while c<=n:
            while i<100:
                i=i+1
                resto = number%i
                if resto == 0:
                    count=count+1
            while i==100:
                if count==2:
                    print(number)
                    c=c+1
                i=0
                count=0
                number=number+1        

# 3_9
# Faça um programa que leia um valor inteiro N e então imprima em linhas separadas seus dígitos na ordem inversa. Por exemplo: O número 9376 seria impresso como:

# 6
# 7
# 3
# 9

# Entrada:
# Valor inteiro N.

# Saída:
# Dígitos do número, impressos linha a linha, em ordem inversa

num= int(input())
bi = (num%100000000)//10000000
cMilhar = (num%10000000)//1000000
dMilhar = (num%1000000)//100000
uMilhar = (num%100000)//10000
Milhar = (num%10000)//1000
Centena = (num%1000)//100
Dezena = (num%100)//10
Unidade = num%10

Milhar=str(Milhar)
Centena=str(Centena)
Dezena=str(Dezena)
Unidade=str(Unidade)
print(Unidade)
print(Dezena)
print(Centena)
print(Milhar)
print(uMilhar)
print(dMilhar)
print(cMilhar)
print(bi)

# 3_10
# Faça um programa que leia um valor inteiro N que representa a quantidade de linhas para impressão de uma pirâmide de números 1. A figura impressa é composta apenas pelos caracteres hífen (-) e o número 1. Por exemplo, uma pirâmide com altura 5 deve ser representada da seguinte forma:
# ----1----
# ---111---
# --11111--
# -1111111-
# 111111111

# Entrada:
# Quantidade de linhas (altura) da pirâmide

# Saída:
# Pirâmide

n = int(input())

ctot=2*(n-1)+1


for p in range(1,ctot+1,2):
    a=0
    b=p
    while a!=((ctot-p)/2):
        print("-",end="")
        a=a+1
    while p>0:
        print("1",end="")
        p=p-1
    a=0
    while a!=((ctot-b)/2):
        print("-",end="")
        a=a+1

    if p ==0:
        print()
