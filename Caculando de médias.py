                      ##Cálculo de média
##Definindo as váriaveis e o input
from time import sleep
i = 1
quant = maior = menor = media = 0
per = int(input('Quantos números você quer tirar a média? '))
##Um laço de repetição, inputando os numeros da média
while i < per+1:
  num = float(input(f'Digite o {i}º número: '))
  ##Definindo os contadores e o valor que eles devem ir subindo a  cada ação/input
  i += 1
  quant += 1
  ##Estruturas condicionais 
  if quant == 1:
    maior = menor = num
  else:
      if num > maior:
        maior = num
      if num < menor:
        menor = num
  ##Calculos para a média
media = maior /2 + menor / 2
##Printando os valores e a média
print(f'O maior nota foi de {maior}, o menor foi {menor} e a média deles foi {media}')
