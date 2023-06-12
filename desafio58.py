# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar
# mostrando no final quantos palpites foram necessários para vencer.
from random import randint
computador = randint(0, 10)
print('Vou pensar em um numero de 0 a 10, tente adivinhar...')
jogador = int(input('Em que numero eu pensei? '))
tentativas = 1
while jogador != computador:
    jogador = int(input('Você errou! Digite outro numero: '))
    tentativas += 1
if jogador == computador:
    print('Você ganhou! Você precisou de {} tentaivas para acertar'.format(tentativas))
