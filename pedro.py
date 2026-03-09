def validar_cpf(cpf):
    cpf = int(input('digite seu cpf: '))
    cpf = ''.join(filter(str.isdigit))
    if len(cpf) != 11:
        print('seu cpf nao esta completo')
    if cpf == cpf * len(cpf):
        print('cpf invalido')

validar_cpf()