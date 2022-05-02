from datetime import datetime
from random import randint
import pytz


class ContaCorrente:
    """
        Documentar:
    """

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, num_conta, digito_conta):
        self.nome = nome
        self.cpf = cpf
        self._saldo = 0
        self._limite = 0
        self.agencia = agencia
        self.num_conta = num_conta
        self.digito_conta = digito_conta
        self._transacoes = []
        self.cartoes = []

    def consultar_saldo(self):
        print('O saldo atual de {} é de R$ {:,.2f}'.format(self.nome, self._saldo))

    def depositar(self, valor):
        self._saldo += valor
        print('Depósito de R$ {:,.2f} realizado com sucesso na conta de {}'.format(valor, self.nome))
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))

    def _limite_conta(self):
        self._limite = -1000
        return self._limite

    def sacar(self, valor):
        if self._saldo - valor > self._limite_conta():
            self._saldo -= valor
            print('Saque de R$ {:,.2f} realizado com sucesso.'.format(valor))
            if self._saldo < 0:
                print('Você está no chque especial')
            self.consultar_saldo()
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
        else:
            print("Saldo insuficiente para saque")
            self.consultar_saldo()

    def consultar_limite_chequeespecial(self):
        print('O limite de Cheque Especial de {} é de R$ {:,.2f}'.format(self.nome, self._limite_conta() * -1))

    def consulta_conta(self):
        print('Agência: {}  Conta: {}-{}'.format(self.agencia, self.num_conta, self.digito_conta))

    def consultar_historico_transacoes(self):
        print('Histórico de transacoes de {}:'.format(self.nome))
        for transacao in self._transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
        conta_destino._saldo += valor
        conta_destino._transacoes.append((-valor, conta_destino._saldo, ContaCorrente._data_hora()))
        print('{} transferiu R$ {:,.2f} para a conta de {}'.format(self.nome, valor, conta_destino.nome))


class CartaoCredito:
    """
        Documentar:
    """

    @staticmethod
    def _data():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR

    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular
        self.validade = "{}/{}".format(CartaoCredito._data().month, CartaoCredito._data().year + 4)
        self.cod_seguranca = '{}{}{}'.format(randint(0, 9), randint(0, 9), randint(0, 9))
        self.limite = 1000
        self._senha = '1234'
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
            print('Sua nova senha é {}'.format(valor))
        else:
            print('Favor verificar os dados de senha inseridos')
