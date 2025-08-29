import time

saldo = 1000.00

def mostrar_saldo():
    print(f'Seu saldo atual é: R${saldo:.2f}')

def depositar(valor):
    global saldo
    if valor > 0:
        saldo += valor
        print(f'\nDepósito de R${valor:.2f} realizado com sucesso')
    else:
        print('\nValor de depósito inválido')

def sacar(valor):
    global saldo
    if valor > 0 and valor <= saldo:
        saldo -= valor
        print(f'\nSaque de R${valor:.2f} realizado com sucesso')
    elif valor > saldo:
        print('\nSaldo insuficiente para realizar o saque')
    else:
        print('\nValor de saque inválido.')

def main():
    while True:
        print('\n--- Sistema Bancário ---')
        print('1. Mostrar Saldo')
        print('2. Depositar')
        print('3. Sacar')
        print('4. Sair')
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            mostrar_saldo()
            time.sleep(0.5)
        elif opcao == '2':
            try:
                valor = input('Digite o valor para depositar: ')
                valor = float(valor)
                depositar(valor)
                time.sleep(0.5)
                print('valor depositado com sucesso!')
            except ValueError:
                print('Por favor digite um número válido')
        elif opcao == '3':
            try:
                valor = float(input('Digite o valor para sacar: '))
                sacar(valor)
                time.sleep(0.5)
                print('valor sacado com sucesso!')
            except ValueError:
                print('Por favor digite um número válido.')
        elif opcao == '4':
            print('Saindo do programa...')
            time.sleep(0.5)
            break
        else:
            print('Opção inválida')

if __name__ == '__main__':
    main()
