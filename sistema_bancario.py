menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).lower()

    if opcao == 'd': # Implementação da operação de depósito
        valor = float(input('Informe o valor a ser depositado: '))
        if valor > 0:
            saldo += valor
            extrato += f'Depósito\tR$ {valor:,.2f}\n'
        else:
            print('Valor inválido. Operação cancelada! ')
  
    elif opcao == 's': # Implementação da operação de saque
        if numero_saques >= LIMITE_SAQUES:
            print(f'O limite de {numero_saques} saques diários já foi atingido. Operação cancelada!')
        else:
            valor = float(input('Informe o valor a ser sacado: '))
            if valor <= 0:
                print('Valor inválido. Operação cancelada!')
            elif valor > 500:
                print(f'Valor excedeu o limite de R$ {limite:.2f}. Operação cancelada!')
            elif valor > saldo:
                print(f'Saldo insuficiente! O seu saldo atual é de R$ {saldo:,.2f}. Operação cancelada!')
            else:
                saldo -= valor
                numero_saques += 1
                extrato += f'Saque\t\tR$ {valor:,.2f}\n'
    
    elif opcao == 'e': # Implementação da operação de extrato
        print('\n' + ' EXTRATO '.center(40, '='))
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:,.2f}')
        print(''.center(40, '='))
    
    elif opcao == 'q': # Implementação da operação de saida do sistema
        break

    else:
        print('Opção inválida! Digite a letra referente a operação')

