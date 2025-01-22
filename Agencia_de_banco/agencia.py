from conta import Conta
class Agencia:
    
    def __init__(self, numero:int, nome:str):
        self.numero = numero
        self.nome = nome
        self.contas = []

    def adicionar_conta(self, numero:int, titular:str, saldo:float):
        self.contas.append(Conta(numero, titular, saldo))

    def buscar_conta(self, numero:int):
        for conta in self.contas:
            if(conta.numero == numero):
                return conta
        return None

    def remover_conta(self, numero:int):
        conta = self.buscar_conta(numero)
        if(conta):
            self.contas.remove(conta)
            return True
        return False
    
    def fechar_agencia(self):
        self.conta.clear()

    def __str__(self):
        return f"{self.numero} - {self.nome}"