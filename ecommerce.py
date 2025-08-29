import time
import statistics

def exibir_menu():
    opcao = input('''
    Digite 1. para iniciar o cadastro das vendas
    Digite 2. para sair
    Opção: ''')
    return opcao

def cadastrar_vendas():
    semanas = ['segunda', 'terça', 'quarta', 'quinta', 'sexta']
    # semanas = ['segunda', 'terça']
    valor_vendas_semanas = []
    for semana in semanas:
        valor_do_dia: float = 0
        print(f'''
        Digite 1. para iniciar o cadastro de {semana}
        Digite 2. para voltar ao menu principal
        Digite 3. para finalizar o programa''')
        cadastro_option = input('Opção: ')

        if cadastro_option == "3":
            print('Saindo do programa...')
            exit()

        elif cadastro_option == '2':
            print('Voltando ao menu principal...')
            time.sleep(1)
            return

        elif cadastro_option == '1':
            while True:
                print(f'Digite o valor do produto da {semana} ou Digite "." para sair ou digite "finalizar" para finalizar o dia')
                valor_produto = input('R$: ')

                if valor_produto == '.':
                    print('voltando para o menu principal')
                    return

                if valor_produto.lower() == 'finalizar':
                    valor_vendas_semanas.append(valor_do_dia)
                    break
                try:
                    valor_produto = float(valor_produto)
                except ValueError:
                    print('pfv insira um caractere valido')

                if isinstance(valor_produto, float):
                    print('adicionando ao total do dia')
                    valor_do_dia = valor_do_dia + valor_produto
                    print(f'valor do produto é {valor_produto}')
                    print(f'valor do dia é {valor_do_dia}')
    return valor_vendas_semanas

def main():
    while True:
        opcao_menu = exibir_menu()

        match opcao_menu:
            case '2':
                print('Saindo do programa.....')
                exit()
            case '1':
                print('Você selecionou a opção 1... iniciando o cadastro das vendas\n')
                time.sleep(1)
                vendas_semana = cadastrar_vendas()
                break
            case _:
                print('Opção inválida')
                time.sleep(1)

    maior_venda = max(vendas_semana)
    media_vendas = statistics.mean(vendas_semana)
    total_vendas = sum(vendas_semana)

    print(f'''
A media das vendas é: R${media_vendas}
A maior venda em um dia é: R${maior_venda}
O total de todas as vendas é: R${total_vendas}''')

if __name__ == '__main__':
    main()
