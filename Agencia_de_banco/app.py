from agencia import Agencia

#testes básicos

a = Agencia(1, "Agencia do Banco do Brasil")

a.adicionar_conta(1, "Joao", 1000)
a.adicionar_conta(2, "Maria", 2000)

conta1 = a.buscar_conta(1)

print(conta1)

conta1.fazer_emprestimo(600, 4)

print(conta1)

conta1.pagar_parcela_emprestimo(conta1.emprestimos[0])

print(conta1)