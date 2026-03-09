import math
import random
# calculadora simplififcada, calculando mdc
num  = int(input('dgite um numero: '))
num2 = int(input('digite outro numero: '))
result = math.gcd(num,num2)
print(f'seu mdc é {result}')
def pog_2():
   raiz = int(input('digite um numero paraa ver sua raiz: '))
   pg = math.sqrt(raiz)
   print(f'o calculo da raiz quadadra é {pg}')
#  chamar função animal
pog_2()
def unsual_2():
   dg1 = float(input('digite um numero para elevar: ').replace(',','.'))
   dg2 = float(input('digite um numero para elevar o primeiro numero que vopce digitou: ').replace(',','.'))
   elevado = math.pow(dg1,dg2)
   print(f' o {dg1} elevado ao {dg2} fica {elevado}')
unsual_2()
# numero random
def cassino():
   import random
num =int(input('digite um numero de 1 a 5: '))
num1 = random.randint(1,5)
while num != num1:
    num =int(input('digite novamente'))
if num == num1:
    print('pa-ra-bens')
elif num > 5:
    print('é so de 1 a 5 animal')    
else:
    print('errrroooou')


cassino()   