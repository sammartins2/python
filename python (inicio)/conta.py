
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print ("Construindo objeto ...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato (self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita (self, valor):
        print("Deposito feito na conta de {}".format (self.__titular))
        self.__saldo += valor

    def saca (self, valor):
        if(valor <= (self.__saldo + self.__limite)):
            print("Saque realizado com sucesso")
            self.__saldo -= valor
        else:
            print("O valor {} passou do limite da conta".format(valor))
    
    def transferir (self, valor, destino):
        print("Transferencia realizada com sucesso da conta {}".format(self.__titular))
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self): #get sempre possui um retorno
        return self.__saldo

    @property
    def titular(self): 
        return self.__titular

    @property
    def limite(self): 
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}