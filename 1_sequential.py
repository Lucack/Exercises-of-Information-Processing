#1 - Sequencial

#1_1 
#Escreva um programa que mostre a mensagem "Alo, mundo!" (observe que não há acentuação na mensagem).


print("Alo, mundo!")

#1_2
#Escreva um programa que leia 3 notas e calcule a média (aritmética).

nota1=int(input())
nota2=int(input())
nota3=int(input())
soma= nota1 + nota2 + nota3
media= soma/3
print("{:.2f}".format(media))



#1_3
#Escreva um programa que leia dois números inteiros A e B, e então imprima o resultado das seguintes operações matemáticas:

# Soma (A + B)
# Subtração (A - B)
# Multiplicação (A x B)
# Divisão (A / B)
# Divisão inteira (A / B)
# Resto da divisão A / B

a= int(input())
b= int(input())
soma= a+b
print(soma)
sub= a-b
print(sub)
mult= a*b
print(mult)
div= a/b
print(div)
divint= a//b
print(divint)
resto= a%b
print(resto)


#1_4
#Sejam A e B dois pontos quaisquer no plano cartesiano, representados por um par de coordenadas (x, y). A menor distância entre A e B é um segmento de reta que tem os dois pontos como extremidade.
#Representando as coordenadas de A pelo par(Ax, Ay), e as coordenadas de B pelo par (Bx, By), podemos calcular essa distância pela equação:
#Escreva um programa que receba as coordenadas de dois pontos A e B e calcule a distância entre eles.



Ax=int(input())
Ay=int(input())
Bx=int(input())
By=int(input())
import math
dist= math.sqrt((Bx-Ax)**2+(By-Ay)**2)
print("{:.2f}".format(dist))


#1_5
#Bits de paridade podem ser usados para verificar, por exemplo, possíveis erros durante a transmissão de uma sequência de bits. O bit de paridade é um bit adicionado a uma sequência de bits de forma a tornar a contagem de 1s ímpar (paridade ímpar) ou par (paridade par). Por exemplo, para a sequência de bits 1011110, ao adicionar um bit paridade (para paridade par), o valor desse bit seria 1. Se esse bit ficar no final da sequência, a sequência final é 10111101 (obverse que agora a quantidade de bits com valor 1 é par).
#Se a quantidade de bits já for par, então, o valor do bit de paridade (para paridade par) seria 0. Por exemplo: para a sequência 1110100, a sequência com o bit de paridade no final fica 11101000.
#Escreva um programa que leia 7 valores (cada um representa o valor de 1 bit de uma sequência de 7 bits). O programa de imprimir o valor do bit paridade para a sequência lida (considere paridade par).

#Entrada:
#A entrada consiste de 7 valores, cada um representa o valor de 1 bit (um valor por linha). Por exemplo:
#1
#0
#1
#1
#1
#1
#0
#Saída:
#Valor do bit de paridade (para paridade par): 0 ou 1

bit1= int(input())
bit2= int(input())
bit3= int(input())
bit4= int(input())
bit5= int(input())
bit6= int(input())
bit7= int(input())

num= bit1+bit2+bit3+bit4+bit5+bit6+bit7
resto= num%2

if(resto==0):
	print("Valor do bit de paridade (para paridade par): 0")
else:
	print("Valor do bit de paridade (para paridade par): 1")


#1_6
#Uma loja aplica descontos anunciando da seguinte forma: 10% + 10%. Ou seja, primeiro reduz o valor total em 10% e depois reduz mais 10% sobre o total já descontado. Escreva um programa que receba o valor de um produto e imprima o valor após o desconto 10% + 10%.
#Por exemplo, para o valor 50, após o desconto, o valor será 40,50
#Entrada:
#Valor total

#Saída:
#Valor com o desconto (utilize duas casas decimais)

valor= int(input())
desc= (valor*(1-0.1))*(1-0.1)
print(desc)

# 1_7
# Um determinado método para encriptar números de 4 dígitos consiste em adicionar 1 em cada dígito do número. Por exemplo:
# O número 1234 ficaria 2345 após a encriptação;
# O número 9092 ficaria 0103 após a encriptação.


# Entrada:
# Número a ser encriptado

# Saída:
# Número encriptado

num= int(input())

Milhar = (num%10000)//1000
Centena = (num%1000)//100
Dezena = (num%100)//10
Unidade = num%10

if (Milhar==9):
    Milhar=0
else:
    Milhar=Milhar+1

if (Centena==9):
    Centena=0
else:
    Centena=Centena+1

if (Dezena==9):
    Dezena=0
else:
    Dezena=Dezena+1

if (Unidade==9):
    Unidade=0
else:
    Unidade=Unidade+1
Milhar=str(Milhar)
Centena=str(Centena)
Dezena=str(Dezena)
Unidade=str(Unidade)
print(Milhar+Centena+Dezena+Unidade)

# 1_8
# Um caminhão de carga possui uma capacidade máxima, medida em Kg. Para carregar o caminhão, os itens que serão transportados são guardados em caixas de transporte. Há caixas de diversas capacidades: Tipo A: 500Kg, Tipo B: 100Kg, Tipo C: 25Kg e Tipo D: 1Kg.
# Ao sair do depósito, um caminhão deve estar cheio, ou seja, com a carga ocupando 100% da sua capacidade máxima. Quanto menor a quantidade de caixas usadas, mais rapidamente o caminhão pode sair do depósito. Por exemplo, um caminhão com capacidade de 400Kg, será carregado mais rapidamente com 4 caixas de 100Kg do que com 400 caixas de 1Kg.
# Escreva um programa que receba a capacidade máxima de um caminhão. Após isso, retorne qual a melhor composição de tamanhos de caixa para esse caminhão.

# Entrada:
# Capacidade máxima do caminhão

# Exemplo:
# 550

# Saída:
# Quatro números inteiros (indicando a melhor combinação de caixas):
# Quantidade de caixas de 500Kg
# Quantidade de caixas de 100Kg
# Quantidade de caixas de 25Kg
# Quantidade de caixas de 1Kg

# Exemplo:

# 1
# 0
# 2
# 0

cap = int(input())
c500= cap//500
print(c500)
c100= (cap-(c500*500))//100
print(c100)
c25= (cap-(c500*500+c100*100))//25
print(c25)
c1 = (cap-(c500*500+c100*100+c25*25))//1
print(c1)

# 1_9
# 1KB = 1000 bytes ou 1KB = 1024 bytes?
# Sobre este tema, há um padrão definido pelo IEC para unidades de medida. Alguns desses casos são mostrados a seguir:
# A partir dessas tabelas, a resposta para a pergunta inicial é 1kB = 1000 bytes. Entretanto, na indústria de software, frequentemente considera-se 1024 bytes.
# Para valores menores, a diferença entre usar o padrão com potências de 2 e de 10 pode ser pequena. Entretanto, para valores maiores, essa diferença pode significar alguns GBs (ou GiBs).
# Escreva um programa que leia o espaço ocupado por um arquivo (em GB) e imprima:
# o tamanho do arquivo em bytes se o valor informado significa GB (pelo padrão IEC)
# o tamanho do arquivo em bytes se o valor informado significa GiB (pelo padrão IEC)
# módulo da diferença entre os dois tamanhos em bytes

# Importante: os valores podem ser grandes, portanto, tenha atenção na escolha do tipo de dados. 

# Entrada:
# Tamanho do arquivo em GB (número inteiro)

# Saída:
# o tamanho do arquivo em bytes se o valor informado significa GB (pelo padrão IEC)
# o tamanho do arquivo em bytes se o valor informado significa GiB (pelo padrão IEC)
# módulo da diferença entre os dois tamanhos em bytes

gb= int(input())
k=gb*10**9
print(k)
ki= gb*2**30
print(ki)
dif=ki-k
print(dif)


# 1_10
# A área de Aprendizado de Máquina tem crescido bastante nos últimos anos. Uma tarefa importante nesse contexto é a classificação. Algoritmos de classificação são capazes de aprender a partir de experiência prévia (e.g. dados históricos). Os classificadores podem então realizar predições para novos dados. Por exemplo, um algoritmo de classificação pode aprender a partir de e-mails antigos e se eles foram classificados como spam ou não spam pelos usuários. Depois, o classificador treinado poderá predizer se novos e-mails são spam ou não. Esse também é um exemplo de classificação binária, em que há duas classes possíveis: spam ou não spam.
# O desempenho de classificadores binários pode ser medido utilizando uma série de métricas. Nesse contexto, existe um conceito conhecido como matriz de confusão. Essa matriz é preenchida com a contagem de predições corretas e incorretas realizadas pelo classificador. A matriz de confusão tem o seguinte formato:
# Nessa matriz, positiva e negativa representam as duas classes. No caso do spam, a classe positiva poderia representar classificar um e-mail como spam e a negativa classificar como não spam. Os valores na matriz são:
# VP: número de vezes que exemplos positivos foram classificados corretamente como positivos
# FN: número de vezes que exemplos positivos foram classificados de forma incorreta como negativos
# FP: número de vezes que exemplos negativos foram classificados de forma incorreta como positivos
# VN: número de vezes que exemplos negativos foram classificados corretamente como negativos


# Com base nos valores na matriz de confusão, podem ser calculadas métricas para avaliação de desempenho. Algumas dessas métricas são apresentadas a seguir:

# No exemplo apresentado:
# Acurácia = (40 + 35) / (40 + 35 + 15 + 10) = 0,75
# Precisão = 40 / (40 + 15) = 0,73
# Sensibilidade = 40 / (40 + 10) = 0,80

# Escreva um programa que leia os valores VP, FN, FP e VN e então imprima o valor das métricas acurácia, precisão e sensibilidade.

# Entrada
# Valor de VP (inteiro)
# Valor de FN (inteiro)
# Valor de FP (inteiro)
# Valor de VN (inteiro)

# Saída
# Acurácia
# Precisão
# Sensibilidade

# Observação: imprima todos os valores com duas casas decimais após a vírgula

VP=int(input())
FN=int(input())
FP=int(input())
VN=int(input())

Acurácia = (VP+VN)/(VP+VN+FP+FN)
print("{:.2f}".format(Acurácia))
Precisão = VP/(VP+FP)
print("{:.2f}".format(Precisão))
Sensibilidade = VP/(VP+FN)
print("{:.2f}".format(Sensibilidade))