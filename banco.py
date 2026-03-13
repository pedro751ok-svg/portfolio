import time 
lista = []
def menu():
   while True:
      try:
         opção = input('escreva umas das opções| cadastrar | login | sair |')
         if opção == 'cadastrar':
            cadastrar()
         elif opção == 'login':
            login()
         elif opção == 'sair':
            print('fechando sistema...')
            break
      except ValueError:
         print('ação invalida')   
         return
def cadastrar():
 # MENU PRINCIPAL
# 1 - Cadastrar usuário
# 2 - Fazer login
# 3 - Listar usuários
# 4 - Remover usuário
# 5 - Sair
   print('TE DIREICIONANDO PARA ABA DE CADASTRO')
   time.sleep(3)
   print('BEM VINDO A TELA DE CADASTRO')
   while True:    
      try:  
         nome = input('por favor informe seu nome completo: ')
         senha = int(input('crie uma senha: '))
         c_senha = int(input('confirme sua senha: '))
         if c_senha != senha:
            print('as senhas nao concidem: ')
            continue
         idade = int(input('por favor infome sua idade: '))
         if idade < 18:
            print('este banco permite entrada apenas de maiores: ')
            continue
         elif idade > 99:
            print('opa dinossauro')
            continue
         cpf = input('informe seu cpf: ' )
         cpf = '' .join(filter(str.isdigit,cpf))
         if len(cpf) != 11:
            print('quantidade de caracteres insuficiente')
            continue
         if cpf == cpf[0]*len(cpf):
            print('cpf invalido')
            continue
         historico = { 'nome':nome,
                         'idade': idade,
                         'cpf': cpf,
                        'senha':senha,
                        'saldo': 0,
                        'historico': []
                      }
         lista.append(historico)
         print('ANALISANDO DADOS')
         time.sleep(3)
         print('CADASTRO FINALIZADO COM SUCESSO')
         return
      except ValueError:
         print('erro')
# login, onde ususario colocara todas informações salvas no dicionario,
# e a função ira verfifcar se estra tud certo

def login():
      while True:  
            if not lista:
               print('nenhum usuario encontrado')
               return
         
            nome1 = input('Insira seu nome de usuário: ')
            senha2 = int(input('Insira sua senha: '))
            cpf1 = input('Insira seu CPF: ')
            cpf1 = ''.join(filter(str.isdigit, cpf1))  
         
            for cadastro in lista:
               if cadastro['nome'] == nome1 and cadastro['senha'] == senha2 and cadastro['cpf'] == cpf1:
                  menu2(cadastro)
                  return
            
               
               
            print('usuario nao encontrado confirme seus dados')


def menu2(usuario):
# 1 - ver saldo
#2 - depositar
#3 - sacar
#4 - histórico
#5 - sair da conta
   while True:      
         print('1 - ver saldo')
         print('2 - depositar')
         print('3 - sacar')
         print('4 - historico')
         print('5 - sair da conta')
         ação = int(input('selecione uma ação que você deseja realizar: '))
         if ação == 1:
          print('seu saldo atual é',usuario['saldo'])
         
         elif ação == 2:
            val = int(input('digite um valor que você deseja depositar'))
            usuario['saldo'] += val
            usuario['historico'].append('depositou {}'.format(val))
            print(usuario['historico'])
         elif ação == 3:
            val = int(input('digite um valor que você deseja sacar'))
            usuario['saldo']-= val
            usuario['historico'].append('sacou {}'.format(val))
            print(usuario['historico'])
            print(lista)
         elif ação == 4:
           for h in usuario['historico']:
              print(h)

         elif ação == 5:
            break
     
         else:
            print('ação invalida tente novamente')
            return


menu()