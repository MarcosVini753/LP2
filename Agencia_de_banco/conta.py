from emprestimo import Emprestimo
class Conta:

    def __init__(self, numero:int, titular:str, saldo:float):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.emprestimos = []

    def sacar(self, valor:float):
        if(self.saldo >= valor):
            self.saldo -= valor
            return True
        return False

    def depositar(self, valor:float):
        self.saldo += valor

    def transferir(self, conta_destino:'Conta', valor:float):
        if(self.sacar(valor)):
            conta_destino.depositar(valor)
            return True
            
        return False
    
    def fazer_emprestimo(self, valor:float, parcelas:int):
        self.emprestimos.append(Emprestimo(valor, parcelas))
        self.depositar(valor)
    
    def pagar_parcela_emprestimo(self, emprestimo:Emprestimo):
        if(emprestimo.pagar_parcela(self.saldo)):
            self.saldo -= emprestimo.parcelas_valor
            return True
        return False
    
    def __str__(self):
        return f"{self.numero} - {self.titular} - R$ {self.saldo:.2f}{"\nEmprestimos:\n" + "".join([x.__str__() for x in self.emprestimos]) if len(self.emprestimos) else ""}\n"