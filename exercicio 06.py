#exercício 06: jogo de adivinhar um número em 3 niveis de dificuldade e contador de tentativas
import random
contador=0
nivel=int(input(" \n escolha um nivel: \n \n 1) facil 0 a 5 \n 2) médio 0 a 50 \n 3) difícil 0 a 100 \n \n"))

if nivel==1:
  sorteio = random.randint(0,10)
elif nivel == 2:
  sorteio = random.randint(0,50)
elif nivel == 3:
  sorteio = random.randint(0,100)

tentativa=int(input("informe um numero: "))

while tentativa != sorteio:
  print("voce errou! \n")
  if tentativa <= sorteio:
    print("escolha um numero maior")
  elif tentativa >= sorteio:
    print("escolha um numero menor")

  tentativa=int(input("informe um numero: "))
  contador=contador+1

if tentativa == sorteio:
  print("\n parabens, voce acertou! \n")
  print(f"o numero sorteado foi {sorteio}\n")
  print(f"o numero de tentativas foi: {contador + 1}")