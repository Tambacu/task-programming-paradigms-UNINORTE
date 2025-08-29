class Product:
    def __init__(self, id, name, unit, quantity, min_quantity, description):
        self.id = id
        self.name = name
        self.unit = unit
        self.quantity = quantity
        self.min_quantity = min_quantity
        self.description = description

    def __str__(self):
        return f"ID: {self.id} - {self.name} - {self.quantity} {self.unit} (Mín: {self.min_quantity}) - {self.description}"

class Inventory:
    def __init__(self):
        self.products = []
        self.nextID = 1
        self.units = ['kg', 'g', 'l', 'ml', 'unidade(s)', 'm', 'cm']

    def add_product(self, name, unit, quantity, min_quantity, description):
        product = Product(self.nextID, name, unit, quantity, min_quantity, description)
        self.products.append(product)
        self.nextID += 1
        print(f"'{name}' foi adicionado ao estoque com sucesso!\n")

    def update_stock(self, id_product, quantity_change):
        for product in self.products:
            if product.id == id_product:
                product.quantity += quantity_change
                if product.quantity < 0:
                    product.quantity = 0
                print(f"Estoque de '{product.name}' atualizado para {product.quantity} {product.unit}.\n")
                return
        print("Produto não encontrado.\n")

    def check_restock(self):
        low_stock = [p for p in self.products if p.quantity < p.min_quantity]
        if low_stock:
            print("\n Produtos que precisam de reposição:")
            for p in low_stock:
                print(p)
        else:
            print("\n Todos os produtos estão acima do estoque mínimo.\n")

    def list_products(self):
        if self.products:
            print("\n Estoque atual:\n")
            for product in self.products:
                print(product)
        else:
            print("\nNenhum produto no estoque. Adicione itens primeiro!\n")

def show_menu():
    print("\n---- Menu Estoque ----")
    print("1 - Listar produtos")
    print("2 - Adicionar produto")
    print("3 - Registrar entrada de produto")
    print("4 - Registrar saída de produto")
    print("5 - Verificar necessidade de reposição")
    print("6 - Sair do sistema")

def get_unit():
    print("\nEscolha uma medida: ")
    for i, unit in enumerate(inventory.units, 1):
        print(f"{i}. {unit}")
    while True:
        try:
            choose = int(input("\nInforme o número da unidade: "))
            if 1 <= choose <= len(inventory.units):
                return inventory.units[choose - 1]
            else:
                print("\nOpção inválida. Tente novamente.")
        except ValueError:
            print("\nEntrada inválida. Tente novamente.")

def main():
    print("---- Sistema de Controle de Estoque ----")

    while True:
        show_menu()
        try:
            choose = int(input("\nO que deseja? "))

            if choose == 1:
                inventory.list_products()

            elif choose == 2:
                name = input("Informe o nome do produto: ")
                unit = get_unit(inventory.units)
                while True:
                    try:
                        quantity = float(input("Informe a quantidade inicial: "))
                        break
                    except ValueError:
                        print("Quantidade inválida. Digite um número válido.")
                while True:
                    try:
                        min_quantity = float(input("Informe o estoque mínimo: "))
                        break
                    except ValueError:
                        print("Valor inválido. Digite um número válido.")
                description = input("Informe a descrição do produto: ")
                inventory.add_product(name, unit, quantity, min_quantity, description)

            elif choose == 3:
                try:
                    id_product = int(input("Informe o ID do produto: "))
                    quantity = float(input("Informe a quantidade de entrada: "))
                    inventory.update_stock(id_product, quantity)
                except ValueError:
                    print("Entrada inválida. Tente novamente.")

            elif choose == 4:
                try:
                    id_product = int(input("Informe o ID do produto: "))
                    quantity = float(input("Informe a quantidade de saída: "))
                    inventory.update_stock(id_product, -quantity)
                except ValueError:
                    print("Entrada inválida. Tente novamente.")

            elif choose == 5:
                inventory.check_restock()

            elif choose == 6:
                print("Saindo do sistema!")
                break

            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Tente um número válido.")

inventory = Inventory()

if __name__ == "__main__":
    main()
