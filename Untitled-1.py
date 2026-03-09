#cirar cadastro de usuarios usando dicionario dentro de lista, loop e tratamento de erros
import time
lista_cd = []
def cadastro(): 
        print ('BEM VINDO A TELA DE CADASTRO')
        nome  = input('informe seu nome completo: ')
        while True:
            try:
                    idade = int(input('informe sua idade: '))
                    if idade < 18:
                        print('esse site e apenas para maiores de idade')
                        return
                    senha = int(input('crie sua senha: '))
                    c_senha = int(input('confirme sua senha: '))
                    if senha == c_senha:
                        print('LOGIN CRIADO COM SUCESSO')
                        cadastrados = { 'nome': nome,
                                    'idade': idade,
                                    'senha': senha,
                           }
                        lista_cd.append(cadastrados)
                        return cadastrados
                    else:
                         print('senhas nao condizem tente novamente')
            except ValueError:
                print('digite apenas numeros')



def login():
    cadastro()
    print('CARREGANDO O LOGIN')
    time.sleep(3)
    print('BEM VINDO A TELA DE LOGIN')

    while True:
        try:
                nome2 = input('informe seu nome de ususario: ')
                for login in lista_cd:
                    if nome2 == login['nome']:
                        print(f'seja bem vindo {nome2}')
                        senha_l = int(input('confirme sua senha: '))
                        if senha_l == login['senha']:
                            print('senha correta')
                            return
                        else:
                            print('senha ou ususario nao enconttrado')
        except ValueError:
                print('use apenas numeros na senha e letras no nome')

login()