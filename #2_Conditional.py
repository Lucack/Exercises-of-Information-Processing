#2 - Condicional

# 2_1
# Escreva um programa que leia as notas de duas avaliações e imprima a média final (MF); Se a média for maior ou igual a 5, imprima “APROVADO” e encerre o programa.
# Entretanto, se a média final for menor que 5, leia uma terceira nota (REC). A média com recuperação (MR) então será (MF + REC) / 2. Imprima a média com recuperação.  Se a média com recuperação for maior ou igual a 5, imprima “APROVADO” e, caso contrário, imprima “REPROVADO”. 

# Entrada:
# Nota da avaliação 1
# Nota da avaliação 2
# Nota da REC (será solicitada apenas se MF < 5)

# Saída:
# Média final
# Média com recuperação (apenas quando MF < 5)
# APROVADO/REPROVADO
# Observação: Mostre as médias com apenas duas casas decimais.

      p1 = int(input())
      p2 = int(input())
      MF = (p1+p2)/2
      print("{:.2f}".format(MF))
      if (MF >= 5):
          print("APROVADO")
      elif (MF<5):
          REC = int(input())
          MR= (MF+REC)/2
          print("{:.2f}".format(MR))
          if (MR >=5):
              print("APROVADO")
          else:
              print("REPROVADO")
    
 

# 2_2
# Uma empresa contratou diversos vendedores. Para cada um deles, a empresa paga um salário fixo mais 20% de comissão sobre o total de vendas realizadas pelo vendedor. Por exemplo, um vendedor com salário fixo de 2000,00 e que vendeu 3500,00, receberá 2700,00 (sendo 700,00 de comissão).
# Neste mês, a empresa definiu como meta que os vendedores devem vender o suficiente para pelo menos obter uma comissão de 50% de seu salário fixo. Por exemplo, para o caso do vendedor que recebe 2000,00 de salário, ele deve vender pelo menos o suficiente para obter 1000,00 de comissão.
# Escreva um programa que leia o salário fixo do vendedor e o total de vendas realizadas no mês. O programa então irá imprimir o valor da comissão e o texto "Atingiu meta de vendas" (se a meta de vendas foi atingida) ou "Nao atingiu meta de vendas" (se a meta de vendas não foi atingida).

# Entrada:
# Salário fixo do vendedor
# Soma das vendas realizadas pelo vendedor no mês

# Saída:
# Comissão (imprima o valor com duas casas decimais após a vírgula)
# Atingiu meta de vendas/Nao atingiu meta de vendas
# Observação: Não há um ~ "til" na palavra "Nao" na saída do programa.

      sfixo= int(input())
      tvendas= int(input())
      com= (tvendas*(0.2))
      print("{:.2f}".format(com))
      esperado= (sfixo)/2
      if (com >= esperado):
          print("Atingiu meta de vendas")
      else:
          print("Nao atingiu meta de vendas")

# 2_3


# Foi encontrado um dispositivo que possui um sistema que mostra as seguintes  mensagens, dependendo da temperatura medida: Muito Baixa, Baixa, Normal, Alta e Muito Alta. O dispositivo usa as faixas exibidas na figura a seguir:
# Escreva um programa que leia o valor da temperatura e mostre qual a mensagem que seria exibida. 

# Entrada:
# Valor da temperatura.

# Saída:
# Mensagem (de acordo com a temperatura).

        temp= int(input())
        if (temp <= -20):
            print("Muito Baixa")
        elif (temp >-20 & temp <= 30):
            print("Baixa")
        elif (30 < temp <= 200):
            print("Normal")
        elif (200 < temp <= 250):
            print("Alta")
        else:
            print("Muito Alta")


# 2_4
# Uma montadora de discos voadores possui filiais em diversos planetas. Recentemente, a empresa enviou um comunicado a todos os seus clientes sobre a necessidade de realização de revisão em alguns discos voadores, conforme a tabela a seguir:
# Ano de produção	Motor principal e distância percorrida	Requer revisão?
# 1901 a 2000	Caso use os motores principais 100 ou 101, independentemente da distância percorrida	 SIM
# 2001 a 2020	Independemente do motor, caso a distância percorrida seja maior que 5000 anos-luz	 SIM
# 2021	Caso use os motores principais 200 ou 201, e tenha percorrido uma distância maior que 200 anos-luz	 SIM
# Todos os demais casos não necessitam de revisão no momento.
# Escreva um programa que leia o ano de produção do disco voador, o código do motor principal, a distância percorrida pelo disco (em anos-luz) e imprima "SIM" (se o disco requer revisão) ou "NAO" (se o disco não requer revisão no momento).

# Entrada
# Ano de produção
# Código do motor principal
# Distância percorrida em anos-luz

# Saída
# SIM/NAO (de acordo com o critério descrito no enunciado do exercício)

          ano = int(input())
          cod = int(input())
          dist = int(input())
          if (1901 <= ano<= 2000):
              if (cod == 100 or cod == 101):
                  print("SIM")
              else:
                  print("NAO")
          elif (2001 <= ano <= 2020):
              if (dist > 5000):
                  print("SIM")
              else:
                  print("NAO")
          elif(ano==2021):
              if ((cod == 200 or cod == 201) & (dist > 200)):
                  print("SIM")
              else:
                  print('NAO')
          else:
              print("NAO")

# 2_5
# Escreva um programa que leia os comprimentos dos lados de um triângulo. Após isso, verifique se é um triângulo válido. Observação: para um triângulo ser válido, nenhum dos lados pode ser mair que a soma dos outros dois lados.

# Entrada:
# Comprimento de cada um dos três lados

# Saída:
# Seu programa deve imprimir "VALIDO" se for um triângulo válido ou "INVALIDO" se não for. Importante: observe que a letra "A" em "VALIDO"/"INVALIDO" não tem acento neste programa.


      l1 = int(input())
      l2 = int(input())
      l3 = int(input())
      if ((l1+l2>l3) & (l2+l3>l1) & (l1+l3>l2)):
          print("VALIDO")
      else:
          print("INVALIDO")

# 2_6
# Escreva um programa que leia duas datas (dia, mês e ano) e então retorne qual das duas é a mais antiga.

# Entrada:
# 3 números inteiros (dia, mês e ano da data 1);
# 3 números inteiros (dia, mês e ano da data 2)

# Saída:
# Se a data 1 for mais antiga, imprima "DATA1" e, caso contrário, imprima "DATA2". Se as duas datas forem iguais, imprima "IGUAIS".

        dia1 = int(input())
        mes1 = int(input())
        ano1 = int(input())
        dia2 = int(input())
        mes2 = int(input())
        ano2 = int(input())
        dia = dia1-dia2
        mes = mes1-mes2
        ano = ano1-ano2
        if (ano >0):
            print("DATA2")
        elif ((ano == 0) & (mes >0)):
            print("DATA2")
        elif ((ano == 0) & (mes == 0) & (dia>0)):
            print("DATA2")
        elif ((ano == 0) & (mes == 0) & (dia == 0)):
            print("IGUAIS")
        else:
            print("DATA1")


# 2_7
# Escreva um programa que leia três números inteiros quaisquer, armazenando nas variáveis A, B e C. Após isso, imprima os números em ordem crescente.

# Entrada:
# Três números inteiros.

# Saída:
# Os três números em ordem crescente.

        a = int(input())
        b = int(input())
        c = int(input())
        ab = a-b
        bc = b-c
        ac = a-c

        if ((ab<=0) & (ac<=0)):
            print(a)
            if (bc>=0):
                print(c)
                print(b)
            else:
                print(b)
                print(c)
        elif ((ab>=0) & (bc<=0)):
            print(b)
            if (ac>=0):
                print(c)
                print(a)
            else:
                print(a)
                print(c)
        elif ((ac>=0) & (bc>=0)):
            print(c)
            if (ab>=0):
                print(b)
                print(a)
            else:
                print(a)
                print(b)
        else:
            print("none")



# 2_8
# Escreva um programa que leia os valores x e y de um ponto. A partir disso, determine se o ponto está dentro ou fora do retângulo a seguir:

        x = int(input())
        y = int(input())
        if ((-800 <= x <= 22 )&(-20 <= y <= 35)):
            print("SIM")
        else:
            print("NAO")

# 2_9
# Uma montadora de discos voadores possui fábricas em diversos planetas e faz entregas em diversas partes do universo. Essa empresa usa números de 6 dígitos para identificar a origem do disco, o destino do disco e o modelo, conforme formato a seguir:

# OODDMM:
# OO: código do planeta de origem (onde o disco voador foi fabricado)
# DD: código do planeta de destino (onde o disco voador será entregue)
# MM: código do modelo
# A empresa usa as seguintes tabelas com os códigos de planetas e modelos de discos voadores:
# Portanto, o número 809162 será usado para um disco voador fabricado em Marte (código 80), entregue em HD21749b (código 91) e do modelo C9000 (código 62).
# Escreva um programa que leia um número de 6 dígitos e então imprima o planeta de origem, o planeta de destino e o modelo.

# Entrada
# Número de 6 dígitos

# Saída
# Planeta de origem
# Planeta de destino
# Modelo do disco voador

        a = int(input())
        oo = (a%1000000)//10000
        dd = (a%100000)*100//10000
        mm = (a%100)*10000//10000

        if (dd>=100):
            dd=(a%10000)*1000//100000


        if (oo == 80):
            oo = "Marte"
        elif (oo == 81):
            oo = "Saturno"
        elif (oo == 90):
            oo = "Netuno"
        elif (oo == 91):
            oo = "HD21749b"

        if (dd == 80):
            dd = "Marte"
        elif (dd == 81):
            dd = "Saturno"
        elif (dd == 90):
            dd = "Netuno"
        elif (dd == 91):
            dd = "HD21749b"

        if (mm == 60):
            mm = "A6000"
        elif (mm == 61):
            mm = "B7500"
        else:
            mm = "C9000"
        print(oo)
        print(dd)
        print(mm)


# 2_10
# Um avião de carga possui uma autonomia que depende do peso da carga sendo transportada:

# A capacidade máxima desse avião é 250000kg. Além disso, dependendo das condições de voo, esse avião pode ter uma autonomia até 10% maior.
# Escreva um programa que recebe o peso total da carga, as coordenadas de partida (Ax, Ay) as coordenadas do destino (Bx, By) e então imprima a distância e também se o avião tem autonomia para chegar ao destino. Imprima:
# "SIM" (se o avião tem autonomia para chegar no destino com a carga)
# "TALVEZ" (se o avião tem autonomia para chegar no destino com a carga, mas considerando o adicional de 10% que depende de condições de voo)
# "NAO" (se o avião não tem autonomia para chegar no destino com a carga, mesmo considerando o adicional de 10% que depende de condições de voo)

# Para calcular a distância a ser percorrida (em km), considere a distância Euclidiana em linha reta entre os pontos (Ax,Ay) e (Bx,By). Veja o exercício EP1_4 - Distância entre pontos para detalhes sobre como calcular a distância entre dois pontos.

# Considere que o avião apenas é usado para cargas inferiores a 250000kg e, portanto, não é necessário prever o caso que a carga é superior a sua capacidade máxima.

# Entrada
# Carga (em kg)
# Ax
# Ay
# Bx
# By

# Saída
# Distância (imprima o valor com duas casas decimais após a vírgula)
# SIM/TALVEZ/NAO (de acordo com os critérios apresentados no enunciado)

        carga = int(input())
        Ax = int(input())
        Ay = int(input())
        Bx = int(input())
        By = int(input())

        import math
        dist= math.sqrt((Bx-Ax)**2+(By-Ay)**2)
        print("{:.2f}".format(dist))

        if (carga <= 50000):
            if (dist<=18000):
                print("SIM")
            elif (dist<=(18000*1.1)):
                print("TALVEZ")
            else:
                print("NAO")
        elif (50000 < carga <= 200000):
            if (dist<=9000 ):
                print("SIM")
            elif (dist<=(9000*1.1)):
                print("TALVEZ")
            else:
                print("NAO")
        elif (200000 < carga <= 250000):
            if (dist<=3000  ):
                print("SIM")
            elif (dist<=(3000*1.1)):
                print("TALVEZ")
            else:
                print("NAO")
