class SistemaBancario:
    def __init__(self):
        self.usuarios = []

    def encontrar_usuario_por_cpf(self, cpf):
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                return usuario
        return None

    def criar_usuario(self):
        nome = input("Digite o nome: ")
        data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
        
        while True:
            cpf = input("Digite o CPF (somente números): ")
            if not cpf.isdigit():
                print("\nCPF inválido! O CPF deve conter apenas números.")
            elif len(cpf) != 11:
                print("\nCPF inválido! O CPF deve ter 11 dígitos.")
            elif self.encontrar_usuario_por_cpf(cpf):
                print("\nCPF já cadastrado! Não é possível cadastrar o mesmo CPF duas vezes.")
            else:
                break

        endereco = input("Digite o endereço (Ex: Rua A, 123 - Bairro - Cidade/UF): ")

        usuario = Usuario(nome, data_nascimento, cpf, endereco)
        self.usuarios.append(usuario)
        print(f"\nUsuário {nome} cadastrado com sucesso!")
