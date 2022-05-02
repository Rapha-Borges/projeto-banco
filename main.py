from ContasBancos import ContaCorrente, CartaoCredito
from Agencia import AgenciaVirtual, AgenciaPremium, AgenciaComun

# programa

agencia_premium_especial = AgenciaPremium('22-2222-2222', '444.444.444-78')

# Criando as contas
# conta_Lira = ContaCorrente("Lira", "111.222.333-45", 1052, 39394, 5)
#
# conta_Rapha = ContaCorrente("Rapha", "222.333.444-55", 1052, 38954, 5)
#
# cartao_Lira = CartaoCredito("Lira", conta_Lira)
#
# print(conta_Lira.__dict__)
# print(cartao_Lira.__dict__)
#
# # Realizando as transações
#
# conta_Lira.consulta_conta()
#
# conta_Lira.consultar_limite_chequeespecial()
#
# conta_Lira.consultar_saldo()
#
# conta_Lira.depositar(5000)
#
# conta_Lira.consultar_saldo()
#
# conta_Lira.sacar(40)
#
# conta_Lira.transferir(1000, conta_Rapha)
#
# conta_Lira.consultar_saldo()
#
# conta_Rapha.consultar_saldo()
#
# print('-' * 20)
#
# conta_Lira.consultar_historico_transacoes()
#
# conta_Rapha.consultar_historico_transacoes()
#
# print(cartao_Lira.conta_corrente.agencia)
#
# print(cartao_Lira.numero)
# print(cartao_Lira.cod_seguranca)
# print(cartao_Lira.validade)
#
# help(ContaCorrente)
