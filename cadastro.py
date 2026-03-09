# usuarios = {
#     "joao": {"senha": "123", "saldo": 1000},
#     "ana": {"senha": "abc", "saldo": 500},
#     "pedro": {"senha": "999", "saldo": 200}
dicionario = {
    "joao": {"senha": "123", "saldo": 1000},
    "ana": {"senha": "abc", "saldo": 500},
    "pedro": {"senha": "999", "saldo": 200}
}
historico = []
#login
chances = 0
while chances < 3:
    usuario =input('digite seu user')
    senha = input('digite sua senha')
    if usuario in dicionario and senha == dicionario[usuario]['senha']:
       print('usuario encontrado') 
       break
    else:
       print('chances',chances + 1)
    chances +=1
    if chances == 3:
       print('acesso negado')
       break
 # 3) Após login correto, mostrar MENU em loop:
# 1 - Ver saldo
# 2 - Sacar
# 3 - Depositar
# 4 - Transferir
# 5 - Sair
def menu():
    while True:
        ação = input('Digite a ação que você quer realizar: ').lower()
        
        if ação == 'ver saldo':
            print(dicionario[usuario]['saldo'])
            historico.append(f'{usuario} viu saldo')
        
        elif ação == 'sacar':
            sacar = int(input('Digite o valor do saque: '))
            if sacar > dicionario[usuario]['saldo']:
                print('Saldo insuficiente')
            else:
                dicionario[usuario]['saldo'] -= sacar
                print('Saque realizado, novo saldo:', dicionario[usuario]['saldo'])
                historico.append(f'{usuario} sacou {sacar}')
        
        elif ação == 'depositar':
            depositar = int(input('Digite o valor do depósito: '))
            dicionario[usuario]['saldo'] += depositar
            print('Seu saldo com o depósito ficou', dicionario[usuario]['saldo'])
            historico.append(f'{usuario} depositou {depositar}')
        
        elif ação == 'tranferir':
            tranferi = int(input('Digite o valor da transferência: '))
            if tranferi > dicionario[usuario]['saldo']:
                print('Saldo insuficiente para transferência')
            else:
                dicionario[usuario]['saldo'] -= tranferi
                print('Desconto com sua transferência, saldo atual:', dicionario[usuario]['saldo'])
                historico.append(f'{usuario} transferiu {tranferi}')
        
        elif ação == 'ver historico':
            if historico:
                print('Histórico de ações:')
                for h in historico:
                    print(h)
            else:
                print('Nenhuma ação registrada ainda.')
        
        elif ação == 'sair':
            print('Ok saindo...')
            break
        
        else:
            print('Ação inválida')


menu()
