class Sistema():
    def __init__(self):
        self.saldo = 0
        self.extrato = []
        self.limite_saque = 3
        self.saques_realizados = 0

    def ver_saldo(self):
        print(f'''\nSeu saldo atual é: R${self.saldo}''')
   
    def depositar(self, valor):
        if valor <= 0:
            print('''\nO valor do deposito deve ser positivo.''')
        else:
            self.saldo += valor
            self.extrato.append(f"Depósito: R${valor:.2f}")
            print(f'''\nDepósito de R${valor:.2f} feito com sucesso!''')
   
    def sacar(self, valor):
        if valor <= 0:
            print('''\nO valor de saque deve ser positivo.''')
        elif self.saques_realizados >= self.limite_saque:
            print('''\nLimite de saques diários atingido!''') 
            return opcao
        elif valor > 500:
            print('''\nO valor máximo a ser sacado é R$500''')
        elif valor > self.saldo:
            print('''\nSaldo insuficiente!''')
        else:
            self.saldo -= valor
            self.saques_realizados += 1
            self.extrato.append(f"Saque: R${valor:.2f}")
            print(f'''\nSaque de: R${valor:.2f} bem sucedido!''')
   
    def ver_extrato(self):
        print('''\n           <=========> EXTRATO <=========>''')
        if not self.extrato:
            print('''\n             Nenhuma transação realizada.''')
        else:
            for transacao in self.extrato:
                print(f'''\n                {transacao}''')
        print('''\n           <=========> EXTRATO <=========>''')
        
def pausar():
    input('''\nPressione Enter para voltar...''')
 
conta = Sistema() 
while True:            
    print('''           <=========> MENU <=========>
            
                        1. Saldo
                        2. Deposito
                        3. Saque
                        4. Extrato
                        5. Sair
            
            <=========> MENU <=========>''')          

    try:

        opcao = int(input("\n               Digite uma opção: "))

        if opcao == 1:
            conta.ver_saldo()
            pausar()
        
        elif opcao == 2:
            valor = float(input('''\nDigite o valor do depósito: '''))
            conta.depositar(valor)
            pausar()
        
        elif opcao == 3:
            valor = float(input('''\nDigite o valor a ser sacado: '''))
            conta.sacar(valor)
            pausar()
        
        elif opcao == 4:
            conta.ver_extrato()
            pausar()
                
        elif opcao == 5:
            print('''\nFinalizando sessão...''')
            break
        
        else:
            print('''\nOpção inválida. Tente novamente.''')
            
    except ValueError:
        print('''\nOpção inválida. Digite uma das opções.''')
