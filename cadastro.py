class Restaurante:
    def __init__(self):
        self.clientes = {}

    def cadastrar_cliente(self, cpf):
        if cpf not in self.clientes:
            self.clientes[cpf] = []
        else:
            print("Cliente já cadastrado.")

    def registrar_entrada(self, cpf, data):
        if cpf in self.clientes:
            self.clientes[cpf].append(data)
            print(f"Entrada registrada para o CPF {cpf} na data {data}.")
        else:
            print("Cliente não encontrado.")

    def mostrar_registros(self, cpf):
        if cpf in self.clientes:
            print(f"Registros de entrada para o CPF {cpf}:")
            for data in self.clientes[cpf]:
                print(data)
        else:
            print("Cliente não encontrado.")


if __name__ == "__main__":
    restaurante = Restaurante()

    while True:
        print("\n1. Cadastrar Cliente")
        print("2. Registrar Entrada")
        print("3. Mostrar Registros de Entrada")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cpf = input("Digite o CPF do cliente: ")
            restaurante.cadastrar_cliente(cpf)
        elif opcao == "2":
            cpf = input("Digite o CPF do cliente: ")
            data = input("Digite a data (DD/MM/AAAA): ")
            restaurante.registrar_entrada(cpf, data)
        elif opcao == "3":
            cpf = input("Digite o CPF do cliente: ")
            restaurante.mostrar_registros(cpf)
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
