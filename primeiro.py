import time
lista = []
def cadastro():
      nome = input('digite seu nome: ')
      idade = int(input('digite sua idade: '))
      
      while True:
       senha =int(input('crie uma senha: '))
       c_senha = int(input('confirma sua senha: '))
       if c_senha != senha:
           print('tente novamente')
       elif c_senha == senha:
            print('cadastro concluido')
            cadastrados = {'nome':nome,
                         'idade': idade,
                         'senha': senha,
                         }
            lista.append(cadastrados)
            return cadastrados
                  

def login():
    cadastro()

    print('CARREGANDO...')
    time.sleep(2)
    print('BEM VINDO A TELA DE LOGIN')
    while True:
            nome1 = input('digite seu nome: ')
            senha2 = int(input('digite sua senha: '))
            for usuario in lista:
              if usuario['nome'] == nome1:
               if usuario['senha'] == senha2:
                  print('SEJA BEM VINDO')
                  return
               else:
                   print('usuario nao encontrado')

login()

#MENU COM INTERAÇÕES DO ESTOQUE, FUNÇÕES COMO, ADICIONAR,VER QUANTIDADE,RETIRAR DO ESTOQUE.
def menu():
    estoque = {'arroz': 20,
        'feijão': 17,
        'café': 10,
        'leite': 28,
        'refrigerantes':18}
    while True:
        ação = input('|ver estoque|, |adicionar item|, |ver quantidade,|retirar item|')
        if ação == 'ver estoque':
         for armazen in estoque:
            print(armazen)
        if ação == 'ver quantidade':
            produto = input('escola o produto que você quer ver a quantidade')
            print(produto,estoque[produto])
        
        if ação == 'adicionar item':
            add_item = input('escreva o item que voce quer adicionar')
            qtde = int(input('escreva a quantidade'))
            estoque[add_item] = qtde
        
        if ação == 'retirar item':
            ret_item = input('escreva o item que voce deseja retirar do estoque')
            del estoque[ret_item] 
        
menu()