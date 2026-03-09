import time 
lista = []
def menu_p():
 # MENU PRINCIPAL
# 1 - Cadastrar usuário
# 2 - Fazer login
# 3 - Listar usuários
# 4 - Remover usuário
# 5 - Sair
  opção, historico = input('escreva a ação que voce deseja realizar | cadastrar | login |')
  if opção == 'cadastrar':
   print('TE DIREICIONANDO PARA ABA DE CADASTRO')
   time.sleep(3)
   print('BEM VINDO A TELA DE CADASTRO')
   while True:
      try:    
         senha = int(input('crie uma senha'))
         c_senha = int(input('confirme sua senha'))
         nome = input('por favor informe seu nome completo')
         idade = int(input('por favor infome sua idade'))
         if idade < 18:
            print('este banco permite entrada apenas de maiores de idade.')
            break
         cpf = input('informe seu cpf' )
         cpf = '' .join(filter(str.isdigit,cpf))
         if len(cpf) != 11:
            print('quantidade de caracteres insuficiente')
         if cpf[0] == cpf * len(cpf):
            print('cpf invalido')
            raise ValueError('cpf deve conter numeros diferentes')
         if c_senha != senha:
            print('senhas nao concidem')
         print('ANALISANDO DADOS')
         time.sleep(3)
         print('CADASTRO FINALIZADO COM SUCESSO')
         historico = { 'nome':nome,
                         'idade': idade,
                         'cpf': cpf,
                        'senha':senha
                      }
         lista.append(historico)
         return opção, historico
      except ValueError:
            print('ERRO AO SE CADASTRAR')



def login():
   opção,historico = menu_p()
   for cadastro in lista:
      if opção == 'login':
         print('CARREGANDO TELA DE LOGIN')
         time.sleep(3)
         print('BEM VINDO A TELA DE LOGIN')
      senha2 = int(input('insira sua senha'))
      nome1 = input(' insira seu nome de usuario')
      cpf1 = input('insira seu cpf')
      if historico['nome'] != nome1:
        if historico['senha'] != senha2:
         if historico['cpf'] != cpf1:
            print('usuario nao encontrado')

login()


