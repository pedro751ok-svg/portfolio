import random

def adivinhe_lista():
    lista = ['caio','lucas','pedro','marcos']
    escolha = input(f'escolha alguem que voce pense que é o impostor {lista}')
    impostor = random.choice(lista)
    while escolha != impostor:
        escolha = input('escolha novamente')
    if escolha == impostor:
        print('você descobriu o impostor')
    else:
        print('tennte novamente')
        
def num_aleatori(): 
    num1 = int(input('digite um numero: '))
    num2 = random.randint(0,11)
    while num2 != num1:
      num1 = int(input('digite um numero: '))
    if num1 == num2:
        print('parabéns')
    else:
        print('voce errou tente novamente: ')    



adivinhe_lista()
num_aleatori()