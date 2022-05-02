from random import randint


class Agencia:
    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verifica_caixa(self, caixa_min):
        if self.caixa < caixa_min:
            print('Caixa abaixo do nível recomendado. Caixa atual R$ {:,.2f}'.format(self.caixa))
        else:
            print('O valor de caixa está ok. Caixa atual R$ {:,.2f}'.format(self.caixa))

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print('Emprestimo não disponível!')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))


class AgenciaVirtual(Agencia):
    def __init__(self, site, telefone, cnpj):
        self.site = site
        super().__init__(telefone, cnpj, numero=randint(5000, 5999))
        self.caixa = 1000000
        self.caixa_paypal = 0

    def depositar_paypal(self, valor):
        self.caixa -= valor
        self.caixa_paypal += valor

    def sacar_paypal(self, valor):
        self.caixa += valor
        self.caixa_paypal -= valor
        
    def verifica_caixa(self):
        caixa_min = 1000000
        super().verifica_caixa(caixa_min)


class AgenciaComun(Agencia):
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 3999))
        self.caixa = 1000000
        
    def verifica_caixa(self):
        caixa_min = 1000000
        super().verifica_caixa(caixa_min)


class AgenciaPremium(Agencia):
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(4000, 4999))
        self.caixa = 10000000
        
    def verifica_caixa(self):
        caixa_min = 10000000
        super().verifica_caixa(caixa_min)

    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            super().adicionar_cliente(nome, cpf, patrimonio)
            print('Cliente adicionado')
        else:
            print('Patrimonio baixo')


if __name__ == '__main__':
    agencia1 = Agencia('51-3333-3333', '00.123.456/0001-78', 1053)
    agencia_virtual1 = AgenciaVirtual('www.agenciateste.com.br', '51-5555-5555', '11.111.111/0001-22')
    agencia_premium1 = AgenciaPremium('51-4444-4444', '11.222.333/0001-44')

    agencia_premium1.adicionar_cliente('Andressa', '888.888.888-88', 10000000)
    print(agencia_premium1.clientes)

    # print(agencia_virtual1.caixa)
    # agencia_virtual1.depositar_paypal(20000)
    # print(agencia_virtual1.caixa)
    # print(agencia_virtual1.caixa_paypal)

    # agencia_premium1.verifica_caixa()
    # agencia_virtual1.verifica_caixa()

    # agencia1.caixa = 1000000
    # agencia1.verifica_caixa()
    #
    # agencia1.emprestar_dinheiro(1500, '222.222.222-12', 0.02)
    # print(agencia1.emprestimos)
    #
    # agencia1.adicionar_cliente('Lira', '213.123.123-12', 10000)
    # print(agencia1.clientes)
