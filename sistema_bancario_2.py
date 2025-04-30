"""
Projeto: Sistema Bancário
Versão: 2.0
Descrição: Aprimoramento do sistema bancário com o uso funções e implementação de novas funcionalidades (cadastro de usuários/clientes e contas) 
Autor: Luis Fabiano Tesser
Data de Criação/Ultima modificação: 29/04/2025
"""

# ========= Definição das funções ==============

# Implementação do menu principal
def exibe_menu():
    menu = '''
        [d]  Depositar
        [s]  Sacar
        [e]  Extrato
        [nu] Novo Usuário
        [lu] Lista Usuários
        [nc] Nova Conta
        [lc] Lista Contas
        [q]  Sair

        =>'''
    opcao = input(menu).lower()
    return opcao


# Implementação da função depositar
def depositar(saldo, extrato, /):
    valor = float(input('Informe o valor a ser depositado: '))
    if valor > 0:
        saldo += valor
        extrato += f'Depósito\tR$ {valor:,.2f}\n'
        print('Operação realizada com sucesso!😊')
    else:
        print('Valor inválido. Operação cancelada!☠️')
    return saldo, extrato


# Implementação da função sacar
def sacar(*, saldo, extrato, limite, numero_saques, limite_saques):
    if numero_saques >= limite_saques:
        print(f'O limite de {numero_saques} saques diários já foi atingido. Operação cancelada!☠️')
    else:
        valor = float(input('Informe o valor a ser sacado: '))
        if valor <= 0:
            print('Valor inválido. Operação cancelada!☠️')
        elif valor > 500:
            print(f'Valor excedeu o limite de R$ {limite:.2f}. Operação cancelada!☠️')
        elif valor > saldo:
            print(f'Saldo insuficiente! O seu saldo atual é de R$ {saldo:,.2f}. Operação cancelada!☠️')
        else:
            saldo -= valor
            numero_saques += 1
            extrato += f'Saque\t\tR$ {valor:,.2f}\n'
            print('Operação realizada com sucesso!😊')
    return saldo, extrato, numero_saques


# Implementação da função exibe extrato
def exibe_extrato(saldo, /, *, extrato):
    print('\n' + ' EXTRATO '.center(40, '='))
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'\nSaldo: R$ {saldo:,.2f}')
    print(''.center(40, '='))
    return


# Verifica se o cpf já está cadastrado na lista de clientes
# Returna True se já existe e False se não encontrou
def verifica_cpf_ja_existe(cpf, clientes):
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            return True
    return False


# Cria um novo cliente / usuário
def novo_usuario(clientes):
    cpf = input('Informe o número do CPF do novo cliente: ')
    if verifica_cpf_ja_existe(cpf, clientes):
        print('O CPF informado já está cadastrado! Operação cancelada!☠️')
        return
    nome = input('Nome completo: ')
    data_nasc = input('Data de Nascimento (dd/mm/aaaa): ')
    endereco = input('Endereço (Logradouro - Número - Bairro - Cidade/Sigla Estado): ')
    clientes.append({'cpf': cpf, 'nome': nome, 'data_nascimento': data_nasc, 'endereco': endereco})
    print('Cliente adicionado. Operação realizada com sucesso!😊')
    return


# Exibe a lista de usuários/clientes
def lista_usuarios(clientes):
    for cliente in clientes:
        print(cliente)
    return


def nova_conta(contas, clientes):
    if not contas:
        numero_conta = 1
    else:
        numero_conta = contas[-1]['conta'] + 1
    # numero_conta = len(contas) + 1 - código alternativo para definir o número da conta que está sendo criada
    cpf = input('Informe o CPF do cliente: ')
    if verifica_cpf_ja_existe(cpf, clientes):
        contas.append({'conta': numero_conta, 'agencia': '0001', 'cliente': cpf})
        print(f'Conta {numero_conta} criada. Operação realizada com sucesso!😊')
    else:
        print(f'O CPF {cpf} não está cadastrado! Operação cancelada!☠️')
    return


# Exibe a lista de contas
def lista_contas(contas):
    for conta in contas:
        print(conta)
    return


# Função principal
def main():
    AGENCIA = '0001'
    LIMITE_SAQUES = 3
    contas = []
    clientes = []
    saldo = 0
    limite_por_saque = 500
    extrato = ''
    numero_saques = 0
    

    while True:
        opcao = exibe_menu()
        if opcao == 'd': 
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == 's':
            saldo, extrato, numero_saques = sacar(saldo= saldo, extrato= extrato, limite= limite_por_saque, numero_saques= numero_saques, limite_saques=LIMITE_SAQUES)
        elif opcao == 'e':
            exibe_extrato(saldo, extrato= extrato)
        elif opcao == 'nu':
            novo_usuario(clientes)
        elif opcao == 'lu':
            lista_usuarios(clientes)
        elif opcao == 'nc':
            nova_conta(contas, clientes)
        elif opcao == 'lc':
            lista_contas(contas)
        elif opcao == 'q': 
            break
        else:
            print('Opção inválida! Digite a letra referente a operação')
    return()



# início da execução do programa
#-----------------------------------------------------
if __name__ == '__main__': 
    main() # chamada da função main
