
estoque_atual = 100
estoque_minimo = 20


def atualizar_estoque(quantidade, tipo_movimento):
    global estoque_atual

    print(f"--- Processando: {tipo_movimento} de {quantidade} itens ---")

    if tipo_movimento == 'entrada':
        estoque_atual += quantidade
        print(f"Entrada registrada com sucesso!")
    elif tipo_movimento == 'saida':
        if quantidade <= estoque_atual:
            estoque_atual -= quantidade
            print(f"Saída registrada com sucesso!")
        else:
            print(f"Atenção: Não há produtos suficientes para esta saída. Estoque atual: {estoque_atual}")
    else:
        print("Erro: Tipo de movimento inválido. Use 'entrada' ou 'saida'.")

    print(f"Novo estoque atual: {estoque_atual}")
    return estoque_atual


def verificar_estoque():
    """
    Verifica se o estoque atual está abaixo do mínimo definido e exibe um alerta.
    """
    print("\n--- Verificando Estoque ---")
    if estoque_atual <= estoque_minimo:
        print(f"ALERTA: Estoque baixo! Apenas {estoque_atual} unidades restantes.")
        print("É necessário fazer a reposição de produtos.")
    else:
        print(f"Estoque em nível adequado. Unidades: {estoque_atual}")
    print("--------------------------\n")



print("### INÍCIO DA OPERAÇÃO ###")
print(f"Estoque inicial: {estoque_atual}")
print(f"Estoque mínimo definido: {estoque_minimo}")
verificar_estoque()


atualizar_estoque(50, 'entrada')
verificar_estoque()


atualizar_estoque(30, 'saida')
verificar_estoque()

atualizar_estoque(110, 'saida')
verificar_estoque()

atualizar_estoque(50, 'saida')
verificar_estoque()
