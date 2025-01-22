class Emprestimo:

    def __init__(self, valor:float, parcelas:int):
        self.valor = valor
        self.parcelas = parcelas
        self.parcelas_valor = valor / parcelas
    
    def pagar_parcela(self, saldo_conta:float):
        if(saldo_conta >= self.parcelas_valor and self.parcelas > 0):
            self.valor -= self.parcelas_valor
            self.parcelas -= 1 
            return True
        return False
    
    def __str__(self):
        return f"R$ {self.valor:.3f} - {self.parcelas} x R$ {self.parcelas_valor:.3f}\n"
    
